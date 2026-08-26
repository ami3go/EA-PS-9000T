from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDoubleSpinBox, QFormLayout, QGroupBox, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget


class ManualControlTab(QWidget):
    set_voltage = Signal(float)
    set_current = Signal(float)
    set_power = Signal(float)
    apply_all = Signal(float, float, float)
    readback = Signal()

    def __init__(self):
        super().__init__()
        root = QVBoxLayout(self)
        box = QGroupBox("Manual Setpoints")
        form = QFormLayout(box)
        self.voltage = QDoubleSpinBox(); self.voltage.setRange(0, 2000); self.voltage.setDecimals(4); self.voltage.setSuffix(" V")
        self.current = QDoubleSpinBox(); self.current.setRange(0, 1000); self.current.setDecimals(4); self.current.setSuffix(" A")
        self.power = QDoubleSpinBox(); self.power.setRange(0, 100000); self.power.setDecimals(3); self.power.setSuffix(" W")
        self.v_read = QLabel("-"); self.i_read = QLabel("-"); self.p_read = QLabel("-")
        form.addRow("Voltage", self.voltage); form.addRow("Voltage readback", self.v_read)
        form.addRow("Current", self.current); form.addRow("Current readback", self.i_read)
        form.addRow("Power", self.power); form.addRow("Power readback", self.p_read)
        root.addWidget(box)
        row = QHBoxLayout()
        btn_v = QPushButton("Set voltage"); btn_i = QPushButton("Set current"); btn_p = QPushButton("Set power")
        btn_all = QPushButton("Apply all"); btn_read = QPushButton("Read setpoints")
        for b in [btn_v, btn_i, btn_p, btn_all, btn_read]: row.addWidget(b)
        root.addLayout(row); root.addStretch()
        btn_v.clicked.connect(lambda: self.set_voltage.emit(self.voltage.value()))
        btn_i.clicked.connect(lambda: self.set_current.emit(self.current.value()))
        btn_p.clicked.connect(lambda: self.set_power.emit(self.power.value()))
        btn_all.clicked.connect(lambda: self.apply_all.emit(self.voltage.value(), self.current.value(), self.power.value()))
        btn_read.clicked.connect(self.readback)

    def update_readback(self, v: float, i: float, p: float):
        self.v_read.setText(f"{v:.6g} V"); self.i_read.setText(f"{i:.6g} A"); self.p_read.setText(f"{p:.6g} W")
