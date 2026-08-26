# EA PS 9000 T Production SCPI Driver

This document describes how to use `EAPS9000T_class.py`, what was changed compared with the original prototype, and how to use the driver safely in a long-running industrial/lab automation environment.

The driver is designed for EA Elektro-Automatik PS 9000 T power supplies controlled over serial SCPI. It keeps the original public API where practical, but adds stricter safety, validation, logging, and production-mode behavior.

> Important: this software driver is not a replacement for external safety hardware. For industrial plant use, always use physical emergency stop, interlocks, fuses, contactors, DUT protection, thermal protection, and a validated safety PLC or equivalent safety chain where required.

---

## Files

Recommended files:

```text
EAPS9000T_class.py          # Main driver
test_EAPS9000T_class.py     # Basic fake-serial smoke tests
EA_PS9000T_DRIVER_README.md        # This document
```

---

## Installation

The driver uses `pyserial`. `pyvisa` is not required.

```bash
pip install pyserial
```

Optional tools for development/testing:

```bash
pip install pytest mypy ruff
```

The driver can be compiled/tested with:

```bash
python -m py_compile EAPS9000T_class.py
python -m unittest -q test_EAPS9000T_class.py
```

---

## Import

```python
from EAPS9000T_class import EaPs9000T, PowerSupplyLimits
```

---

## Backward-compatible basic usage

This keeps the old style from the prototype:

```python
from EAPS9000T_class import EaPs9000T

ps = EaPs9000T(port="COM8")
ps.set_voltage(10)
ps.set_current(1)
ps.output_on()

# Test code here

ps.output_off()
ps.close()
```

This mode is convenient for manual bench work, but it is not the recommended mode for industrial unattended use because it can use default limits if no model-specific limits are provided.

---

## Recommended production usage

For plant use, always pass explicit model limits and enable `production_mode=True`.

```python
import logging
from EAPS9000T_class import EaPs9000T, PowerSupplyLimits

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

limits = PowerSupplyLimits(
    voltage_min=0,
    voltage_max=80,
    current_min=0,
    current_max=40,
    power_min=0,
    power_max=1500,
    ovp_min=0,
    ovp_max=88,
    ocp_min=0,
    ocp_max=44,
    opp_min=0,
    opp_max=1650,
)

with EaPs9000T(
    port="COM8",
    limits=limits,
    production_mode=True,
    allow_default_limits=False,
    expected_idn_contains="EA",
    expected_model="PS 9000",
    station_id="EOL_TESTER_03_PSU_1",
    auto_remote=True,
    verify_remote=True,
    raise_on_close_error=True,
) as ps:
    ps.enable_output_safely(
        voltage=24.0,
        current=2.0,
        ovp=30.0,
        ocp=2.5,
        opp=100.0,
        verify=True,
    )

    values = ps.measure_all()
    print(values)

    ps.output_off(verify=True)
```

Production mode changes several behaviors:

- explicit limits are required when `allow_default_limits=False`;
- remote mode is verified by default during connection;
- set commands call `check_errors()` after write;
- `output_on()` and `output_off()` verify state;
- `close()` becomes stricter and reports safety-state errors;
- output-off-on-close is verified by default.

---

## Safest way to enable output

Use `enable_output_safely()` instead of manually calling multiple set commands.

```python
ps.enable_output_safely(
    voltage=12.0,
    current=1.0,
    ovp=15.0,
    ocp=1.5,
    opp=30.0,
    verify=True,
)
```

The sequence is deliberate:

1. acquire and verify remote lock;
2. clear old SCPI status;
3. program protection limits first: OVP, OCP, optionally OPP;
4. program voltage/current/power setpoints;
5. read back setpoints;
6. check SCPI errors/status;
7. enable output;
8. verify output state.

This is safer than setting voltage and turning output on directly.

---

## Measuring output

Sequential measurement:

```python
values = ps.measure_all()
print(values["voltage_v"])
print(values["current_a"])
print(values["power_w"])
```

Individual measurement:

```python
voltage = ps.measure_voltage()
current = ps.measure_current()
power = ps.measure_power()
```

Fast array measurement is disabled by default to avoid sending unsupported SCPI commands on firmware that does not support `MEAS:ARR?`.

Enable it only after confirming your PSU firmware supports it:

