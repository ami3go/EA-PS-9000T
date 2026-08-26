"""
Production-oriented EA Elektro-Automatik PS 9000 T serial/SCPI driver.

This file is a drop-in replacement for the original prototype file and keeps the
old public API names where practical:

    ps = EaPs9000T()
    ps.set_voltage(10)
    ps.set_current(1)
    ps.output_on()
    ps.output_off()
    ps.close()

Important safety changes compared with the prototype:
    * failed connection raises an exception instead of creating a half-valid object;
    * send() returns after a successful write instead of sending the same command
      retry_cnt times;
    * query() treats empty replies as timeouts;
    * serial port state is checked before every operation;
    * close() can switch output off before releasing remote control;
    * range errors are rejected by high-level setter methods;
    * logging and custom exceptions replace print-only error handling;
    * context manager support is added.

The command-builder classes from the original file are still available, for
example:

    cmd = storage()
    cmd.source.voltage.val(10)       -> 'SOUR:VOLTage 10V'
    cmd.source.current.ovc.val(5)    -> 'SOUR:CURRent:PROTection 5'
    cmd.output.on()                  -> 'OUTP ON'

Notes:
    * Nominal limits differ between PS 9000 T models. The defaults below match
      the original prototype assumptions: 500 V, 5 A, 3000 W. Pass explicit
      limits for your exact supply model.
    * This driver uses SCPI over a serial port. pyvisa is intentionally not used.
"""

from __future__ import annotations

import logging
import math
import re
import time
import warnings
from dataclasses import dataclass
from typing import Iterable, Optional, Sequence, Tuple, Union

try:
    import serial
    import serial.tools.list_ports
except ImportError as _exc:  # allows importing command builders without pyserial installed
    serial = None  # type: ignore[assignment]
    SerialException = OSError
    _PY_SERIAL_IMPORT_ERROR = _exc
else:
    SerialException = serial.SerialException
    _PY_SERIAL_IMPORT_ERROR = None

Number = Union[int, float]


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------


class EAPSError(Exception):
    """Base class for all EA PS 9000 T driver errors."""


class InstrumentNotFoundError(EAPSError):
    """Raised when no matching serial device can be found."""


class DependencyError(EAPSError):
    """Raised when a required Python dependency is missing."""


class CommunicationError(EAPSError):
    """Raised for serial write/read failures."""


class CommandTimeoutError(CommunicationError):
    """Raised when a query receives no reply before timeout."""


class RemoteControlError(EAPSError):
    """Raised when remote-control lock cannot be obtained or verified."""


class InstrumentCommandError(EAPSError):
    """Raised when the instrument reports a SCPI command error."""


class RangeError(ValueError, EAPSError):
    """Raised when a requested setpoint is outside configured safe limits."""


# ---------------------------------------------------------------------------
# Configuration / helpers
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PowerSupplyLimits:
    """Electrical limits for one concrete EA PS 9000 T model."""

    voltage_min: float = 0.0
    voltage_max: float = 500.0
    current_min: float = 0.0
    current_max: float = 5.0
    power_min: float = 0.0
    power_max: float = 3000.0
    resistance_min: float = 0.0
    resistance_max: float = 10000.0
    ovp_min: float = 0.0
    ovp_max: float = 500.0
    ocp_min: float = 0.0
    ocp_max: float = 5.0
    opp_min: float = 0.0
    opp_max: float = 3000.0


def _require_pyserial() -> None:
    if serial is None:
        raise DependencyError(
            "pyserial is required for EA PS 9000 T communication. "
            "Install it with: pip install pyserial"
        ) from _PY_SERIAL_IMPORT_ERROR


def get_com_port_by_keyword(keyword: str) -> Optional[str]:
    """
    Return the first COM/device path whose description contains *keyword*.

    Example return values:
        Windows: 'COM3'
        Linux:   '/dev/ttyUSB0'

    Returns None if no matching device is found.
    """
    _require_pyserial()
    if not keyword:
        return None

    keyword_lower = keyword.lower()
    for port in serial.tools.list_ports.comports():
        description = (port.description or "").lower()
        manufacturer = (getattr(port, "manufacturer", "") or "").lower()
        product = (getattr(port, "product", "") or "").lower()
        hwid = (getattr(port, "hwid", "") or "").lower()
        haystack = " ".join((description, manufacturer, product, hwid))
        if keyword_lower in haystack:
            return port.device
    return None


