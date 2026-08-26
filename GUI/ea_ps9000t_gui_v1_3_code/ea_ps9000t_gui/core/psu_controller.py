from __future__ import annotations

import logging
import threading
from dataclasses import dataclass, field
from typing import Optional

from EAPS9000T_class import EaPs9000T, PowerSupplyLimits, list_serial_ports

from .exceptions import NotConnectedError
from .mock_psu import MockFaultConfig, MockPsu

logger = logging.getLogger(__name__)


@dataclass
class PsuConnectionConfig:
    mock_mode: bool = True
    port: Optional[str] = None
    keyword: str = "PS 9000 T"
    baudrate: int = 115200
    timeout: float = 1.0
    write_timeout: float = 1.0
    retry_cnt: int = 3
    retry_delay: float = 0.2
    production_mode: bool = False
    auto_remote: bool = True
    verify_remote: bool = False
    safe_close: bool = True
    output_off_on_close: bool = True
    measurement_array_supported: bool = False
    expected_idn_contains: list[str] = field(default_factory=list)
    expected_model: Optional[str] = None
    expected_serial: Optional[str] = None
    station_id: Optional[str] = None
    limits: PowerSupplyLimits = field(default_factory=PowerSupplyLimits)
    mock_faults: MockFaultConfig = field(default_factory=MockFaultConfig)


