import sys
from PySide6.QtWidgets import QApplication

from qt_code.custom_main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(parent_app=app)
    window.show()

    sys.exit(app.exec())
