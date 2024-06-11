from PySide6.QtWidgets import QDialog, QDialogButtonBox 
from .ui_dialog_addSpool import Ui_Dialog
class addSpool(QDialog):

    def __init__(self, index: int):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.index = index

        self.producer = self.ui.producerOfSpool.text()
        self.color = self.ui.colorOfSpool.text()
        self.lenght = self.ui.producerOfSpool.text()

        self.button_clicked = self.ui.buttonBox.clicked
    
   

        





