```python
ps = EaPs9000T(
    port="COM8",
    limits=limits,
    measurement_array_supported=True,
)

values = ps.measure_all_fast()
```

If `measurement_array_supported=False`, `measure_all_fast()` automatically uses the safe three-query `measure_all()` path.

---

## Heartbeat / watchdog usage

The driver includes `ping()` for supervisor integration. It returns `False` instead of raising on communication failure.

```python
if not ps.ping():
    # Escalate to your plant supervisor, stop test, or call reconnect_safely()
    print("PSU communication lost")
```

Because the driver now uses an internal `threading.RLock`, watchdog calls cannot interleave serial bytes with normal test commands.

Example watchdog loop:

```python
import time

while test_is_running:
    if not ps.ping():
        ps.output_state_unknown = True
        raise RuntimeError("Power supply heartbeat failed")
    time.sleep(5)
```

For real plant equipment, heartbeat failure should normally move the station into a safe state and alert the operator. Do not assume the PSU output is off after communication loss unless verified by hardware or a separate safety circuit.

---

## Reconnect after link loss

The driver provides a best-effort reconnect helper:

```python
try:
    ps.reconnect_safely(force_output_off=True, verify_output_off=True)
except Exception:
    # Treat as serious station fault.
    # The output state may be unknown.
    raise
```

Important behavior:

- if communication is still possible, it tries to switch output off before reconnecting;
- if output state cannot be verified, `output_state_unknown` may be set;
- plant code should treat unknown output state as an alarm condition.

---

## Safe shutdown

Recommended:

```python
ps.output_off(verify=True)
ps.close(output_off=True, remote_off=True, verify_output_off=True)
```

Using the context manager is preferred:

```python
with EaPs9000T(port="COM8", limits=limits, production_mode=True) as ps:
    ps.enable_output_safely(voltage=12, current=1, ovp=15, ocp=1.5)
    # test code
# close() is called automatically here
```

In production mode, close errors are treated more strictly. If the driver cannot verify output-off during close, the caller should stop the station and alert the operator.

---

## Exception handling pattern

Example:

```python
from EAPS9000T_class import (
    EaPs9000T,
    PowerSupplyLimits,
    EAPSError,
    CommunicationError,
    SafetyStateError,
    InstrumentAlarmError,
)

try:
    with EaPs9000T(port="COM8", limits=limits, production_mode=True) as ps:
        ps.enable_output_safely(voltage=24, current=2, ovp=30, ocp=2.5)
        result = ps.measure_all()
        ps.output_off(verify=True)

except SafetyStateError as exc:
    # Output may still be on or state may be unknown.
    # Stop station, trigger external safety path if required.
    print(f"SAFETY ERROR: {exc}")
    raise

except CommunicationError as exc:
    # USB/serial/timeout failure.
    print(f"COMMUNICATION ERROR: {exc}")
    raise

except InstrumentAlarmError as exc:
    # Status or output state inconsistent with expectation.
    print(f"INSTRUMENT ALARM: {exc}")
    raise

except EAPSError as exc:
    # Other driver/instrument error.
    print(f"EA DRIVER ERROR: {exc}")
    raise
```

---

## Identity checking

Do not rely only on automatic COM-port discovery in a plant. Use fixed port mapping and identity checks.

```python
ps = EaPs9000T(
    port="COM8",
    limits=limits,
    production_mode=True,
    expected_idn_contains=["EA", "PS 9000"],
    expected_serial="123456789",
)
```

Available identity checks:

```python
expected_idn_contains="EA"
expected_idn_contains=["EA", "PS 9000"]
expected_model="PS 9000"
expected_serial="123456789"
```

The driver checks these strings against the `*IDN?` response and raises `DeviceIdentityError` if the connected instrument is not the expected plant device.

---

## Logging

Enable logging in your application:

```python
import logging

logging.basicConfig(
    filename="psu_driver.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
```

Use `station_id` to make logs easier to read in multi-station systems:

```python
ps = EaPs9000T(
    port="COM8",
    limits=limits,
    station_id="BMS_EOL_STATION_01_PSU_MAIN",
)
```

Log messages include the station ID in important connection and fallback paths.

---

## Command builder compatibility

The old command-builder style is still available:

