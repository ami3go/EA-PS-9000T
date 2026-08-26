from __future__ import annotations

MATERIAL_DARK_QSS = """
* { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.5pt; }
QMainWindow, QWidget { background: #121212; color: #EDEDED; }
QTabWidget::pane { border: 1px solid #2A2A2A; border-radius: 12px; padding: 6px; }
QTabBar::tab { background: #1E1E1E; border: 1px solid #2B2B2B; padding: 9px 14px; border-top-left-radius: 8px; border-top-right-radius: 8px; }
QTabBar::tab:selected { background: #263238; color: #FFFFFF; border-bottom: 2px solid #80CBC4; }
QGroupBox { border: 1px solid #303030; border-radius: 12px; margin-top: 18px; padding: 12px; background: #1A1A1A; }
QGroupBox::title { subcontrol-origin: margin; left: 14px; padding: 0 6px; color: #B2DFDB; }
QLineEdit, QDoubleSpinBox, QSpinBox, QComboBox, QTextEdit, QPlainTextEdit, QTableWidget {
    background: #202020; color: #F5F5F5; border: 1px solid #3A3A3A; border-radius: 8px; padding: 6px;
}
QPushButton { background: #2D3A3A; color: #FFFFFF; border: 0px; border-radius: 8px; padding: 8px 12px; min-height: 28px; }
QPushButton:hover { background: #365050; }
QPushButton:disabled { background: #2A2A2A; color: #777777; }
QPushButton#primaryButton { background: #006A60; }
QPushButton#primaryButton:hover { background: #00796B; }
QPushButton#dangerButton { background: #B3261E; font-weight: 700; }
QPushButton#dangerButton:hover { background: #D32F2F; }
QPushButton#warningButton { background: #B26A00; font-weight: 700; }
QLabel#measurement { font-size: 34px; font-weight: 700; color: #FFFFFF; }
QLabel#statusChip { border-radius: 10px; padding: 5px 10px; font-weight: 700; background: #424242; color: white; }
QLabel#banner { border-radius: 10px; padding: 9px 12px; font-weight: 700; background: #2E2E2E; }
"""


def set_button_kind(button, kind: str) -> None:
    if kind == "primary":
        button.setObjectName("primaryButton")
    elif kind == "danger":
        button.setObjectName("dangerButton")
    elif kind == "warning":
        button.setObjectName("warningButton")


def status_color(style: str) -> str:
    return {
        "ok": "#1B5E20",
        "error": "#B3261E",
        "warning": "#B26A00",
        "unknown": "#424242",
        "info": "#0D47A1",
    }.get(style, "#424242")


def set_status_chip(label, text: str, style: str = "unknown") -> None:
    label.setText(text)
    label.setObjectName("statusChip")
    label.setStyleSheet(f"QLabel#statusChip {{ background: {status_color(style)}; }}")
