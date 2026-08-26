from __future__ import annotations

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QCheckBox, QGroupBox, QHBoxLayout, QLabel, QPushButton, QSpinBox, QVBoxLayout, QWidget

from core.psu_controller import PsuController


class MeasurementTab(QWidget):
    def __init__(self, controller: PsuController, log_callback=None):
        super().__init__()
        self.controller = controller
        self.log_callback = log_callback or (lambda text: None)
        self.timer = QTimer(self); self.timer.timeout.connect(self.poll)
        root = QVBoxLayout(self)
        values = QGroupBox("Live Measurements")
        vals_layout = QHBoxLayout(values)
        self.v = QLabel("0.000 V"); self.i = QLabel("0.000 A"); self.p = QLabel("0.000 W")
        for label in [self.v, self.i, self.p]:
            label.setObjectName("measurement"); vals_layout.addWidget(label)
        root.addWidget(values)
        status = QGroupBox("Status")
        stat_layout = QVBoxLayout(status)
        self.status = QLabel("-"); self.errors = QLabel("-")
        stat_layout.addWidget(self.status); stat_layout.addWidget(self.errors)
        root.addWidget(status)
        controls = QHBoxLayout()
        self.interval = QSpinBox(); self.interval.setRange(100, 60000); self.interval.setValue(500); self.interval.setSuffix(" ms")
        self.fast = QCheckBox("Use fast measurement")
        start = QPushButton("Start monitoring"); stop = QPushButton("Stop monitoring")
        controls.addWidget(self.interval); controls.addWidget(self.fast); controls.addWidget(start); controls.addWidget(stop)
        root.addLayout(controls); root.addStretch()
        start.clicked.connect(lambda: self.timer.start(self.interval.value()))
        stop.clicked.connect(self.timer.stop)

    def poll(self):
        try:
            data = self.controller.measure(fast=self.fast.isChecked())
            self.v.setText(f"{data.get('voltage_v', 0):.4f} V")
            self.i.setText(f"{data.get('current_a', 0):.4f} A")
            self.p.setText(f"{data.get('power_w', 0):.4f} W")
            health = self.controller.check_health()
            self.status.setText(f"Status byte: {health.get('status_byte')} | Output: {health.get('output_on')} | Remote: {health.get('remote_owner')}")
            self.errors.setText(self.controller.get_errors())
        except Exception as exc:
            self.log_callback(f"Measurement error: {exc}")
