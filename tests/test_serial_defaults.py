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


def test_output_off_recovers_a_failed_serial_transport_once() -> None:
    supply = driver.EaPs9000T(auto_connect=False, limits=driver.PowerSupplyLimits())
    calls: list[str] = []

    def send(command: str, **_kwargs: object) -> None:
        calls.append(command)
        if len(calls) == 1:
            raise driver.CommunicationError("stale serial handle")

    def reconnect_safely(**kwargs: object) -> str:
        assert kwargs == {"force_output_off": False}
        calls.append("reconnect")
        return "EA,PS 9000 T"

    supply.send = send  # type: ignore[method-assign]
    supply.reconnect_safely = reconnect_safely  # type: ignore[method-assign]

    supply.output_off()

    assert calls == ["OUTP OFF", "reconnect", "OUTP OFF"]
    assert supply.output_state_unknown is True
