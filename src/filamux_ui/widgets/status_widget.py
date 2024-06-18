
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from .ui_status_widget import Ui_StatusWidget
from ..backend.protobuf import GetStatusRes

class StatusWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_StatusWidget()
        self.ui.setupUi(self)

    @Slot(str)
    def onStatusChanged(self, status: str):
        self.ui.status.setText(status)

    @Slot(int)
    def onCurrentSpoolChanged(self, spool: int):
        self.ui.currentSpool.setText(f"{spool}")
