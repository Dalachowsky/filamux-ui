from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from .ui_spool_widget import Ui_SpoolWidget 

class SpoolWidget(QWidget):

    szpulRequest = Signal(int)

    def __init__(self, index: int):
        super().__init__()
        self.ui = Ui_SpoolWidget()
        self.ui.setupUi(self)
        self.index = index
        print(f"SpoolWidget: {index}")

        self.ui.changeButton.clicked.connect(self._onChangeButtonClick)

    @Slot()
    def _onChangeButtonClick(self):
        self.szpulRequest.emit(self.index)