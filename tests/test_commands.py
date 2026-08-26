"""Offline tests for SCPI command construction."""

import sys
from types import ModuleType


# These tests exercise command generation only.  Avoid requiring a serial device
# (or the pyserial wheel) in the test environment.
serial = ModuleType("serial")
serial_tools = ModuleType("serial.tools")
serial_list_ports = ModuleType("serial.tools.list_ports")
serial_list_ports.comports = lambda: []
serial.tools = serial_tools
serial_tools.list_ports = serial_list_ports
sys.modules.setdefault("serial", serial)
sys.modules.setdefault("serial.tools", serial_tools)
sys.modules.setdefault("serial.tools.list_ports", serial_list_ports)

from EAPS9000T import storage
from EAPS9000T.EAPS9000T_class import range_check


def test_public_command_builders() -> None:
    commands = storage()

    assert commands.source.voltage.val(12.5) == "SOUR:VOLTage 12.5V"
    assert commands.source.current.val(2) == "SOUR:CURrent 2A"
    assert commands.output.on() == "OUTP ON"
    assert commands.system.error_all.req() == "SYST:ERR:ALL?"


def test_values_are_clamped_to_supported_range() -> None:
    assert range_check(600, 0, 500, "voltage") == 500
    assert range_check(-1, 0, 500, "voltage") == 0