def list_serial_ports() -> list[str]:
    """Return all visible serial device names."""
    _require_pyserial()
    return [comport.device for comport in serial.tools.list_ports.comports()]


def _format_number(value: Number) -> str:
    """Format a SCPI numeric value without unnecessary trailing zeros."""
    value_f = float(value)
    if value_f.is_integer():
        return str(int(value_f))
    return f"{value_f:.12g}"


def _coerce_float(value: Number, name: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise RangeError(f"{name} must be numeric, got {value!r}") from exc


def validate_range(value: Number, min_val: Number, max_val: Number, name: str) -> float:
    """Return value as float if it is within range, otherwise raise RangeError."""
    value_f = _coerce_float(value, name)
    min_f = float(min_val)
    max_f = float(max_val)
    if not math.isfinite(value_f):
        raise RangeError(f"{name} must be finite, got {value_f!r}")
    if value_f < min_f or value_f > max_f:
        raise RangeError(f"{name}={value_f:g} is outside allowed range {min_f:g}..{max_f:g}")
    return value_f


def range_check(val: Number, min: Number, max: Number, val_name: str):  # noqa: A002 - kept for old API
    """
    Backward-compatible clamp helper used by the old command-builder classes.

    The original function silently clamped and printed. For compatibility this
    still returns a clamped value, but it emits a warning so production code can
    detect accidental out-of-range usage. High-level EaPs9000T.set_* methods use
    strict validation and raise RangeError instead.
    """
    value = _coerce_float(val, val_name)
    min_f = float(min)
    max_f = float(max)

    if value > max_f:
        warnings.warn(
            f"{val_name}={value:g} is above maximum {max_f:g}; clamping for legacy compatibility",
            RuntimeWarning,
            stacklevel=2,
        )
        return max
    if value < min_f:
        warnings.warn(
            f"{val_name}={value:g} is below minimum {min_f:g}; clamping for legacy compatibility",
            RuntimeWarning,
            stacklevel=2,
        )
        return min
    return val


def parse_numeric_response(response: str) -> float:
    """
    Parse a numeric SCPI response that may include units.

    Examples:
        '12.34V' -> 12.34
        '1.2E-3 A' -> 0.0012
    """
    match = re.search(r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", response.strip())
    if not match:
        raise ValueError(f"No numeric value found in response {response!r}")
    return float(match.group(0))


def parse_csv_numeric_response(response: str) -> tuple[float, ...]:
    """Parse comma-separated numeric response values that may include units."""
    return tuple(parse_numeric_response(item) for item in response.split(",") if item.strip())


# ---------------------------------------------------------------------------
# Main driver
# ---------------------------------------------------------------------------


class EaPs9000T:
    """
    EA PS 9000 T serial/SCPI driver.

    Backward-compatible basic usage:

        ps = EaPs9000T()
        ps.set_voltage(10)
        ps.set_current(1)
        ps.output_on()
        ps.output_off()
        ps.close()

    Recommended production usage:

        limits = PowerSupplyLimits(voltage_max=80, current_max=40, power_max=1500,
                                   ovp_max=88, ocp_max=44, opp_max=1650)
        with EaPs9000T(port="COM8", limits=limits, auto_remote=True) as ps:
            ps.set_ovp(30)
            ps.set_ocp(2)
            ps.set_voltage(24)
            ps.set_current(1)
            ps.output_on(verify=True)
            print(ps.measure_all())
    """

    def __init__(
        self,
        port: Optional[str] = None,
        baudrate: int = 115200,
        timeout: float = 1.0,
        write_timeout: float = 1.0,
        keyword: str = "PS 9000 T",
        retry_cnt: int = 3,
        retry_delay: float = 0.2,
        limits: Optional[PowerSupplyLimits] = None,
        auto_connect: bool = True,
        auto_remote: bool = True,
        verify_remote: bool = False,
        safe_close: bool = True,
        output_off_on_close: bool = True,
        logger: Optional[logging.Logger] = None,
    ):
        self.cmd = storage(limits=limits)
        self.ser: Optional[serial.Serial] = None
        self.port = port
        self.baudrate = int(baudrate)
        self.timeout = float(timeout)
        self.write_timeout = float(write_timeout)
        self.keyword = keyword
        self.retry_delay = float(retry_delay)
        self.limits = limits or PowerSupplyLimits()
        self.safe_close = bool(safe_close)
        self.output_off_on_close = bool(output_off_on_close)
        self.logger = logger or logging.getLogger(self.__class__.__name__)
        self._retry_cnt = 3
        self.retry_cnt = retry_cnt
        self.idn: Optional[str] = None

        if auto_connect:
            self.connect(port=port, auto_remote=auto_remote, verify_remote=verify_remote)

    @property
    def retry_cnt(self) -> int:
        return self._retry_cnt

    @retry_cnt.setter
    def retry_cnt(self, value: int) -> None:
        value = int(value)
        if value < 1:
            raise ValueError("retry_cnt must be >= 1")
        self._retry_cnt = value

    @property
    def is_connected(self) -> bool:
        return self.ser is not None and bool(self.ser.is_open)

    def __enter__(self) -> "EaPs9000T":
        if not self.is_connected:
            self.connect(auto_remote=True)
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def connect(
        self,
        port: Optional[str] = None,
        auto_remote: bool = True,
        verify_remote: bool = False,
    ) -> str:
        """
        Open the serial port, query *IDN?, and optionally enter remote mode.

        Returns the identification string.
        """
        if self.cmd is None:
            self.cmd = storage(limits=self.limits)

        if self.is_connected:
            return self.idn or ""

        selected_port = port or self.port or get_com_port_by_keyword(self.keyword)
        if selected_port is None:
            ports = list_serial_ports()
            raise InstrumentNotFoundError(
                f"No EA PS 9000 T serial port found with keyword {self.keyword!r}. "
                f"Visible ports: {ports}"
            )

        self.port = selected_port
        _require_pyserial()
        try:
            self.ser = serial.Serial(
                port=selected_port,
                baudrate=self.baudrate,
                timeout=self.timeout,
                write_timeout=self.write_timeout,
            )
        except SerialException as exc:
            raise CommunicationError(f"Could not open serial port {selected_port!r}") from exc

        self.idn = self.query("*IDN?")
        self.logger.info("Connected to EA power supply: %s", self.idn)

        if auto_remote:
            self.remote_on(verify=verify_remote)
        return self.idn

    def _require_open(self) -> serial.Serial:
        if self.ser is None:
            raise CommunicationError("Serial port is not open: self.ser is None")
        if not self.ser.is_open:
            raise CommunicationError(f"Serial port {self.port!r} is closed")
        return self.ser

    def _write_once(self, command: str) -> None:
        ser = self._require_open()
        payload = f"{command}\r\n".encode("ascii")
        ser.write(payload)
        ser.flush()

    def send(self, txt: str) -> None:
        """
        Send one SCPI command.

        Kept for backward compatibility. Unlike the prototype, a successful write
        returns immediately; the command is not sent retry_cnt times.
        """
        last_exc: Optional[BaseException] = None
        command = str(txt).strip()
        if not command:
            raise ValueError("Cannot send an empty SCPI command")

        for attempt in range(1, self._retry_cnt + 1):
            try:
                self._write_once(command)
                self.logger.debug("SCPI write: %s", command)
                return
            except (SerialException, OSError, CommunicationError) as exc:
                last_exc = exc
                self.logger.warning(
                    "SCPI write failed on attempt %d/%d: %s",
                    attempt,
                    self._retry_cnt,
                    command,
                    exc_info=True,
                )
                if attempt < self._retry_cnt:
                    time.sleep(self.retry_delay)

        raise CommunicationError(f"Failed to send SCPI command {command!r}") from last_exc

    def query(self, cmd_srt: str) -> str:
        """
        Send one SCPI query and return a stripped text response.

        The old method name and misspelled parameter name are kept for backward
        compatibility with existing code.
        """
        last_exc: Optional[BaseException] = None
        command = str(cmd_srt).strip()
        if not command:
            raise ValueError("Cannot query an empty SCPI command")

        for attempt in range(1, self._retry_cnt + 1):
            try:
                ser = self._require_open()
                try:
                    ser.reset_input_buffer()
                except (SerialException, OSError):
                    # Some Serial-like test doubles may not support this.
                    pass

                self._write_once(command)
                raw = ser.readline()
                if not raw:
                    raise CommandTimeoutError(f"No reply to query {command!r}")

                response = raw.decode("ascii", errors="replace").strip()
                self.logger.debug("SCPI query: %s -> %s", command, response)
                return response
            except (SerialException, OSError, UnicodeDecodeError, CommunicationError) as exc:
                last_exc = exc
                self.logger.warning(
                    "SCPI query failed on attempt %d/%d: %s",
                    attempt,
                    self._retry_cnt,
                    command,
                    exc_info=True,
                )
                if attempt < self._retry_cnt:
                    time.sleep(self.retry_delay)

        raise CommunicationError(f"Failed to query SCPI command {command!r}") from last_exc

    def close(
        self,
        output_off: Optional[bool] = None,
        remote_off: bool = True,
        suppress_errors: bool = True,
    ) -> None:
        """
        Close the driver safely.

        By default, this turns output off and releases remote mode before closing.
        Pass output_off=False only when another controller intentionally continues
        controlling the supply.
        """
        if output_off is None:
            output_off = self.output_off_on_close

        if self.ser is None:
            self.cmd = None
            return

        errors: list[BaseException] = []
        if self.ser.is_open:
            if self.safe_close and output_off:
                try:
                    self.output_off()
                except BaseException as exc:  # keep close robust during shutdown
                    errors.append(exc)
                    self.logger.warning("Could not switch output off during close", exc_info=True)
            if remote_off:
                try:
                    self.remote_off()
                except BaseException as exc:
                    errors.append(exc)
                    self.logger.warning("Could not release remote mode during close", exc_info=True)
            try:
                self.ser.close()
            except BaseException as exc:
                errors.append(exc)
                self.logger.warning("Could not close serial port", exc_info=True)

        self.ser = None
        self.cmd = None

        if errors and not suppress_errors:
            raise CommunicationError(f"Errors occurred during close: {errors!r}")

    # ------------------------------------------------------------------
    # High-level commands, old names kept
    # ------------------------------------------------------------------

    def set_voltage(self, val: Number) -> None:
        value = validate_range(val, self.limits.voltage_min, self.limits.voltage_max, "voltage")
        self.send(self.cmd.source.voltage.val(value))

    def get_voltage_setpoint(self) -> float:
        return parse_numeric_response(self.query(self.cmd.source.voltage.req()))

    def set_current(self, val: Number) -> None:
        value = validate_range(val, self.limits.current_min, self.limits.current_max, "current")
        self.send(self.cmd.source.current.val(value))

    def get_current_setpoint(self) -> float:
        return parse_numeric_response(self.query(self.cmd.source.current.req()))

    def set_power(self, val: Number) -> None:
        value = validate_range(val, self.limits.power_min, self.limits.power_max, "power")
        self.send(self.cmd.source.power.val(value))

    def get_power_setpoint(self) -> float:
        return parse_numeric_response(self.query(self.cmd.source.power.req()))

    def output_on(self, verify: bool = False) -> None:
        self.send(self.cmd.output.on())
        if verify and not self.is_output_on():
            raise InstrumentCommandError("OUTP ON was sent, but output state did not become ON")

    def output_off(self, verify: bool = False) -> None:
        self.send(self.cmd.output.off())
        if verify and self.is_output_on():
            raise InstrumentCommandError("OUTP OFF was sent, but output state is still ON")

    def is_output_on(self) -> bool:
        reply = self.query(self.cmd.output.req())
        return _parse_bool_response(reply)

    def remote_on(self, verify: bool = False) -> None:
        self.send(self.cmd.system.lock.on())
        if verify:
            owner = self.get_remote_owner()
            if owner and "REMOTE" not in owner.upper():
                raise RemoteControlError(f"Remote lock not active. Owner response: {owner!r}")

    def remote_off(self) -> None:
        self.send(self.cmd.system.lock.off())

    def get_remote_owner(self) -> str:
        return self.query(self.cmd.system.lock.owner.req())

    def get_errors(self) -> str:
        """Backward-compatible name. Returns all SCPI errors as raw text."""
        return self.query(self.cmd.system.error_all.req())

    def read_error(self) -> str:
        return self.query(self.cmd.system.error.req())

    def check_errors(self) -> None:
        """Raise InstrumentCommandError if the SCPI error queue reports an error."""
        errors = self.get_errors()
        normalized = errors.strip().upper()
        if normalized and not normalized.startswith("0") and "NO ERROR" not in normalized:
            raise InstrumentCommandError(errors)

    def clear_status(self) -> None:
        self.send(self.cmd.cls.str())

    def reset(self) -> None:
        self.send(self.cmd.reset.str())

    def read_status_byte(self) -> int:
        reply = self.query(self.cmd.read_status.req())
        return int(parse_numeric_response(reply))

    def set_ovp(self, val: Number) -> None:
        value = validate_range(val, self.limits.ovp_min, self.limits.ovp_max, "OVP")
        self.send(self.cmd.source.voltage.ovp.val(value))

    def set_ocp(self, val: Number) -> None:
        value = validate_range(val, self.limits.ocp_min, self.limits.ocp_max, "OCP")
        self.send(self.cmd.source.current.ocp.val(value))

    def set_ovc(self, val: Number) -> None:
        """Deprecated compatibility alias for set_ocp()."""
        warnings.warn("set_ovc() is deprecated; use set_ocp()", DeprecationWarning, stacklevel=2)
        self.set_ocp(val)

    def set_opp(self, val: Number) -> None:
        value = validate_range(val, self.limits.opp_min, self.limits.opp_max, "OPP")
        self.send(self.cmd.source.power.opp.val(value))

    # ------------------------------------------------------------------
    # Measurement helpers
    # ------------------------------------------------------------------

    def measure_voltage(self) -> float:
        return parse_numeric_response(self.query(self.cmd.measure.voltage.req()))

    def measure_current(self) -> float:
        return parse_numeric_response(self.query(self.cmd.measure.current.req()))

    def measure_power(self) -> float:
        return parse_numeric_response(self.query(self.cmd.measure.power.req()))

    def measure_all(self) -> dict[str, float]:
        """
        Return measured voltage/current/power.

        Uses individual queries for broad compatibility. If your exact firmware
        supports a faster MEAS:ARR? command, you can use query('MEAS:ARR?')
        directly or add a model-specific optimized method.
        """
        return {
            "voltage_v": self.measure_voltage(),
            "current_a": self.measure_current(),
            "power_w": self.measure_power(),
        }


# ---------------------------------------------------------------------------
# Command-builder classes kept for compatibility with the original file
# ---------------------------------------------------------------------------


class req3:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self.cmd = self.prefix

    def req(self) -> str:
        return self.cmd + "?"


class str3:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self.cmd = self.prefix

    def str(self) -> str:
        return self.cmd


class dig_param3:
    def __init__(self, prefix: str, min: Number, max: Number):  # noqa: A002 - old API
        self.prefix = prefix
        self.cmd = self.prefix
        self.max = max
        self.min = min
        self.ending = ""

    def val(self, count: Number = 0) -> str:
        count = range_check(count, self.min, self.max, "value")
        txt = f"{self.cmd} {_format_number(count)}{self.ending}"
        return txt


class query_only(req3):
    """Command node that intentionally supports only query syntax."""

    def val(self, *args, **kwargs) -> str:
        raise AttributeError(f"{self.cmd!r} is query-only; use .req()")


class str_on_off:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self.cmd = self.prefix
        self.owner = req3(self.prefix + ":OWN")

    def on(self) -> str:
        return self.cmd + " ON"

    def off(self) -> str:
        return self.cmd + " OFF"

    def req(self) -> str:
        return self.cmd + "?"


class speed:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self.cmd = self.prefix

    def fast(self) -> str:
        return self.cmd + " FAST"

    def slow(self) -> str:
        return self.cmd + " SLOW"


class range_resolution:
    def __init__(self, prefix: str, min: Number, max: Number):  # noqa: A002 - old API
        self.prefix = prefix
        self.cmd = self.prefix
        self.max = max
        self.min = min

    def val(self, count: Number = 0) -> str:
        count = range_check(count, self.min, self.max, "value")
        txt = f"{self.cmd} {_format_number(count)}"
        return txt


class storage:
    """Root command storage class from the original file."""

    def __init__(self, limits: Optional[PowerSupplyLimits] = None):
        self.cmd = None
        self.prefix = None
        self.limits = limits or PowerSupplyLimits()
        self.measure = measure()
        self.system = system()
        self.output = str_on_off("OUTP")
        self.source = source(self.limits)
        self.idn = req3("*IDN")
        self.cls = str3("*CLS")
        self.reset = str3("*RST")
        self.read_status = req3("*STB")


class configure(req3):
    def __init__(self, limits: Optional[PowerSupplyLimits] = None):
        self.limits = limits or PowerSupplyLimits()
        self.prefix = "CONFigure"
        self.cmd = "CONFigure"
        self.current = current(self.prefix, self.limits.current_min, self.limits.current_max)
        self.voltage = voltage(self.prefix, self.limits.voltage_min, self.limits.voltage_max)


class voltage(dig_param3, req3):
    def __init__(self, prefix: str, min_val: Number = 0, max_val: Number = 500):
        self.min = min_val
        self.max = max_val
        self.prefix = prefix + ":" + "VOLTage"
        self.cmd = self.prefix
        self.ending = "V"
        self.ovp = Protection(self.prefix, min_val, max_val)


class current(dig_param3, req3):
    def __init__(self, prefix: str, min_val: Number = 0, max_val: Number = 5):
        self.min = min_val
        self.max = max_val
        self.prefix = prefix + ":" + "CURrent"
        self.cmd = self.prefix
        self.ending = "A"
        protection = Protection(self.prefix, min_val, max_val)
        self.ovc = protection  # old, incorrect name kept
        self.ocp = protection  # correct alias


class source:
    def __init__(self, limits: Optional[PowerSupplyLimits] = None):
        self.limits = limits or PowerSupplyLimits()
        self.cmd = "SOUR"
        self.prefix = "SOUR"
        self.current = current(self.prefix, self.limits.current_min, self.limits.current_max)
        self.voltage = voltage(self.prefix, self.limits.voltage_min, self.limits.voltage_max)
        self.power = spwr(self.prefix, self.limits.power_min, self.limits.power_max)
        self.resistance = sres(self.prefix, self.limits.resistance_min, self.limits.resistance_max)


class Protection(req3, dig_param3):
    def __init__(self, prefix: str, min_val: Number, max_val: Number):
        self.min = min_val
        self.max = max_val
        self.ending = ""
        self.prefix = prefix + ":" + "PROTection"
        self.cmd = self.prefix


class spwr(dig_param3, req3):
    def __init__(self, prefix: str, min_val: Number = 0, max_val: Number = 3000):
        self.min = min_val
        self.max = max_val
        self.prefix = prefix + ":" + "POWER"
        self.cmd = self.prefix
        self.ending = "W"
        self.opp = Protection(self.prefix, min_val, max_val)


class sres(dig_param3, req3):
    def __init__(self, prefix: str, min_val: Number = 0, max_val: Number = 10000):
        self.min = min_val
        self.max = max_val
        self.prefix = prefix + ":" + "RESISTANCE"
        self.cmd = self.prefix
        self.ending = "OHM"


class system:
    def __init__(self):
        self.cmd = "SYST"
        self.prefix = "SYST"
        self.lock = str_on_off(self.prefix + ":LOCK")
        self.error = req3(self.prefix + ":ERR")
        self.error_all = req3(self.prefix + ":ERR:ALL")
        self.config = syst_conf(self.prefix)


class syst_conf:
    def __init__(self, prefix: str = "SYST"):
        self.cmd = prefix + ":CONF"
        self.prefix = self.cmd
        self.controller = controller(self.prefix)


class controller:
    def __init__(self, prefix: str):
        self.cmd = prefix + ":CONT"
        self.prefix = self.cmd
        self.speed = speed(self.prefix + ":SPE")


class measure:
    def __init__(self):
        self.cmd = "MEASure"
        self.prefix = "MEASure"
        self.current = query_only(self.prefix + ":CURRent")
        self.voltage = query_only(self.prefix + ":VOLTage")
        self.power = query_only(self.prefix + ":POWer")
        self.array = req3(self.prefix + ":ARRay")


# ---------------------------------------------------------------------------
# Internal parsing helpers
# ---------------------------------------------------------------------------


def _parse_bool_response(reply: str) -> bool:
    text = reply.strip().upper()
    if text in {"1", "ON", "TRUE", "YES"}:
        return True
    if text in {"0", "OFF", "FALSE", "NO"}:
        return False
    # Some instruments return a numeric value with units or text.
    try:
        return bool(int(parse_numeric_response(text)))
    except Exception as exc:
        raise ValueError(f"Cannot parse boolean response {reply!r}") from exc


# ---------------------------------------------------------------------------
# Safe demonstration. No real output is enabled unless explicitly requested.
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="EA PS 9000 T driver smoke test")
    parser.add_argument("--port", default=None, help="Serial port, e.g. COM8 or /dev/ttyUSB0")
    parser.add_argument("--connect", action="store_true", help="Actually connect and query *IDN?")
    args = parser.parse_args()

    cmd = storage()
    print(cmd.source.voltage.req())
    print(cmd.source.voltage.val(10))
    print(cmd.source.current.ovc.val(5))
    print(cmd.source.voltage.ovp.val(500))

    if args.connect:
        with EaPs9000T(port=args.port, auto_remote=False) as ps:
            print(ps.idn)
            print(ps.get_errors())
