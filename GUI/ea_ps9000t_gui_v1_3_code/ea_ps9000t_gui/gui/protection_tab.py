from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDoubleSpinBox, QFormLayout, QGroupBox, QHBoxLayout, QPushButton, QVBoxLayout, QWidget


class ProtectionTab(QWidget):
    set_ovp = Signal(float)
    set_ocp = Signal(float)
    set_opp = Signal(float)
    apply_all = Signal(float, float, float)

    def __init__(self):
        super().__init__()
        root = QVBoxLayout(self)
        box = QGroupBox("Protection Limits")
        form = QFormLayout(box)
        self.ovp = QDoubleSpinBox(); self.ovp.setRange(0, 2000); self.ovp.setDecimals(4); self.ovp.setValue(30); self.ovp.setSuffix(" V")
        self.ocp = QDoubleSpinBox(); self.ocp.setRange(0, 1000); self.ocp.setDecimals(4); self.ocp.setValue(2); self.ocp.setSuffix(" A")
        self.opp = QDoubleSpinBox(); self.opp.setRange(0, 100000); self.opp.setDecimals(3); self.opp.setValue(150); self.opp.setSuffix(" W")
        form.addRow("OVP", self.ovp); form.addRow("OCP", self.ocp); form.addRow("OPP", self.opp)
        root.addWidget(box)
        row = QHBoxLayout()
        btn_ovp = QPushButton("Set OVP"); btn_ocp = QPushButton("Set OCP"); btn_opp = QPushButton("Set OPP"); btn_all = QPushButton("Apply all protections")
        for b in [btn_ovp, btn_ocp, btn_opp, btn_all]: row.addWidget(b)
        root.addLayout(row); root.addStretch()
        btn_ovp.clicked.connect(lambda: self.set_ovp.emit(self.ovp.value()))
        btn_ocp.clicked.connect(lambda: self.set_ocp.emit(self.ocp.value()))
        btn_opp.clicked.connect(lambda: self.set_opp.emit(self.opp.value()))
        btn_all.clicked.connect(lambda: self.apply_all.emit(self.ovp.value(), self.ocp.value(), self.opp.value()))
