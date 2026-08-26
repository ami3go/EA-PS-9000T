import pytest

from EAPS9000T_class import PowerSupplyLimits, RangeError
from core.mock_psu import MockPsu


def test_mock_psu_connects_and_disconnects():
    psu = MockPsu(limits=PowerSupplyLimits(voltage_max=10))
    assert psu.connect().startswith("MOCK")
    assert psu.is_connected
    psu.close()
    assert not psu.is_connected


def test_mock_psu_stores_setpoints_and_measures():
    psu = MockPsu(limits=PowerSupplyLimits(voltage_max=10, current_max=2, power_max=50))
    psu.connect()
    psu.set_voltage(5)
    psu.set_current(1)
    psu.set_power(20)
    psu.output_on(verify=True)
    data = psu.measure_all()
    assert 4.9 <= data["voltage_v"] <= 5.1
    assert psu.get_voltage_setpoint() == 5


def test_mock_psu_rejects_range_error():
    psu = MockPsu(limits=PowerSupplyLimits(voltage_max=10))
    psu.connect()
    with pytest.raises(RangeError):
        psu.set_voltage(11)
