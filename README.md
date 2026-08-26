# EA-PS-9000T

Python serial-SCPI control helpers for EA Elektro-Automatik PS 9000 T programmable DC power supplies.

> Status: this project is an early-stage driver.  Validate commands, limits, and output state on a safely configured instrument before using it in unattended or safety-critical work.

## Installation

Install directly from GitHub:

```bash
python -m pip install "git+https://github.com/ami3go/EA-PS-9000T.git"
```

Or, for a local checkout:

```bash
git clone https://github.com/ami3go/EA-PS-9000T.git
cd EA-PS-9000T
python -m pip install .
```

The package installs [pyserial](https://pyserial.readthedocs.io/) automatically. Python 3.9 or newer is required.

## Quick start

Connect the supply over USB, ensure it appears as a serial port with a description that includes `PS 9000 T`, then:

```python
from EAPS9000T import EaPs9000T

supply = EaPs9000T()
try:
    supply.set_current(2.0)
    supply.set_voltage(12.0)
    supply.output_on()
    print(supply.get_errors())
finally:
    supply.output_off()
    supply.close()
```

`EaPs9000T()` automatically searches for the USB serial port and switches the instrument to remote mode. See the `Examples/` directory for more command-generation examples.

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest
python -m build
```

The tests are offline and do not communicate with a power supply. Distribution artifacts are created in `dist/`.

## License

Released under the [MIT License](LICENSE).
