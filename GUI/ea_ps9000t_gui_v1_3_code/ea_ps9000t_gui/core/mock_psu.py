from __future__ import annotations

import random
import time
from dataclasses import dataclass
from typing import Optional

from EAPS9000T_class import (
    CommunicationError,
    DeviceIdentityError,
    InstrumentCommandError,
    PowerSupplyLimits,
    RangeError,
    RemoteControlError,
    validate_range,
)


@dataclass
class MockFaultConfig:
    communication_timeout: bool = False
    wrong_idn: bool = False
    output_on_verify_failure: bool = False
    output_off_verify_failure: bool = False
    scpi_error_queue_not_empty: bool = False
    slow_measurement_response_s: float = 0.0
    serial_disconnect_during_profile: bool = False
    remote_lock_failure: bool = False
    output_state_unknown: bool = False


class MockPsu:
    """Simulation backend with the same high-level API shape as EaPs9000T."""

    def __init__(
        self,
        limits: Optional[PowerSupplyLimits] = None,
        expected_idn_contains=None,
        expected_model: Optional[str] = None,
        expected_serial: Optional[str] = None,
        station_id: str = "MOCK_STATION",
        fault_config: Optional[MockFaultConfig] = None,
        **_: object,
    ):
        self.limits = limits or PowerSupplyLimits()
        self.expected_idn_contains = expected_idn_contains or []
        self.expected_model = expected_model
        self.expected_serial = expected_serial
        self.station_id = station_id
        self.fault_config = fault_config or MockFaultConfig()
        self.connected = False
        self.remote = False
        self.output = False
        self.output_state_unknown = False
        self.idn = "MOCK,EA-PS9000T,000000,FW:SIM"
        self.voltage_v = 0.0
        self.current_a = 0.0
        self.power_w = 0.0
        self.ovp_v = self.limits.ovp_max
        self.ocp_a = self.limits.ocp_max
        self.opp_w = self.limits.opp_max

    @property
    def is_connected(self) -> bool:
        return self.connected

    def _require_connected(self) -> None:
        if not self.connected:
            raise CommunicationError("Mock PSU is not connected")
        if self.fault_config.communication_timeout:
            raise CommunicationError("Mock communication timeout")

    def connect(self, *_, **__) -> str:
        if self.fault_config.communication_timeout:
            raise CommunicationError("Mock connection timeout")
        self.connected = True
        self.idn = "WRONG,DEVICE,123,FW:SIM" if self.fault_config.wrong_idn else "MOCK,EA-PS9000T,000000,FW:SIM"
        if self.expected_idn_contains:
            for part in self.expected_idn_contains:
                if part and part.lower() not in self.idn.lower():
                    raise DeviceIdentityError(f"Mock IDN {self.idn!r} does not contain {part!r}")
        return self.idn

    def close(self, output_off: bool = True, **_: object) -> None:
        if output_off and self.connected:
            self.output_off(verify=False)
        self.connected = False
        self.remote = False

    def reconnect_safely(self, *_, **__) -> str:
        self.close(output_off=True)
        return self.connect()

    def ping(self) -> bool:
        try:
            self._require_connected()
            return True
        except Exception:
            return False

    def remote_on(self, verify: bool = False) -> None:
        self._require_connected()
        if self.fault_config.remote_lock_failure:
            raise RemoteControlError("Mock remote lock failure")
        self.remote = True

    def remote_off(self) -> None:
        self._require_connected()
        self.remote = False

    def get_remote_owner(self) -> str:
        self._require_connected()
        return "REMOTE" if self.remote else "LOCAL"

    def set_voltage(self, val: float) -> None:
        self._require_connected()
        self.voltage_v = validate_range(val, self.limits.voltage_min, self.limits.voltage_max, "voltage")

    def get_voltage_setpoint(self) -> float:
        self._require_connected()
        return self.voltage_v

    def set_current(self, val: float) -> None:
        self._require_connected()
        self.current_a = validate_range(val, self.limits.current_min, self.limits.current_max, "current")

    def get_current_setpoint(self) -> float:
        self._require_connected()
        return self.current_a

    def set_power(self, val: float) -> None:
        self._require_connected()
        self.power_w = validate_range(val, self.limits.power_min, self.limits.power_max, "power")

    def get_power_setpoint(self) -> float:
        self._require_connected()
        return self.power_w

    def set_ovp(self, val: float) -> None:
        self._require_connected()
        self.ovp_v = validate_range(val, self.limits.ovp_min, self.limits.ovp_max, "OVP")

    def set_ocp(self, val: float) -> None:
        self._require_connected()
        self.ocp_a = validate_range(val, self.limits.ocp_min, self.limits.ocp_max, "OCP")

    def set_opp(self, val: float) -> None:
        self._require_connected()
        self.opp_w = validate_range(val, self.limits.opp_min, self.limits.opp_max, "OPP")

    def output_on(self, verify: bool = False) -> None:
        self._require_connected()
        self.output = not self.fault_config.output_on_verify_failure
        self.output_state_unknown = self.fault_config.output_state_unknown
        if verify and not self.output:
            raise InstrumentCommandError("Mock output ON verification failure")

    def output_off(self, verify: bool = False) -> None:
        self._require_connected()
        if self.fault_config.output_off_verify_failure:
            self.output = True
        else:
            self.output = False
        self.output_state_unknown = self.fault_config.output_state_unknown
        if verify and self.output:
            raise InstrumentCommandError("Mock output OFF verification failure")

    def is_output_on(self) -> bool:
        self._require_connected()
        if self.output_state_unknown:
            raise InstrumentCommandError("Mock output state unknown")
        return self.output

    def measure_all(self) -> dict[str, float]:
        self._require_connected()
        if self.fault_config.slow_measurement_response_s > 0:
            time.sleep(self.fault_config.slow_measurement_response_s)
        voltage = self.voltage_v if self.output else 0.0
        current = min(self.current_a, self.power_w / max(voltage, 1e-9)) if self.output and self.power_w > 0 else 0.0
        return {
            "voltage_v": voltage + random.uniform(-0.005, 0.005),
            "current_a": current + random.uniform(-0.001, 0.001),
            "power_w": max(0.0, voltage * current + random.uniform(-0.05, 0.05)),
        }

    def measure_all_fast(self, *_, **__) -> dict[str, float]:
        return self.measure_all()

    def get_errors(self) -> str:
        self._require_connected()
        return '100,"Mock SCPI error"' if self.fault_config.scpi_error_queue_not_empty else '0,"No error"'

    def check_errors(self) -> None:
        if self.fault_config.scpi_error_queue_not_empty:
            raise InstrumentCommandError(self.get_errors())

    def clear_status(self) -> None:
        self.fault_config.scpi_error_queue_not_empty = False

    def read_status_byte(self) -> int:
        self._require_connected()
        return 0

    def check_device_health(self, expected_output=None, require_remote: bool = False) -> dict:
        self.check_errors()
        if require_remote and not self.remote:
            raise RemoteControlError("Mock remote is not active")
        if expected_output is not None and self.output != expected_output:
            raise InstrumentCommandError(f"Mock unexpected output state: {self.output}")
        return {
            "status_byte": 0,
            "remote_owner": self.get_remote_owner(),
            "output_on": self.output,
            "output_state_unknown": self.output_state_unknown,
        }

    def verify_setpoints(self, voltage=None, current=None, power=None, tolerance: float = 1e-6) -> None:
        if voltage is not None and abs(float(voltage) - self.voltage_v) > tolerance:
            raise InstrumentCommandError("Mock voltage setpoint mismatch")
        if current is not None and abs(float(current) - self.current_a) > tolerance:
            raise InstrumentCommandError("Mock current setpoint mismatch")
        if power is not None and abs(float(power) - self.power_w) > tolerance:
            raise InstrumentCommandError("Mock power setpoint mismatch")

    def enable_output_safely(self, *, voltage, current, ovp, ocp, opp=None, power=None, verify=True, tolerance=1e-6):
        self.remote_on(verify=True)
        self.clear_status()
        self.set_ovp(ovp)
        self.set_ocp(ocp)
        if opp is not None:
            self.set_opp(opp)
        if power is not None:
            self.set_power(power)
        self.set_voltage(voltage)
        self.set_current(current)
        if verify:
            self.verify_setpoints(voltage=voltage, current=current, power=power, tolerance=tolerance)
        self.output_on(verify=True)
