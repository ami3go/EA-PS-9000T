from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from core.psu_controller import PsuConnectionConfig, PsuController
from EAPS9000T_class import PowerSupplyLimits


class ConnectionTab(QWidget):
    connect_requested = Signal(object)
    disconnect_requested = Signal()
    reconnect_requested = Signal()

    def __init__(self, controller: PsuController):
        super().__init__()
        self.controller = controller
        root = QVBoxLayout(self)

        box = QGroupBox("Connection")
        form = QFormLayout(box)
        self.port_combo = QComboBox()
        self.manual_port = QLineEdit()
        self.keyword = QLineEdit("PS 9000 T")
        self.baudrate = QSpinBox(); self.baudrate.setRange(1200, 3000000); self.baudrate.setValue(115200)
        self.timeout = QDoubleSpinBox(); self.timeout.setRange(0.05, 30); self.timeout.setValue(1.0); self.timeout.setSuffix(" s")
        self.write_timeout = QDoubleSpinBox(); self.write_timeout.setRange(0.05, 30); self.write_timeout.setValue(1.0); self.write_timeout.setSuffix(" s")
        self.retry_cnt = QSpinBox(); self.retry_cnt.setRange(1, 20); self.retry_cnt.setValue(3)
        self.retry_delay = QDoubleSpinBox(); self.retry_delay.setRange(0, 10); self.retry_delay.setValue(0.2); self.retry_delay.setSuffix(" s")
        self.mock_mode = QCheckBox("Use Mock PSU"); self.mock_mode.setChecked(True)
        self.production_mode = QCheckBox("Production mode")
        form.addRow("Port dropdown", self.port_combo)
        form.addRow("Manual port", self.manual_port)
        form.addRow("Keyword", self.keyword)
        form.addRow("Baudrate", self.baudrate)
        form.addRow("Timeout", self.timeout)
        form.addRow("Write timeout", self.write_timeout)
        form.addRow("Retry count", self.retry_cnt)
        form.addRow("Retry delay", self.retry_delay)
        form.addRow(self.mock_mode)
        form.addRow(self.production_mode)
        root.addWidget(box)

        limits = QGroupBox("Model limits")
        limits_form = QFormLayout(limits)
        self.vmax = QDoubleSpinBox(); self.vmax.setRange(0, 2000); self.vmax.setValue(80); self.vmax.setSuffix(" V")
        self.imax = QDoubleSpinBox(); self.imax.setRange(0, 1000); self.imax.setValue(40); self.imax.setSuffix(" A")
        self.pmax = QDoubleSpinBox(); self.pmax.setRange(0, 100000); self.pmax.setValue(1500); self.pmax.setSuffix(" W")
        self.ovpmax = QDoubleSpinBox(); self.ovpmax.setRange(0, 2000); self.ovpmax.setValue(88); self.ovpmax.setSuffix(" V")
        self.ocpmax = QDoubleSpinBox(); self.ocpmax.setRange(0, 1000); self.ocpmax.setValue(44); self.ocpmax.setSuffix(" A")
        self.oppmax = QDoubleSpinBox(); self.oppmax.setRange(0, 100000); self.oppmax.setValue(1650); self.oppmax.setSuffix(" W")
        for label, widget in [("Voltage max", self.vmax), ("Current max", self.imax), ("Power max", self.pmax), ("OVP max", self.ovpmax), ("OCP max", self.ocpmax), ("OPP max", self.oppmax)]:
            limits_form.addRow(label, widget)
        root.addWidget(limits)

        identity = QGroupBox("Identity validation")
        identity_form = QFormLayout(identity)
        self.expected_contains = QLineEdit("EA,PS9000")
        self.expected_model = QLineEdit()
        self.expected_serial = QLineEdit()
        self.station_id = QLineEdit("PSU_GUI")
        identity_form.addRow("Expected IDN contains", self.expected_contains)
        identity_form.addRow("Expected model", self.expected_model)
        identity_form.addRow("Expected serial", self.expected_serial)
        identity_form.addRow("Station ID", self.station_id)
        root.addWidget(identity)

        buttons = QHBoxLayout()
        self.refresh_btn = QPushButton("Refresh ports")
        self.connect_btn = QPushButton("Connect")
        self.disconnect_btn = QPushButton("Disconnect")
        self.reconnect_btn = QPushButton("Reconnect safely")
        buttons.addWidget(self.refresh_btn); buttons.addWidget(self.connect_btn); buttons.addWidget(self.disconnect_btn); buttons.addWidget(self.reconnect_btn)
        root.addLayout(buttons)

        self.idn_label = QLabel("IDN: -")
        self.status_label = QLabel("Disconnected")
        root.addWidget(self.idn_label)
        root.addWidget(self.status_label)
        root.addStretch()

        self.refresh_btn.clicked.connect(self.refresh_ports)
        self.connect_btn.clicked.connect(lambda: self.connect_requested.emit(self.build_config()))
        self.disconnect_btn.clicked.connect(self.disconnect_requested)
        self.reconnect_btn.clicked.connect(self.reconnect_requested)
        self.refresh_ports()

    def refresh_ports(self):
        current = self.port_combo.currentText()
        self.port_combo.clear()
        self.port_combo.addItems(self.controller.available_ports())
        if current:
            idx = self.port_combo.findText(current)
            if idx >= 0:
                self.port_combo.setCurrentIndex(idx)

    def build_config(self) -> PsuConnectionConfig:
        port = self.manual_port.text().strip() or self.port_combo.currentText().strip() or None
        expected = [p.strip() for p in self.expected_contains.text().split(",") if p.strip()]
        limits = PowerSupplyLimits(
            voltage_max=self.vmax.value(), current_max=self.imax.value(), power_max=self.pmax.value(),
            ovp_max=self.ovpmax.value(), ocp_max=self.ocpmax.value(), opp_max=self.oppmax.value(),
        )
        return PsuConnectionConfig(
            mock_mode=self.mock_mode.isChecked(), port=port, keyword=self.keyword.text().strip() or "PS 9000 T",
            baudrate=self.baudrate.value(), timeout=self.timeout.value(), write_timeout=self.write_timeout.value(),
            retry_cnt=self.retry_cnt.value(), retry_delay=self.retry_delay.value(), production_mode=self.production_mode.isChecked(),
            expected_idn_contains=expected, expected_model=self.expected_model.text().strip() or None,
            expected_serial=self.expected_serial.text().strip() or None, station_id=self.station_id.text().strip() or None,
            limits=limits,
        )

    def set_connected(self, idn: str):
        self.idn_label.setText(f"IDN: {idn}")
        self.status_label.setText("Connected")

    def set_disconnected(self):
        self.status_label.setText("Disconnected")
