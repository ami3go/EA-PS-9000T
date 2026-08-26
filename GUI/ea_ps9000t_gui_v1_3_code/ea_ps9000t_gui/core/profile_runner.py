from __future__ import annotations

import csv
import logging
import threading
import time
import traceback
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable, Optional

from .profile_model import ProfileStep, VoltageProfile
from .psu_controller import PsuController

logger = logging.getLogger(__name__)

ProgressCallback = Callable[[dict], None]
MessageCallback = Callable[[str], None]
ErrorCallback = Callable[[BaseException, str], None]
FinishedCallback = Callable[[str], None]


@dataclass
class ProfileRunnerConfig:
    ramp_update_interval_ms: int = 100
    measurement_log_interval_ms: int = 500
    output_off_at_end: bool = True
    output_off_on_stop: bool = True
    output_off_on_error: bool = True
    log_measurements: bool = True
    measurement_log_path: Optional[str] = None
    output_verify: bool = True


class ProfileRunner:
    """Background thread runner for CSV voltage profiles."""

    def __init__(
        self,
        controller: PsuController,
        profile: VoltageProfile,
        config: Optional[ProfileRunnerConfig] = None,
        on_progress: Optional[ProgressCallback] = None,
        on_message: Optional[MessageCallback] = None,
        on_error: Optional[ErrorCallback] = None,
        on_finished: Optional[FinishedCallback] = None,
    ):
        self.controller = controller
        self.profile = profile
        self.config = config or ProfileRunnerConfig()
        self.on_progress = on_progress
        self.on_message = on_message
        self.on_error = on_error
        self.on_finished = on_finished
        self._stop_event = threading.Event()
        self._pause_event = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self._started_at = 0.0
        self._paused_total_s = 0.0
        self._pause_started_at: Optional[float] = None
        self._last_measurement_log_s = -1e9
        self._log_file = None
        self._log_writer: Optional[csv.DictWriter] = None

    @property
    def is_running(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    @property
    def is_paused(self) -> bool:
        return self._pause_event.is_set()

    def start(self) -> None:
        if self.is_running:
            raise RuntimeError("Profile is already running")
        self._stop_event.clear()
        self._pause_event.clear()
        self._thread = threading.Thread(target=self._run, name="ProfileRunner", daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop_event.set()

    def pause(self) -> None:
        if not self._pause_event.is_set():
            self._pause_started_at = time.monotonic()
            self._pause_event.set()
            self._emit_message("Profile paused")

    def resume(self) -> None:
        if self._pause_event.is_set():
            if self._pause_started_at is not None:
                self._paused_total_s += time.monotonic() - self._pause_started_at
            self._pause_started_at = None
            self._pause_event.clear()
            self._emit_message("Profile resumed")

    def join(self, timeout: Optional[float] = None) -> None:
        if self._thread is not None:
            self._thread.join(timeout)

    def _profile_elapsed_s(self) -> float:
        now = time.monotonic()
        paused = self._paused_total_s
        if self._pause_event.is_set() and self._pause_started_at is not None:
            paused += now - self._pause_started_at
        return now - self._started_at - paused

    def _wait_until(self, target_s: float) -> bool:
        while not self._stop_event.is_set():
            while self._pause_event.is_set() and not self._stop_event.is_set():
                time.sleep(0.05)
            if self._profile_elapsed_s() >= target_s:
                return True
            time.sleep(min(0.05, max(0.0, target_s - self._profile_elapsed_s())))
        return False

    def _apply_step(self, step: ProfileStep) -> None:
        if step.ovp_v is not None:
            self.controller.set_ovp(step.ovp_v)
        if step.ocp_a is not None:
            self.controller.set_ocp(step.ocp_a)
        if step.opp_w is not None:
            self.controller.set_opp(step.opp_w)
        if step.current_a is not None:
            self.controller.set_current(step.current_a)
        if step.power_w is not None:
            self.controller.set_power(step.power_w)
        self.controller.set_voltage(step.voltage_v)
        if step.output == "on":
            self.controller.output_on(verify=self.config.output_verify)
        elif step.output == "off":
            self.controller.output_off(verify=self.config.output_verify)

    def _maybe_measure_and_log(self, step: ProfileStep, force: bool = False, message: str = "") -> dict:
        elapsed = self._profile_elapsed_s()
        if not force and (elapsed - self._last_measurement_log_s) < (self.config.measurement_log_interval_ms / 1000.0):
            return {"elapsed_s": elapsed, "step_index": step.index}
        measurement = self.controller.measure(fast=False)
        self._last_measurement_log_s = elapsed
        output_state = "unknown"
        try:
            output_state = "on" if self.controller.is_output_on() else "off"
        except Exception:
            output_state = "unknown"
        row = {
            "timestamp_iso": datetime.now().isoformat(),
            "elapsed_s": f"{elapsed:.6f}",
            "step_index": step.index,
            "set_voltage_v": step.voltage_v,
            "set_current_a": step.current_a if step.current_a is not None else "",
            "set_power_w": step.power_w if step.power_w is not None else "",
            "measured_voltage_v": measurement.get("voltage_v", ""),
            "measured_current_a": measurement.get("current_a", ""),
            "measured_power_w": measurement.get("power_w", ""),
            "output_state": output_state,
            "status": "ok",
            "message": message,
        }
        if self._log_writer is not None:
            self._log_writer.writerow(row)
            if self._log_file:
                self._log_file.flush()
        if self.on_progress:
            self.on_progress(row)
        return row

    def _ramp_between(self, step: ProfileStep, next_step: ProfileStep) -> None:
        duration = max(0.0, next_step.time_s - step.time_s)
        if duration <= 0:
            return
        interval = max(0.05, self.config.ramp_update_interval_ms / 1000.0)
        while not self._stop_event.is_set():
            while self._pause_event.is_set() and not self._stop_event.is_set():
                time.sleep(0.05)
            elapsed = self._profile_elapsed_s()
            if elapsed >= next_step.time_s:
                break
            fraction = min(1.0, max(0.0, (elapsed - step.time_s) / duration))
            voltage = step.voltage_v + (next_step.voltage_v - step.voltage_v) * fraction
            self.controller.set_voltage(voltage)
            self._maybe_measure_and_log(
                ProfileStep(
                    index=step.index,
                    row_number=step.row_number,
                    time_s=elapsed,
                    voltage_v=voltage,
                    current_a=step.current_a,
                    power_w=step.power_w,
                    output="keep",
                    ramp="linear",
                    comment=step.comment,
                ),
                force=False,
                message="linear ramp",
            )
            time.sleep(interval)

    def _open_measurement_log(self) -> None:
        if not self.config.log_measurements:
            return
        path = Path(self.config.measurement_log_path or f"logs/profile_measurements_{datetime.now():%Y%m%d_%H%M%S}.csv")
        path.parent.mkdir(parents=True, exist_ok=True)
        self._log_file = path.open("w", encoding="utf-8", newline="")
        fields = [
            "timestamp_iso",
            "elapsed_s",
            "step_index",
            "set_voltage_v",
            "set_current_a",
            "set_power_w",
            "measured_voltage_v",
            "measured_current_a",
            "measured_power_w",
            "output_state",
            "status",
            "message",
        ]
        self._log_writer = csv.DictWriter(self._log_file, fieldnames=fields)
        self._log_writer.writeheader()

    def _close_measurement_log(self) -> None:
        if self._log_file is not None:
            self._log_file.close()
            self._log_file = None
            self._log_writer = None

    def _emit_message(self, text: str) -> None:
        logger.info(text)
        if self.on_message:
            self.on_message(text)

    def _run(self) -> None:
        status = "completed"
        self._started_at = time.monotonic()
        self._paused_total_s = 0.0
        self._last_measurement_log_s = -1e9
        self._emit_message(f"Profile started: {self.profile.path}")
        self._open_measurement_log()
        try:
            for i, step in enumerate(self.profile.steps):
                if not self._wait_until(step.time_s):
                    status = "stopped"
                    break
                overrun = self._profile_elapsed_s() - step.time_s
                if overrun > 0.25:
                    self._emit_message(f"Timing warning: step {step.index} overrun {overrun:.3f} s")
                self._apply_step(step)
                self._maybe_measure_and_log(step, force=True, message=step.comment)
                if step.ramp == "linear" and i + 1 < len(self.profile.steps):
                    self._ramp_between(step, self.profile.steps[i + 1])

            if self._stop_event.is_set():
                status = "stopped"
                if self.config.output_off_on_stop:
                    self.controller.output_off(verify=True)
            elif status == "completed" and self.config.output_off_at_end:
                self.controller.output_off(verify=True)
            self._emit_message(f"Profile {status}")
        except BaseException as exc:
            status = "error"
            tb = traceback.format_exc()
            logger.error("Profile execution failed: %s", exc, exc_info=True)
            if self.config.output_off_on_error:
                try:
                    self.controller.output_off(verify=True)
                except BaseException:
                    logger.critical("SAFETY WARNING: output state could not be verified", exc_info=True)
            if self.on_error:
                self.on_error(exc, tb)
        finally:
            self._close_measurement_log()
            if self.on_finished:
                self.on_finished(status)
