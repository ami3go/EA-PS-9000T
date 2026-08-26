# EA PS 9000 T GUI

Modern Material-inspired PySide6 GUI for controlling an EA Elektro-Automatik PS 9000 T programmable DC power supply.

> Safety: this software can control hazardous voltage/current. Start in mock mode, configure exact model limits, and test with conservative values before using real hardware.

## Features

- Mock mode for testing without hardware.
- Serial connection to `EaPs9000T` driver.
- Manual voltage/current/power setpoints.
- OVP/OCP/OPP protection setup.
- Persistent output-control panel with emergency off.
- Live measurements.
- CSV voltage-profile loading, validation, preview, and execution.
- Measurement and application logging.
- Core tests that do not require hardware.

## Install

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The application starts with **Use Mock PSU** enabled by default.

## CSV profile format

Required columns:

```text
time_s, voltage_v
```

Optional columns:

```text
current_a, power_w, ovp_v, ocp_a, opp_w, output, ramp, comment
```

`output` may be `on`, `off`, or `keep`.
`ramp` may be `step` or `linear`.

See `examples/example_voltage_profile.csv`.

## Tests

```bash
pytest
```

## PyInstaller

Debug build:

```bash
pyinstaller --noconfirm --onedir main.py
```

One-file build:

```bash
pyinstaller --noconfirm --onefile --windowed main.py
```

The `--onedir` build is easier to troubleshoot.
