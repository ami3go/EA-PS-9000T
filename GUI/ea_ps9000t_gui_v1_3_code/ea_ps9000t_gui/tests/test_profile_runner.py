from pathlib import Path

from EAPS9000T_class import PowerSupplyLimits
from core.profile_loader import load_voltage_profile
from core.profile_runner import ProfileRunner, ProfileRunnerConfig
from core.psu_controller import PsuConnectionConfig, PsuController


def _connected_controller():
    c = PsuController()
    limits = PowerSupplyLimits(voltage_max=20, current_max=5, power_max=100, ovp_max=25, ocp_max=6, opp_max=150)
    c.connect(PsuConnectionConfig(mock_mode=True, limits=limits, expected_idn_contains=["MOCK"]))
    return c, limits


def test_profile_runner_executes_short_profile(tmp_path: Path):
    c, limits = _connected_controller()
    p = tmp_path / "profile.csv"
    p.write_text("time_s,voltage_v,current_a,power_w,output\n0,0,1,20,off\n0.05,5,1,20,on\n0.10,0,1,20,off\n", encoding="utf-8")
    result = load_voltage_profile(p, limits)
    assert result.ok and result.profile
    log_path = tmp_path / "measurement.csv"
    runner = ProfileRunner(c, result.profile, ProfileRunnerConfig(measurement_log_path=str(log_path), ramp_update_interval_ms=50, measurement_log_interval_ms=50))
    runner.start()
    runner.join(3)
    assert not runner.is_running
    assert log_path.exists()


def test_profile_runner_handles_stop_request(tmp_path: Path):
    c, limits = _connected_controller()
    p = tmp_path / "profile.csv"
    p.write_text("time_s,voltage_v,current_a,power_w,output\n0,0,1,20,on\n5,5,1,20,on\n", encoding="utf-8")
    result = load_voltage_profile(p, limits)
    runner = ProfileRunner(c, result.profile, ProfileRunnerConfig(output_off_on_stop=True))  # type: ignore[arg-type]
    runner.start()
    runner.stop()
    runner.join(3)
    assert not runner.is_running