class PsuController:
    """Thread-safe facade over real EaPs9000T or MockPsu backend."""

    def __init__(self):
        self._lock = threading.RLock()
        self._psu = None
        self._config: Optional[PsuConnectionConfig] = None
        self._last_voltage: Optional[float] = None
        self._last_current: Optional[float] = None
        self._last_power: Optional[float] = None
        self._last_ovp: Optional[float] = None
        self._last_ocp: Optional[float] = None
        self._last_opp: Optional[float] = None
        self.output_state_unknown = False

    @staticmethod
    def available_ports() -> list[str]:
        try:
            return list_serial_ports()
        except Exception as exc:
            logger.warning("Could not list serial ports: %s", exc)
            return []

    @property
    def config(self) -> Optional[PsuConnectionConfig]:
        return self._config

    @property
    def limits(self) -> PowerSupplyLimits:
        if self._config:
            return self._config.limits
        return PowerSupplyLimits()

    def connect(self, config: PsuConnectionConfig) -> str:
        with self._lock:
            self.disconnect(suppress_errors=True)
            self._config = config
            if config.mock_mode:
                self._psu = MockPsu(
                    limits=config.limits,
                    expected_idn_contains=config.expected_idn_contains,
                    expected_model=config.expected_model,
                    expected_serial=config.expected_serial,
                    station_id=config.station_id or "MOCK_STATION",
                    fault_config=config.mock_faults,
                )
                idn = self._psu.connect()
            else:
                self._psu = EaPs9000T(
                    port=config.port,
                    baudrate=config.baudrate,
                    timeout=config.timeout,
                    write_timeout=config.write_timeout,
                    keyword=config.keyword,
                    retry_cnt=config.retry_cnt,
                    retry_delay=config.retry_delay,
                    limits=config.limits,
                    auto_connect=True,
                    auto_remote=config.auto_remote,
                    verify_remote=config.verify_remote,
                    safe_close=config.safe_close,
                    output_off_on_close=config.output_off_on_close,
                    production_mode=config.production_mode,
                    expected_idn_contains=config.expected_idn_contains or None,
                    expected_model=config.expected_model,
                    expected_serial=config.expected_serial,
                    station_id=config.station_id,
                    measurement_array_supported=config.measurement_array_supported,
                )
                idn = getattr(self._psu, "idn", "") or ""
            logger.info("Connected PSU: %s", idn)
            return idn

    def disconnect(self, suppress_errors: bool = False) -> None:
        with self._lock:
            if self._psu is None:
                return
            try:
                self._psu.close(output_off=True, suppress_errors=suppress_errors)
            finally:
                self._psu = None
                self.output_state_unknown = False

    def _require_psu(self):
        if self._psu is None or not self.is_connected():
            raise NotConnectedError("PSU is not connected")
        return self._psu

    def is_connected(self) -> bool:
        with self._lock:
            return self._psu is not None and bool(getattr(self._psu, "is_connected", False))

    def ping(self) -> bool:
        with self._lock:
            if self._psu is None:
                return False
            return bool(self._psu.ping())

    def reconnect_safely(self) -> str:
        with self._lock:
            psu = self._require_psu()
            idn = psu.reconnect_safely(force_output_off=True, verify_output_off=False)
            self.output_state_unknown = bool(getattr(psu, "output_state_unknown", False))
            return idn

    def set_voltage(self, voltage_v: float):
        with self._lock:
            self._require_psu().set_voltage(voltage_v)
            self._last_voltage = float(voltage_v)

    def set_current(self, current_a: float):
        with self._lock:
            self._require_psu().set_current(current_a)
            self._last_current = float(current_a)

    def set_power(self, power_w: float):
        with self._lock:
            self._require_psu().set_power(power_w)
            self._last_power = float(power_w)

    def get_voltage_setpoint(self) -> float:
        with self._lock:
            value = self._require_psu().get_voltage_setpoint()
            self._last_voltage = float(value)
            return float(value)

    def get_current_setpoint(self) -> float:
        with self._lock:
            value = self._require_psu().get_current_setpoint()
            self._last_current = float(value)
            return float(value)

    def get_power_setpoint(self) -> float:
        with self._lock:
            value = self._require_psu().get_power_setpoint()
            self._last_power = float(value)
            return float(value)

    def set_ovp(self, ovp_v: float):
        with self._lock:
            self._require_psu().set_ovp(ovp_v)
            self._last_ovp = float(ovp_v)

    def set_ocp(self, ocp_a: float):
        with self._lock:
            self._require_psu().set_ocp(ocp_a)
            self._last_ocp = float(ocp_a)

    def set_opp(self, opp_w: float):
        with self._lock:
            self._require_psu().set_opp(opp_w)
            self._last_opp = float(opp_w)

    def output_on(self, verify: bool = True):
        with self._lock:
            psu = self._require_psu()
            psu.output_on(verify=verify)
            self.output_state_unknown = bool(getattr(psu, "output_state_unknown", False))

    def output_off(self, verify: bool = True):
        with self._lock:
            psu = self._require_psu()
            psu.output_off(verify=verify)
            self.output_state_unknown = bool(getattr(psu, "output_state_unknown", False))

    def emergency_off(self):
        # This is still serialized, but is exposed as a distinct method for priority queue upgrades later.
        logger.warning("Emergency OFF requested")
        self.output_off(verify=True)

    def is_output_on(self) -> bool:
        with self._lock:
            state = bool(self._require_psu().is_output_on())
            self.output_state_unknown = False
            return state

    def measure(self, fast: bool = False) -> dict:
        with self._lock:
            psu = self._require_psu()
            return psu.measure_all_fast() if fast else psu.measure_all()

    def check_health(self) -> dict:
        with self._lock:
            psu = self._require_psu()
            health = psu.check_device_health()
            self.output_state_unknown = bool(health.get("output_state_unknown", False))
            return health

    def check_errors(self):
        with self._lock:
            return self._require_psu().check_errors()

    def get_errors(self) -> str:
        with self._lock:
            return self._require_psu().get_errors()

    def read_status_byte(self) -> int:
        with self._lock:
            return int(self._require_psu().read_status_byte())

    def safe_output_on_from_cached_values(self, verify: bool = True) -> None:
        """Safe output enable sequence based on last GUI/controller values."""
        with self._lock:
            psu = self._require_psu()
            if None in (self._last_voltage, self._last_current, self._last_ovp, self._last_ocp):
                raise ValueError("Voltage, current, OVP and OCP must be set before safe output ON")
            if hasattr(psu, "enable_output_safely"):
                psu.enable_output_safely(
                    voltage=self._last_voltage,
                    current=self._last_current,
                    power=self._last_power,
                    ovp=self._last_ovp,
                    ocp=self._last_ocp,
                    opp=self._last_opp,
                    verify=verify,
                )
            else:
                self.set_ovp(self._last_ovp)  # type: ignore[arg-type]
                self.set_ocp(self._last_ocp)  # type: ignore[arg-type]
                if self._last_opp is not None:
                    self.set_opp(self._last_opp)
                if self._last_power is not None:
                    self.set_power(self._last_power)
                self.set_voltage(self._last_voltage)  # type: ignore[arg-type]
                self.set_current(self._last_current)  # type: ignore[arg-type]
                self.output_on(verify=verify)
            self.output_state_unknown = bool(getattr(psu, "output_state_unknown", False))
