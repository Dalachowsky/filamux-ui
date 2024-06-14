
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from .ui_status_widget import Ui_StatusWidget
from ..backend.protobuf import GetStatusRes

class StatusWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_StatusWidget()
        self.ui.setupUi(self)

    @Slot(GetStatusRes)
    def onStatusReceived(self, msg: GetStatusRes):
        pass
