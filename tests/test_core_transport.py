"""Tests for the scpi-driver-core-backed transport wiring.

Unlike test_commands.py / test_serial_defaults.py, these drive the real
SerialTransport/ScpiClient code path (not a monkeypatched EaPs9000T method),
against a fake pyserial backend swapped in under
scpi_driver_core.transport.serial. This is what actually exercises the
transport/framing/parsing migration end to end.
"""

from __future__ import annotations

import pytest

import scpi_driver_core.transport.serial as serial_module
from EAPS9000T.EAPS9000T_class import EaPs9000T, PowerSupplyLimits


class FakeSerial:
    """Minimal pyserial-like test double, good enough for SerialTransport."""

    instances: list["FakeSerial"] = []

    def __init__(self, **settings):
        self.settings = settings
        self.timeout = settings["timeout"]
        self.write_timeout = settings["write_timeout"]
        self.dtr = True
        self.rts = True
        self.inbound = bytearray()
        self.written = bytearray()
        self.fail_write = False
        FakeSerial.instances.append(self)

    @property
    def in_waiting(self) -> int:
        return len(self.inbound)

    def write(self, data: bytes) -> int:
        if self.fail_write:
            raise OSError("simulated write failure")
        self.written.extend(data)
        return len(data)

    def read(self, size: int) -> bytes:
        count = min(size, len(self.inbound))
        data = bytes(self.inbound[:count])
        del self.inbound[:count]
        return data

    def read_until(self, expected: bytes, size: int) -> bytes:
        end = self.inbound.find(expected)
        count = min(size, len(self.inbound) if end < 0 else end + len(expected))
        return self.read(count)

    def reset_input_buffer(self) -> None:
        self.inbound.clear()

    def reset_output_buffer(self) -> None:
        pass

    def close(self) -> None:
        pass

    def queue_reply(self, text: str) -> None:
        self.inbound.extend(text.encode("ascii"))


@pytest.fixture
def fake_backend(monkeypatch: pytest.MonkeyPatch):
    from types import SimpleNamespace

    FakeSerial.instances.clear()
    monkeypatch.setattr(
        serial_module, "_load_serial", lambda: SimpleNamespace(Serial=FakeSerial)
    )
    return FakeSerial


def _auto_reply(
    fake: FakeSerial,
    idn: str = "EA,PS 9000 T,FAKE123,1.0,FAKE",
    replies: dict[str, str] | None = None,
) -> None:
    """Queue a canned reply for whatever the driver writes next.

    Replies must be queued on write, not beforehand: the driver flushes the
    input buffer immediately before every query attempt (matching the
    original driver's stale-byte handling), so anything pre-queued would be
    discarded before it could be read back.
    """
    original_write = FakeSerial.write
    overrides = replies or {}

    def write_and_reply(self: FakeSerial, data: bytes) -> int:
        text = data.decode("ascii").strip()
        if text in overrides:
            self.queue_reply(overrides[text] + "\n")
        elif text == "*IDN?":
            self.queue_reply(idn + "\n")
        elif text == "SYST:ERR:ALL?":
            self.queue_reply('0,"No error"\n')
        elif text.endswith("?"):
            self.queue_reply("1\n")
        return original_write(self, data)

    FakeSerial.write = write_and_reply  # type: ignore[method-assign]


def test_connect_identifies_over_fake_serial(fake_backend) -> None:
    _auto_reply(fake_backend)
    ps = EaPs9000T(port="FAKE", auto_connect=False, limits=PowerSupplyLimits(), auto_remote=False)

    idn = ps.connect(auto_remote=False)

    assert idn == "EA,PS 9000 T,FAKE123,1.0,FAKE"
    assert ps.is_connected
    ps.close(output_off=False, remote_off=False)
    assert not ps.is_connected


def test_write_timeout_none_reaches_the_fake_serial_backend(fake_backend) -> None:
    _auto_reply(fake_backend)
    ps = EaPs9000T(
        port="FAKE", auto_connect=False, limits=PowerSupplyLimits(), auto_remote=False,
        write_timeout=None,
    )

    ps.connect(auto_remote=False)

    assert fake_backend.instances[-1].settings["write_timeout"] is None
    ps.close(output_off=False, remote_off=False)


def test_check_errors_uses_syst_err_all_wire_command(fake_backend) -> None:
    """Regression guard: the error-queue check must stay on SYST:ERR:ALL?,
    not switch to scpi-driver-core's single-pop SYST:ERR? convention."""
    _auto_reply(fake_backend)
    ps = EaPs9000T(port="FAKE", auto_connect=False, limits=PowerSupplyLimits(), auto_remote=False)
    ps.connect(auto_remote=False)

    ps.check_errors()

    sent = bytes(fake_backend.instances[-1].written).decode("ascii")
    assert "SYST:ERR:ALL?" in sent
    ps.close(output_off=False, remote_off=False)


def test_query_strips_terminator_and_parses_numeric(fake_backend) -> None:
    _auto_reply(fake_backend, replies={"MEASure:VOLTage?": "12.50 V"})
    ps = EaPs9000T(port="FAKE", auto_connect=False, limits=PowerSupplyLimits(), auto_remote=False)
    ps.connect(auto_remote=False)

    voltage = ps.measure_voltage()

    assert voltage == pytest.approx(12.5)
    ps.close(output_off=False, remote_off=False)


def test_output_off_recovers_after_fake_write_failure(fake_backend) -> None:
    _auto_reply(fake_backend)
    ps = EaPs9000T(port="FAKE", auto_connect=False, limits=PowerSupplyLimits(), auto_remote=False)
    ps.connect(auto_remote=False)

    fake_backend.instances[-1].fail_write = True

    def heal_on_reconnect(*args, **kwargs):
        idn = EaPs9000T.connect(ps, auto_remote=False)
        fake_backend.instances[-1].fail_write = False
        return idn

    ps.reconnect_safely = heal_on_reconnect  # type: ignore[method-assign]

    ps.output_off(verify=False)

    assert ps.is_connected
    ps.close(output_off=False, remote_off=False)
