from __future__ import annotations

import logging

try:
    from PySide6.QtCore import Signal, QObject
    from PySide6.QtWidgets import QGroupBox, QPlainTextEdit, QVBoxLayout
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("PySide6 is required for the GUI. Install with: pip install PySide6") from exc


class QtLogEmitter(QObject):
    message = Signal(str)


class QTextEditLogHandler(logging.Handler):
    def __init__(self, emitter: QtLogEmitter):
        super().__init__()
        self.emitter = emitter

    def emit(self, record: logging.LogRecord) -> None:
        self.emitter.message.emit(self.format(record))


class LogPanel(QGroupBox):
    def __init__(self, title: str = "Application Log"):
        super().__init__(title)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.text)
        self.emitter = QtLogEmitter()
        self.emitter.message.connect(self.append)

    def create_handler(self) -> logging.Handler:
        handler = QTextEditLogHandler(self.emitter)
        handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s", "%H:%M:%S"))
        return handler

    def append(self, line: str) -> None:
        self.text.appendPlainText(line)