```python
from EAPS9000T_class import storage

cmd = storage()

print(cmd.source.voltage.req())       # SOUR:VOLTage?
print(cmd.source.voltage.val(10))     # SOUR:VOLTage 10V
print(cmd.source.current.ocp.val(5))  # SOUR:CURrent:PROTection 5
print(cmd.source.current.ovc.val(5))  # old compatibility alias
print(cmd.output.on())                # OUTP ON
```

For production application code, prefer the high-level methods on `EaPs9000T` because they validate ranges and can check instrument errors.

Recommended:

```python
ps.set_voltage(10)
```

Avoid direct low-level send unless necessary:

```python
ps.send(cmd.source.voltage.val(10))
```

---

## What was changed compared with the original prototype

### Communication reliability

- `send()` no longer sends the same command `retry_cnt` times after a successful write.
- `query()` treats empty replies as timeouts.
- Read/write failures raise exceptions instead of only printing text.
- The serial port is checked before every operation.
- Stale input bytes are flushed after opening the port.
- Retry count and retry delay are configurable.
- `reset()` is sent without blind retry because it is not safe to duplicate some non-idempotent commands.

### Thread safety

- A `threading.RLock` now serializes all serial I/O.
- This prevents watchdog `ping()` calls from corrupting normal SCPI request/response order.

### Safety behavior

- `PowerSupplyLimits` defines allowed voltage/current/power/protection ranges.
- High-level setters reject out-of-range values with `RangeError`.
- `output_on(verify=True)` and `output_off(verify=True)` wait for relay settling and read back output state.
- `close()` can switch output off and verify it before releasing remote control.
- `production_mode=True` enables stricter checking.
- `enable_output_safely()` adds a correct plant-style output-enable sequence.
- `output_state_unknown` is available for supervisor logic after reconnect/link-loss scenarios.

### Identity and configuration validation

- Optional identity checks were added using the `*IDN?` response.
- Production mode can require explicit limits by setting `allow_default_limits=False`.
- A `ConfigurationError` is raised if production-mode configuration is unsafe or incomplete.

### Diagnostics

- Custom exceptions were added:
  - `EAPSError`
  - `InstrumentNotFoundError`
  - `DependencyError`
  - `CommunicationError`
  - `CommandTimeoutError`
  - `RemoteControlError`
  - `InstrumentCommandError`
  - `RangeError`
  - `DriverClosedError`
  - `ConfigurationError`
  - `DeviceIdentityError`
  - `SafetyStateError`
  - `InstrumentAlarmError`
- Logging replaces print-only error reporting.
- `check_errors()` parses the numeric SCPI error code.
- `check_device_health()` performs generic health checks.

### Measurement improvements

- Added:
  - `measure_voltage()`
  - `measure_current()`
  - `measure_power()`
  - `measure_all()`
  - `measure_all_fast()`
- `measure_all_fast()` only sends `MEAS:ARR?` when explicitly enabled.

### Backward compatibility

Existing basic code should still work:

```python
ps = EaPs9000T()
ps.set_voltage(10)
ps.set_current(1)
ps.output_on()
ps.output_off()
ps.close()
```

The old `set_ovc()` name is kept as a deprecated alias for `set_ocp()`.

---

## Important limitations still remaining

The driver is now much stronger, but several items still require your exact hardware/manual validation before final plant deployment.

### 1. Alarm/status register decoding

`check_device_health()` currently performs generic checks:

- SCPI error queue;
- status byte;
- optional remote lock;
- optional output state.

It does not yet decode every EA-specific alarm bit such as OVP, OCP, OPP, over-temperature, mains fault, or device alarm. Add this once the exact PS 9000 T status-register mapping for your firmware is confirmed.

### 2. External safety still required

Software cannot guarantee safe energy removal if:

- USB/serial link is lost;
- PSU firmware hangs;
- output relay welds closed;
- Windows freezes;
- Python process crashes;
- DUT wiring fails.

Use external safety hardware for real plant equipment.

### 3. Model limits must be verified

The default limits are inherited from the original prototype assumptions. They may not match your exact EA model. In production, always pass explicit `PowerSupplyLimits`.

### 4. Real-hardware validation required

Before production deployment, test with the actual PSU and DUT/load setup:

- connection/disconnection during output-on;
- PSU power-cycle during test;
- remote lock loss;
- emergency stop activation;
- OVP/OCP/OPP trips;
- communication timeout;
- Windows sleep/reboot/USB reset;
- long-run 24/7 soak test.

---

## Recommended plant integration pattern

