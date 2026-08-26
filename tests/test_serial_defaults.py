"""Offline regression tests for serial transport defaults."""

import EAPS9000T.EAPS9000T_class as driver


def test_write_timeout_defaults_to_pyserial_blocking_mode() -> None:
    supply = driver.EaPs9000T(auto_connect=False, limits=driver.PowerSupplyLimits())

    assert supply.write_timeout is None


def test_explicit_write_timeout_is_preserved() -> None:
    supply = driver.EaPs9000T(
        auto_connect=False,
        limits=driver.PowerSupplyLimits(),
        write_timeout=2.5,
    )

    assert supply.write_timeout == 2.5
