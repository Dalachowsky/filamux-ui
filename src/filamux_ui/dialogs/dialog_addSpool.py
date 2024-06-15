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

    def show(self):
        super().show()
        self.ui.producerOfSpool.clear()
        self.ui.colorOfSpool.clear()
        self.ui.lenghtOfSpool.clear()



    def getSpoolLength(self):
        if self.ui.lenghtOfSpool.text() == "":
            return None
        try:
            return int(self.ui.lenghtOfSpool.text())
        except Exception as error:
            print(error)
            return None

    def getSpoolProducer(self):
        if self.ui.producerOfSpool.text() == "":
            return None
        return self.ui.producerOfSpool.text()
    
    def getSpoolcolor(self):
        if self.ui.colorOfSpool.text() == "":
            return None
        return self.ui.colorOfSpool.text()

    def _producerText(self, text):
        text = text
        self.producer = f"Producent szpuli:     {text.capitalize()}"

    def _colorText(self, text):
        text = text
        self.color = f"Kolor szpuli:     {text.capitalize()}"

    def _lenghtText(self, text):
        text = text
        self.lenght = f"Długość szpuli:     {text}m"














