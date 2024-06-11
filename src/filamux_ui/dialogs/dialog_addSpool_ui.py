# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_addSpool.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 285)
        font = QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.label2 = QLabel(Dialog)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(20, 90, 271, 31))
        self.label3 = QLabel(Dialog)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(20, 160, 321, 31))
        self.label1 = QLabel(Dialog)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(20, 20, 261, 31))
        self.producerOfSpool = QLineEdit(Dialog)
        self.producerOfSpool.setObjectName(u"producerOfSpool")
        self.producerOfSpool.setGeometry(QRect(22, 60, 331, 31))
        self.colorOfSpool = QLineEdit(Dialog)
        self.colorOfSpool.setObjectName(u"colorOfSpool")
        self.colorOfSpool.setGeometry(QRect(20, 130, 331, 31))
        self.lenghtOfSpool = QLineEdit(Dialog)
        self.lenghtOfSpool.setObjectName(u"lenghtOfSpool")
        self.lenghtOfSpool.setGeometry(QRect(20, 200, 331, 31))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label2.setText(QCoreApplication.translate("Dialog", u"Color of the Spool", None))
        self.label3.setText(QCoreApplication.translate("Dialog", u"Lenght of the Spool", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"Producer of the Spool", None))
    # retranslateUi

