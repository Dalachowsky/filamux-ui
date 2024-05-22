
from PySide6.QtWidgets import QApplication

from .main_window import MainWindow

app = QApplication()

window = MainWindow()
window.setWindowTitle("Filamux-UI")
window.show()

app.exec()
