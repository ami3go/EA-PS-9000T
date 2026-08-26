from EAPS9000T_class import PowerSupplyLimits
from core.psu_controller import PsuConnectionConfig, PsuController


def test_controller_handles_mock_backend():
    c = PsuController()
    idn = c.connect(PsuConnectionConfig(mock_mode=True, limits=PowerSupplyLimits(voltage_max=10), expected_idn_contains=["MOCK"]))
    assert "MOCK" in idn
    c.set_voltage(5)
    assert c.get_voltage_setpoint() == 5
    c.disconnect()
    assert not c.is_connected()
