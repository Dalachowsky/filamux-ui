from PySide6.QtWidgets import QWidget, QDialog, QMessageBox
from PySide6.QtCore import Signal, Slot
from .ui_spool_widget import Ui_SpoolWidget 
from ..dialogs.dialog_addSpool import addSpool


class SpoolWidget(QWidget):

    szpulRequest = Signal(int)
    spoolLengthChange = Signal(int, int)
    def __init__(self, index: int):
        super().__init__()

        ############# Główne przypisania #############
        self.ui = Ui_SpoolWidget()
        self.ui.setupUi(self)
        self.index = index
        self.addSpool = addSpool(index)
        self.Qdialog = QDialog()

        ############# Przypisania tekstów #############

        self.ui.label.setText("Załadowana szpula:")
        self.ui.addSpoolButton.setText(f"Dodaj informacje o szpuli {index}")
        self.ui.producerLabel.setText("Producent szpuli:     ")
        self.ui.colorLabel.setText("Color szpuli:     ")
        self.ui.lenghtLabel.setText("Długość szpuli:     ")

        ############# Filament changing #############
        self.ui.changeButton.clicked.connect(self._onChangeButtonClick)
        self.ui.frame.setTitle(f"Szpula filamentu nr: {index}")
        
        ############# Add Spool #############
        self.ui.addSpoolButton.clicked.connect(self._openDialogAddSpool)

        self.addSpool.Ok.connect(self._on_ok_clicked)
        self.addSpool.Cancel.connect(self._on_cancel_clicked)

    @Slot()
    def _on_ok_clicked(self):
        if self.addSpool.getSpoolProducer() is not None:
            self.ui.producerLabel.setText(self.addSpool.producer)
        if self.addSpool.getSpoolcolor() is not None:
            self.ui.colorLabel.setText(self.addSpool.color)
        try:
            length = self.addSpool.getSpoolLength()
        except Exception as error:
            dialog = QMessageBox()
            dialog.setWindowTitle("Błąd")
            dialog.setIcon(QMessageBox.Icon.Critical)
            dialog.setText("Podaj długość szpuli jako liczba")
            self.addSpool.show()
            dialog.exec()
        
        if length is not None:
            self.ui.lenghtLabel.setText(self.addSpool.lenght)
            self.spoolLengthChange.emit(self.index, length)  
    @Slot()
    def _on_cancel_clicked(self):
        self.addSpool.close()

    @Slot()
    def _onChangeButtonClick(self):
        self.szpulRequest.emit(self.index)

    @Slot()
    def _openDialogAddSpool(self):
        self.addSpool.show()

