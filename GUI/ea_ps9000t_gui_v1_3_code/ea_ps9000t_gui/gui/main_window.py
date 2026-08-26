from __future__ import annotations

import logging
from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSplitter,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt

from core.psu_controller import PsuController, PsuConnectionConfig
from .connection_tab import ConnectionTab
from .log_panel import LogPanel
from .manual_control_tab import ManualControlTab
from .measurement_tab import MeasurementTab
from .profile_tab import ProfileTab
from .protection_tab import ProtectionTab
from .settings_tab import SettingsTab
from .widgets import MATERIAL_DARK_QSS, set_button_kind, set_status_chip

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EA PS 9000 T Control GUI")
        self.resize(1366, 850)
        self.controller = PsuController()
        self.setStyleSheet(MATERIAL_DARK_QSS)
        self._build_ui()
        self._connect_signals()
        self._set_disconnected_ui()

    def _build_ui(self):
        central = QWidget()
        root = QVBoxLayout(central)
        self.setCentralWidget(central)

        top = QHBoxLayout()
        self.device_chip = QLabel("DISCONNECTED")
        self.output_chip = QLabel("OUTPUT: UNKNOWN")
        self.idn_label = QLabel("IDN: -")
        set_status_chip(self.device_chip, "DISCONNECTED", "error")
        set_status_chip(self.output_chip, "OUTPUT: UNKNOWN", "warning")
        top.addWidget(self.device_chip); top.addWidget(self.output_chip); top.addWidget(self.idn_label, 1)
        root.addLayout(top)

        self.banner = QLabel("Ready. Use mock mode first before real hardware.")
        self.banner.setObjectName("banner")
        root.addWidget(self.banner)

        output_box = QGroupBox("Persistent Output Control")
        output_layout = QHBoxLayout(output_box)
        self.output_on_btn = QPushButton("OUTPUT ON")
        self.output_off_btn = QPushButton("OUTPUT OFF")
        self.emergency_btn = QPushButton("EMERGENCY OFF")
        set_button_kind(self.output_on_btn, "warning")
        set_button_kind(self.output_off_btn, "primary")
        set_button_kind(self.emergency_btn, "danger")
        self.verify_label = QLabel("Switching verification: ON")
        output_layout.addWidget(self.output_on_btn); output_layout.addWidget(self.output_off_btn); output_layout.addWidget(self.emergency_btn); output_layout.addWidget(self.verify_label, 1)
        root.addWidget(output_box)

        splitter = QSplitter(Qt.Vertical)
        self.tabs = QTabWidget()
        self.connection_tab = ConnectionTab(self.controller)
        self.manual_tab = ManualControlTab()
        self.protection_tab = ProtectionTab()
        self.measurement_tab = MeasurementTab(self.controller, log_callback=lambda t: logger.warning(t))
        self.profile_tab = ProfileTab(self.controller)
        self.settings_tab = SettingsTab()
        self.dashboard = self._create_dashboard()
        self.tabs.addTab(self.dashboard, "Dashboard")
        self.tabs.addTab(self.connection_tab, "Connection")
        self.tabs.addTab(self.manual_tab, "Manual Control")
        self.tabs.addTab(self.protection_tab, "Protection Limits")
        self.tabs.addTab(self.measurement_tab, "Live Measurements")
        self.tabs.addTab(self.profile_tab, "Voltage Profile")
        self.tabs.addTab(self.settings_tab, "Settings")

        self.log_panel = LogPanel()
        logging.getLogger().addHandler(self.log_panel.create_handler())
        splitter.addWidget(self.tabs)
        splitter.addWidget(self.log_panel)
        splitter.setSizes([620, 180])
        root.addWidget(splitter, 1)

        self.dashboard_timer = QTimer(self)
        self.dashboard_timer.timeout.connect(self.refresh_dashboard)
        self.dashboard_timer.start(1000)

    def _create_dashboard(self) -> QWidget:
        w = QWidget()
        layout = QVBoxLayout(w)
        box = QGroupBox("Dashboard")
        row = QHBoxLayout(box)
        self.dash_v = QLabel("0.000 V"); self.dash_i = QLabel("0.000 A"); self.dash_p = QLabel("0.000 W")
        for lbl in [self.dash_v, self.dash_i, self.dash_p]:
            lbl.setObjectName("measurement")
            row.addWidget(lbl)
        layout.addWidget(box)
        self.dash_status = QLabel("Disconnected")
        layout.addWidget(self.dash_status)
        layout.addStretch()
        return w

    def _connect_signals(self):
        self.connection_tab.connect_requested.connect(self.connect_psu)
        self.connection_tab.disconnect_requested.connect(self.disconnect_psu)
        self.connection_tab.reconnect_requested.connect(self.reconnect_psu)
        self.manual_tab.set_voltage.connect(lambda v: self._safe_call("Set voltage", lambda: self.controller.set_voltage(v)))
        self.manual_tab.set_current.connect(lambda i: self._safe_call("Set current", lambda: self.controller.set_current(i)))
        self.manual_tab.set_power.connect(lambda p: self._safe_call("Set power", lambda: self.controller.set_power(p)))
        self.manual_tab.apply_all.connect(self.apply_setpoints)
        self.manual_tab.readback.connect(self.read_setpoints)
        self.protection_tab.set_ovp.connect(lambda v: self._safe_call("Set OVP", lambda: self.controller.set_ovp(v)))
        self.protection_tab.set_ocp.connect(lambda i: self._safe_call("Set OCP", lambda: self.controller.set_ocp(i)))
        self.protection_tab.set_opp.connect(lambda p: self._safe_call("Set OPP", lambda: self.controller.set_opp(p)))
        self.protection_tab.apply_all.connect(self.apply_protections)
        self.output_on_btn.clicked.connect(self.safe_output_on)
        self.output_off_btn.clicked.connect(lambda: self._safe_call("Output OFF", lambda: self.controller.output_off(verify=True), refresh=True))
        self.emergency_btn.clicked.connect(lambda: self._safe_call("EMERGENCY OFF", self.controller.emergency_off, refresh=True, critical=True))

    def connect_psu(self, config: PsuConnectionConfig):
        self._safe_call("Connect", lambda: self._do_connect(config), refresh=True)

    def _do_connect(self, config: PsuConnectionConfig):
        idn = self.controller.connect(config)
        self.idn_label.setText(f"IDN: {idn}")
        self.connection_tab.set_connected(idn)
        set_status_chip(self.device_chip, "CONNECTED", "ok")
        logger.info("Connected: %s", idn)

    def disconnect_psu(self):
        self._safe_call("Disconnect", self.controller.disconnect, refresh=True)
        self._set_disconnected_ui()

    def reconnect_psu(self):
        self._safe_call("Reconnect", lambda: self.idn_label.setText(f"IDN: {self.controller.reconnect_safely()}"), refresh=True)

    def apply_setpoints(self, v: float, i: float, p: float):
        def work():
            self.controller.set_voltage(v); self.controller.set_current(i); self.controller.set_power(p)
        self._safe_call("Apply setpoints", work)

    def apply_protections(self, ovp: float, ocp: float, opp: float):
        def work():
            self.controller.set_ovp(ovp); self.controller.set_ocp(ocp); self.controller.set_opp(opp)
        self._safe_call("Apply protections", work)

    def read_setpoints(self):
        def work():
            v = self.controller.get_voltage_setpoint(); i = self.controller.get_current_setpoint(); p = self.controller.get_power_setpoint()
            self.manual_tab.update_readback(v, i, p)
        self._safe_call("Read setpoints", work)

    def safe_output_on(self):
        msg = (
            f"Enable output with current GUI/controller setpoints?\n\n"
            f"Voltage: {self.manual_tab.voltage.value()} V\nCurrent: {self.manual_tab.current.value()} A\nPower: {self.manual_tab.power.value()} W\n"
            f"OVP: {self.protection_tab.ovp.value()} V\nOCP: {self.protection_tab.ocp.value()} A\nOPP: {self.protection_tab.opp.value()} W"
        )
        if QMessageBox.warning(self, "Confirm OUTPUT ON", msg, QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        def work():
            # Keep this sequence in one controller-level critical operation path; do not call GUI helper
            # methods here because they catch exceptions independently.
            self.controller.set_ovp(self.protection_tab.ovp.value())
            self.controller.set_ocp(self.protection_tab.ocp.value())
            self.controller.set_opp(self.protection_tab.opp.value())
            self.controller.set_voltage(self.manual_tab.voltage.value())
            self.controller.set_current(self.manual_tab.current.value())
            self.controller.set_power(self.manual_tab.power.value())
            self.controller.safe_output_on_from_cached_values(verify=True)
        self._safe_call("Output ON", work, refresh=True, critical=True)

    def refresh_dashboard(self):
        if not self.controller.is_connected():
            return
        try:
            data = self.controller.measure(fast=True)
            self.dash_v.setText(f"{data.get('voltage_v', 0):.4f} V")
            self.dash_i.setText(f"{data.get('current_a', 0):.4f} A")
            self.dash_p.setText(f"{data.get('power_w', 0):.4f} W")
            out = self.controller.is_output_on()
            set_status_chip(self.output_chip, "OUTPUT: ON" if out else "OUTPUT: OFF", "warning" if out else "ok")
            self.dash_status.setText("Connected")
        except Exception as exc:
            logger.warning("Dashboard refresh failed: %s", exc)
            set_status_chip(self.output_chip, "OUTPUT: UNKNOWN", "error")

    def _set_disconnected_ui(self):
        set_status_chip(self.device_chip, "DISCONNECTED", "error")
        set_status_chip(self.output_chip, "OUTPUT: UNKNOWN", "warning")
        self.connection_tab.set_disconnected()
        self.dash_status.setText("Disconnected")

    def _safe_call(self, title: str, func, refresh: bool = False, critical: bool = False):
        try:
            result = func()
            logger.info("%s OK", title)
            if refresh:
                self.refresh_dashboard()
            return result
        except Exception as exc:
            logger.error("%s failed: %s", title, exc, exc_info=True)
            self.banner.setText(f"ERROR: {title} failed: {exc}")
            if critical:
                set_status_chip(self.output_chip, "OUTPUT: UNKNOWN", "error")
            QMessageBox.critical(self, f"{title} failed", str(exc))

    def closeEvent(self, event):
        try:
            if self.controller.is_connected():
                self.controller.disconnect(suppress_errors=True)
        finally:
            event.accept()