Use the PSU driver as one layer in a larger equipment-control architecture:

```text
Test Sequence Manager
        |
        v
Safety Supervisor / Interlock Monitor
        |
        v
Instrument Driver Layer
        |
        v
EA PS 9000 T Power Supply
```

Recommended rules:

1. The test sequence should never call raw SCPI directly.
2. All output enabling should go through `enable_output_safely()`.
3. The supervisor should call `ping()` periodically.
4. Communication failure should stop the test and mark output state unknown.
5. External safety hardware should be able to remove power independently of Python.
6. Every test step should log setpoints, measured values, output state, and errors.

---

## Example: complete industrial-style test step

```python
import logging
import time
from EAPS9000T_class import EaPs9000T, PowerSupplyLimits, EAPSError

logging.basicConfig(level=logging.INFO)

limits = PowerSupplyLimits(
    voltage_max=80,
    current_max=40,
    power_max=1500,
    ovp_max=88,
    ocp_max=44,
    opp_max=1650,
)

try:
    with EaPs9000T(
        port="COM8",
        limits=limits,
        production_mode=True,
        allow_default_limits=False,
        expected_idn_contains=["EA", "PS 9000"],
        station_id="BMS_EOL_STATION_01_PSU",
        auto_remote=True,
        verify_remote=True,
    ) as ps:
        ps.enable_output_safely(
            voltage=24.0,
            current=2.0,
            ovp=30.0,
            ocp=2.5,
            opp=100.0,
            verify=True,
        )

        time.sleep(1.0)
        measurement = ps.measure_all()
        ps.check_device_health(expected_output=True, require_remote=True)
        print(measurement)

        ps.output_off(verify=True)
        ps.check_device_health(expected_output=False, require_remote=True)

except EAPSError as exc:
    # In real plant code, also notify the station supervisor / PLC / operator UI.
    logging.exception("Power supply test step failed: %s", exc)
    raise
```

---

## Example: bench mode with manual COM discovery

```python
from EAPS9000T_class import EaPs9000T, list_serial_ports

print(list_serial_ports())

with EaPs9000T(keyword="PS 9000 T", production_mode=False) as ps:
    print(ps.idn)
    ps.set_voltage(5)
    ps.set_current(0.5)
    ps.output_on(verify=True)
    print(ps.measure_all())
    ps.output_off(verify=True)
```

---

## Example: using old API but safer close

```python
ps = EaPs9000T(port="COM8", limits=limits)
try:
    ps.set_ovp(30)
    ps.set_ocp(2.5)
    ps.set_voltage(24)
    ps.set_current(2)
    ps.output_on(verify=True)
finally:
    ps.close(output_off=True, remote_off=True, verify_output_off=True)
```

---

## Recommended next improvements

For final industrial deployment, consider adding:

1. Exact EA alarm/status-bit decoder for your PSU firmware.
2. Integration tests with real hardware and programmable load.
3. Continuous 24/7 soak test with periodic measurements and reconnect simulation.
4. Station-level log format with test ID, DUT serial, operator, and step number.
5. Safety PLC or hardware interlock interface.
6. Driver package structure instead of a single file.
7. CI checks: `py_compile`, `unittest`, `ruff`, `mypy`.
8. Version number inside the driver, for example `__version__ = "3.0.0"`.

---

## Quick checklist before energising DUT

Before calling `output_on()` or `enable_output_safely()`:

- [ ] Correct PSU model connected.
- [ ] Correct COM port selected.
- [ ] `*IDN?` identity checked.
- [ ] Explicit `PowerSupplyLimits` configured.
- [ ] OVP lower than DUT damage threshold.
- [ ] OCP lower than DUT/wiring safe current.
- [ ] OPP configured if relevant.
- [ ] Output state initially off.
- [ ] Emergency stop and interlock tested.
- [ ] Logging enabled.
- [ ] Test sequence has exception handling.
- [ ] Operator knows recovery procedure for unknown output state.

---

## Summary

`EAPS9000T_class.py` keeps the original convenient API but adds the missing production foundations: strict limits, identity checks, thread-safe serial access, safer output-enable/shutdown flow, watchdog support, reconnection handling, and structured exceptions.

Use simple mode for bench experiments. Use `production_mode=True`, explicit `PowerSupplyLimits`, identity validation, verified output control, and external safety hardware for industrial plant operation.
