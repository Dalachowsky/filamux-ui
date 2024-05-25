
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from .ui_main_window import Ui_MainWindow
from .widgets.spool_widget import SpoolWidget 
from .dialogs.dialog_connect import DialogConnect
from .backend.filamux_client import FilamuxClient
from .backend.filamux_model import FilamuxModel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # Initialize fields
        self._client = FilamuxClient()
        self._model = FilamuxModel()
        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.spoolWidget1 = SpoolWidget(1)
        self.spoolWidget2 = SpoolWidget(2)
        self.dialogConnect = DialogConnect(self._client)
        self.ui.root.layout().addWidget(self.spoolWidget1, 1, 1)
        self.ui.root.layout().addWidget(self.spoolWidget2, 1, 2)

        # Connect signals
        self._model.spoolChanged.connect(self.onSpoolChanged)
        self.spoolWidget1.szpulRequest.connect(self._client.sendSetActiveSpool)
        self.spoolWidget2.szpulRequest.connect(self._client.sendSetActiveSpool)

        self._model.currentSpool = 0
        self._model.currentSpool = 1

    @Slot(int)
    def onSpoolChanged(self, spool):
        print(f"Spool changed: {spool}")

    def show(self):
        super().show()              # Call parent class show()
        self.dialogConnect.show()   # Display dialog for connection

