from pathlib import Path

from EAPS9000T_class import PowerSupplyLimits
from core.profile_loader import load_voltage_profile


def test_profile_loader_accepts_valid_csv(tmp_path: Path):
    p = tmp_path / "valid.csv"
    p.write_text("time_s,voltage_v,current_a,output,ramp\n0,0,1,off,step\n1,5,1,on,linear\n2,10,1,keep,step\n", encoding="utf-8")
    result = load_voltage_profile(p, PowerSupplyLimits(voltage_max=20, current_max=5, power_max=100))
    assert result.ok
    assert result.profile is not None
    assert len(result.profile.steps) == 3


def test_profile_loader_rejects_missing_required_columns(tmp_path: Path):
    p = tmp_path / "bad.csv"
    p.write_text("time_s,current_a\n0,1\n", encoding="utf-8")
    result = load_voltage_profile(p, PowerSupplyLimits())
    assert not result.ok
    assert any(i.column == "voltage_v" for i in result.errors)


def test_profile_loader_rejects_non_monotonic_time(tmp_path: Path):
    p = tmp_path / "bad.csv"
    p.write_text("time_s,voltage_v\n0,1\n0,2\n", encoding="utf-8")
    result = load_voltage_profile(p, PowerSupplyLimits(voltage_max=10))
    assert not result.ok
    assert any("strictly increasing" in i.message for i in result.errors)


def test_profile_loader_rejects_out_of_range_voltage(tmp_path: Path):
    p = tmp_path / "bad.csv"
    p.write_text("time_s,voltage_v\n0,999\n", encoding="utf-8")
    result = load_voltage_profile(p, PowerSupplyLimits(voltage_max=10))
    assert not result.ok
    assert any(i.column == "voltage_v" for i in result.errors)


def test_profile_loader_rejects_invalid_output_and_ramp(tmp_path: Path):
    p = tmp_path / "bad.csv"
    p.write_text("time_s,voltage_v,output,ramp\n0,1,enable,smooth\n", encoding="utf-8")
    result = load_voltage_profile(p, PowerSupplyLimits(voltage_max=10))
    assert not result.ok
    assert any(i.column == "output" for i in result.errors)
    assert any(i.column == "ramp" for i in result.errors)
