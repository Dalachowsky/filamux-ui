from PySide6.QtWidgets import QWidget
from .ui_spool_widget import Ui_SpoolWidget

class SpoolWidget(QWidget):

    def __init__(self, index: int):
        super().__init__()
        self.ui = Ui_SpoolWidget()
        self.ui.setupUi(self)

