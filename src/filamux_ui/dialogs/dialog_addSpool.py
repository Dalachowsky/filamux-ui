from PySide6.QtWidgets import QDialog, QDialogButtonBox 
from .ui_dialog_addSpool import Ui_Dialog
from ..backend.filamux_client import FilamuxClient

class addSpool(QDialog):

    def __init__(self,index):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.index = index
        
        self.Ok = self.ui.buttonBox.accepted
        self.Cancel = self.ui.buttonBox.rejected
        # self.Reset = self.ui.buttonBox.buttonRole.

        self.ui.producerOfSpool.textChanged.connect(self._producerText)
        self.ui.colorOfSpool.textChanged.connect(self._colorText)
        self.ui.lenghtOfSpool.textChanged.connect(self._lenghtText)


    def _producerText(self, text):
        self.producer = f"Producent szpuli:     {text.capitalize()}"

    def _colorText(self, text):
        self.color = f"Kolor szpuli:     {text.capitalize()}"

    def _lenghtText(self, text):
        self.lenght = f"Długość szpuli:     {text}m"
















