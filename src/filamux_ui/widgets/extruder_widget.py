# ******************************************************************************************
# **  Copyright  2024             Michał Radomski                                         **
# **  All Rights Reserved         Politechnika śląska                                     **
# **                                                                                      **
# ******************************************************************************************

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from .ui_extruder_widget import Ui_ExtruderWidget 

class ExtruderWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ExtruderWidget()
        self.ui.setupUi(self)