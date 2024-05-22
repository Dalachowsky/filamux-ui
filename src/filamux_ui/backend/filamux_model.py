
from PySide6.QtCore import Signal, QObject

class FilamuxModel(QObject):

    spoolChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self._currentSpool = 0

    @property
    def currentSpool(self):
        return self._currentSpool

    @currentSpool.setter
    def currentSpool(self, value: int):
        if self._currentSpool != value:
            self._currentSpool = value
            self.spoolChanged.emit(value)
