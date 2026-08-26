from __future__ import annotations

import sys
from pathlib import Path

from core.logging_setup import configure_logging


def main() -> int:
    configure_logging(Path(__file__).resolve().parent / "logs")
    try:
        from PySide6.QtWidgets import QApplication
        from gui.main_window import MainWindow
    except ImportError as exc:
        print("PySide6 is required for the GUI. Install dependencies with: pip install -r requirements.txt")
        raise

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
