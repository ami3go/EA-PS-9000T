from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import (
    QCheckBox,
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from core.profile_loader import load_voltage_profile, write_example_csv
from core.profile_runner import ProfileRunner, ProfileRunnerConfig
from core.psu_controller import PsuController

try:
    from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.figure import Figure
except Exception:  # pragma: no cover - matplotlib optional at runtime
    FigureCanvas = None
    Figure = None


class RunnerSignals(QObject):
    progress = Signal(dict)
    message = Signal(str)
    error = Signal(str, str)
    finished = Signal(str)


class ProfileTab(QWidget):
    def __init__(self, controller: PsuController):
        super().__init__()
        self.controller = controller
        self.profile = None
        self.runner: ProfileRunner | None = None
        self.signals = RunnerSignals()
        self.signals.progress.connect(self.on_progress)
        self.signals.message.connect(self.on_message)
        self.signals.error.connect(self.on_error)
        self.signals.finished.connect(self.on_finished)

        root = QVBoxLayout(self)
        file_box = QGroupBox("CSV Voltage Profile")
        file_layout = QHBoxLayout(file_box)
        self.path = QLineEdit(); self.path.setPlaceholderText("Select CSV profile...")
        load = QPushButton("Load CSV"); reload_btn = QPushButton("Reload"); example = QPushButton("Save example CSV")
        file_layout.addWidget(self.path); file_layout.addWidget(load); file_layout.addWidget(reload_btn); file_layout.addWidget(example)
        root.addWidget(file_box)

        self.validation = QTextEdit(); self.validation.setReadOnly(True); self.validation.setMaximumHeight(100)
        root.addWidget(self.validation)
        self.table = QTableWidget(0, 10)
        self.table.setHorizontalHeaderLabels(["time_s", "voltage_v", "current_a", "power_w", "ovp_v", "ocp_a", "opp_w", "output", "ramp", "comment"])
        root.addWidget(self.table)

        plot_box = QGroupBox("Profile Plot")
        plot_layout = QVBoxLayout(plot_box)
        if FigureCanvas and Figure:
            self.figure = Figure(figsize=(6, 2.4), tight_layout=True)
            self.canvas = FigureCanvas(self.figure)
            plot_layout.addWidget(self.canvas)
        else:
            self.figure = None
            self.canvas = None
            plot_layout.addWidget(QLabel("Install matplotlib to show profile plot."))
        root.addWidget(plot_box)

        cfg = QGroupBox("Execution Settings")
        cfg_l = QHBoxLayout(cfg)
        self.ramp_ms = QSpinBox(); self.ramp_ms.setRange(50, 10000); self.ramp_ms.setValue(100); self.ramp_ms.setSuffix(" ms ramp")
        self.log_ms = QSpinBox(); self.log_ms.setRange(100, 60000); self.log_ms.setValue(500); self.log_ms.setSuffix(" ms log")
        self.off_end = QCheckBox("Output off at end"); self.off_end.setChecked(True)
        self.off_stop = QCheckBox("Output off on stop"); self.off_stop.setChecked(True)
        self.off_error = QCheckBox("Output off on error"); self.off_error.setChecked(True)
        self.log_measure = QCheckBox("Log measurements"); self.log_measure.setChecked(True)
        for w in [self.ramp_ms, self.log_ms, self.off_end, self.off_stop, self.off_error, self.log_measure]: cfg_l.addWidget(w)
        root.addWidget(cfg)

        controls = QHBoxLayout()
        self.run_btn = QPushButton("Run profile"); self.pause_btn = QPushButton("Pause"); self.resume_btn = QPushButton("Resume"); self.stop_btn = QPushButton("Stop")
        controls.addWidget(self.run_btn); controls.addWidget(self.pause_btn); controls.addWidget(self.resume_btn); controls.addWidget(self.stop_btn)
        root.addLayout(controls)
        self.progress = QProgressBar(); root.addWidget(self.progress)
        self.status = QLabel("No profile loaded"); root.addWidget(self.status)

        load.clicked.connect(self.pick_and_load)
        reload_btn.clicked.connect(lambda: self.load_path(self.path.text()))
        example.clicked.connect(self.save_example)
        self.run_btn.clicked.connect(self.run_profile)
        self.pause_btn.clicked.connect(lambda: self.runner.pause() if self.runner else None)
        self.resume_btn.clicked.connect(lambda: self.runner.resume() if self.runner else None)
        self.stop_btn.clicked.connect(lambda: self.runner.stop() if self.runner else None)

    def pick_and_load(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open CSV profile", "", "CSV files (*.csv);;All files (*)")
        if path:
            self.path.setText(path)
            self.load_path(path)

    def save_example(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save example CSV", "example_voltage_profile.csv", "CSV files (*.csv)")
        if path:
            write_example_csv(path)
            QMessageBox.information(self, "Saved", f"Example CSV saved to:\n{path}")

    def load_path(self, path: str):
        if not path:
            return
        result = load_voltage_profile(path, self.controller.limits)
        self.validation.clear()
        for issue in result.issues:
            self.validation.append(f"[{issue.severity.upper()}] {issue}")
        if not result.ok or result.profile is None:
            self.profile = None
            self.status.setText("Profile validation failed")
            self.table.setRowCount(0)
            return
        self.profile = result.profile
        self.status.setText(f"Loaded {len(self.profile.steps)} steps, duration {self.profile.duration_s:.2f} s")
        self.populate_table()
        self.update_plot()

    def populate_table(self):
        self.table.setRowCount(0)
        if not self.profile:
            return
        for step in self.profile.steps:
            row = self.table.rowCount(); self.table.insertRow(row)
            values = [step.time_s, step.voltage_v, step.current_a, step.power_w, step.ovp_v, step.ocp_a, step.opp_w, step.output, step.ramp, step.comment]
            for col, val in enumerate(values):
                self.table.setItem(row, col, QTableWidgetItem("" if val is None else str(val)))

    def update_plot(self):
        if not self.profile or self.figure is None or self.canvas is None:
            return
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        t = [s.time_s for s in self.profile.steps]
        v = [s.voltage_v for s in self.profile.steps]
        ax.step(t, v, where="post", label="Voltage V")
        if any(s.current_a is not None for s in self.profile.steps):
            ax.step(t, [float(s.current_a or 0) for s in self.profile.steps], where="post", label="Current A")
        if any(s.power_w is not None for s in self.profile.steps):
            ax.step(t, [float(s.power_w or 0) for s in self.profile.steps], where="post", label="Power W")
        for s in self.profile.steps:
            if s.output != "keep":
                ax.axvline(s.time_s, linestyle="--", linewidth=0.8)
                ax.text(s.time_s, max(v) if v else 0, s.output.upper(), rotation=90, va="bottom", fontsize=8)
        ax.set_xlabel("Time, s")
        ax.grid(True, alpha=0.25)
        ax.legend(loc="best")
        self.canvas.draw_idle()

    def run_profile(self):
        if not self.profile:
            QMessageBox.warning(self, "No profile", "Load and validate a CSV profile first.")
            return
        config = ProfileRunnerConfig(
            ramp_update_interval_ms=self.ramp_ms.value(),
            measurement_log_interval_ms=self.log_ms.value(),
            output_off_at_end=self.off_end.isChecked(),
            output_off_on_stop=self.off_stop.isChecked(),
            output_off_on_error=self.off_error.isChecked(),
            log_measurements=self.log_measure.isChecked(),
        )
        self.runner = ProfileRunner(
            self.controller,
            self.profile,
            config,
            on_progress=self.signals.progress.emit,
            on_message=self.signals.message.emit,
            on_error=lambda e, tb: self.signals.error.emit(str(e), tb),
            on_finished=self.signals.finished.emit,
        )
        self.progress.setValue(0)
        self.runner.start()

    def on_progress(self, row: dict):
        if self.profile and self.profile.duration_s > 0:
            elapsed = float(row.get("elapsed_s", 0))
            self.progress.setValue(min(100, int(100 * elapsed / self.profile.duration_s)))
        self.status.setText(f"Step {row.get('step_index')} elapsed {row.get('elapsed_s')} s")

    def on_message(self, msg: str):
        self.status.setText(msg)

    def on_error(self, msg: str, tb: str):
        self.status.setText(f"ERROR: {msg}")
        QMessageBox.critical(self, "Profile error", f"{msg}\n\n{tb[-2000:]}")

    def on_finished(self, status: str):
        self.status.setText(f"Profile {status}")
        if status == "completed": self.progress.setValue(100)
