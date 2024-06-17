from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from .ui_extruder_widget import Ui_ExtruderWidget 

class ExtruderWidget(QWidget):

    sendExtruderFeedRequested = Signal(int, int)

    def __init__(self):
        super().__init__()
        self.ui = Ui_ExtruderWidget()
        self.ui.setupUi(self)

        self.ui.feedButton.clicked.connect(self._onSendExtruderFeedClicked)

    @Slot()
    def _onSendExtruderFeedClicked(self):
        self.sendExtruderFeedRequested.emit(int(self.ui.feedSpeed.value()), int(self.ui.feedDistance.value()))
