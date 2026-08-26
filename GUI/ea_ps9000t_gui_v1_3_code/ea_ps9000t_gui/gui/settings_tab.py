from __future__ import annotations

from PySide6.QtWidgets import QCheckBox, QComboBox, QFormLayout, QGroupBox, QLineEdit, QSpinBox, QVBoxLayout, QWidget


class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        root = QVBoxLayout(self)
        box = QGroupBox("Application Settings")
        form = QFormLayout(box)
        self.theme = QComboBox(); self.theme.addItems(["dark_material"])
        self.log_dir = QLineEdit("logs")
        self.csv_dir = QLineEdit("examples")
        self.confirm_output_on = QCheckBox(); self.confirm_output_on.setChecked(True)
        self.off_close = QCheckBox(); self.off_close.setChecked(True)
        self.default_monitor_ms = QSpinBox(); self.default_monitor_ms.setRange(100, 60000); self.default_monitor_ms.setValue(500)
        form.addRow("Theme", self.theme)
        form.addRow("Log directory", self.log_dir)
        form.addRow("Default CSV directory", self.csv_dir)
        form.addRow("Confirm before output ON", self.confirm_output_on)
        form.addRow("Output off on close", self.off_close)
        form.addRow("Default monitor interval", self.default_monitor_ms)
        root.addWidget(box); root.addStretch()
