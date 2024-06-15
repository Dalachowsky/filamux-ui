# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_connect.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_DialogConnect(object):
    def setupUi(self, DialogConnect):
        if not DialogConnect.objectName():
            DialogConnect.setObjectName(u"DialogConnect")
        DialogConnect.setWindowModality(Qt.ApplicationModal)
        DialogConnect.resize(343, 195)
        self.gridLayout_2 = QGridLayout(DialogConnect)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.paramsBox = QGroupBox(DialogConnect)
        self.paramsBox.setObjectName(u"paramsBox")
        self.gridLayout = QGridLayout(self.paramsBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(12)
        self.baudrateLabel = QLabel(self.paramsBox)
        self.baudrateLabel.setObjectName(u"baudrateLabel")
        self.baudrateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.baudrateLabel, 0, 0, 1, 1)

        self.portLabel = QLabel(self.paramsBox)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.portLabel, 1, 0, 1, 1)

        self.portValue = QLineEdit(self.paramsBox)
        self.portValue.setObjectName(u"portValue")

        self.gridLayout.addWidget(self.portValue, 1, 1, 1, 1)

        self.baudrateSelector = QComboBox(self.paramsBox)
        self.baudrateSelector.setObjectName(u"baudrateSelector")

        self.gridLayout.addWidget(self.baudrateSelector, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.paramsBox, 0, 0, 1, 1)

        self.connectButton = QPushButton(DialogConnect)
        self.connectButton.setObjectName(u"connectButton")

        self.gridLayout_2.addWidget(self.connectButton, 1, 0, 1, 1)


        self.retranslateUi(DialogConnect)

        QMetaObject.connectSlotsByName(DialogConnect)
    # setupUi

    def retranslateUi(self, DialogConnect):
        DialogConnect.setWindowTitle(QCoreApplication.translate("DialogConnect", u"Dialog", None))
        self.paramsBox.setTitle(QCoreApplication.translate("DialogConnect", u"Parametry", None))
        self.baudrateLabel.setText(QCoreApplication.translate("DialogConnect", u"Baudrate", None))
        self.portLabel.setText(QCoreApplication.translate("DialogConnect", u"Port", None))
        self.portValue.setText(QCoreApplication.translate("DialogConnect", u"COM3", None))
        self.connectButton.setText(QCoreApplication.translate("DialogConnect", u"Po\u0142\u0105cz", None))
    # retranslateUi

