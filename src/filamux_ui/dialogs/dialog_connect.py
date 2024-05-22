
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal, Slot
from PySide6.QtSerialPort import QSerialPort
from .ui_dialog_connect import Ui_DialogConnect
from ..backend.filamux_client import FilamuxClient

baudrates = [
    ("115200", QSerialPort.BaudRate.Baud115200),
    ("9600", QSerialPort.BaudRate.Baud9600)
]

class DialogConnect(QDialog):

    def __init__(self, client: FilamuxClient):
        super().__init__()
        self.ui = Ui_DialogConnect()
        self.ui.setupUi(self)
        self._setConnecting(False)
        self._client = client

        for baud in baudrates:
            self.ui.baudrateSelector.addItem(baud[0], userData=baud[1])

        # Signals
        self.ui.connectButton.clicked.connect(self._connectRequested)

    def _setConnecting(self, state: bool):
        if state:
            self.ui.connectButton.setText("Łączenie...")
        else:
            self.ui.connectButton.setText("Połącz")
        self.ui.connectButton.setDisabled(state)

    @Slot()
    def _connectRequested(self):
        self._client.setBaudRate(self.ui.baudrateSelector.currentData)
        self._client.setPort(self.ui.portValue.text())
        self._client.start()
        self._setConnecting(True)
