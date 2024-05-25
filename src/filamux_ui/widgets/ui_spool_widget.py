# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spool_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QPushButton,
    QSizePolicy, QWidget)

class Ui_SpoolWidget(object):
    def setupUi(self, SpoolWidget):
        if not SpoolWidget.objectName():
            SpoolWidget.setObjectName(u"SpoolWidget")
        SpoolWidget.resize(400, 300)
        self.gridLayout = QGridLayout(SpoolWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QGroupBox(SpoolWidget)
        self.frame.setObjectName(u"frame")
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.changeButton = QPushButton(self.frame)
        self.changeButton.setObjectName(u"changeButton")

        self.gridLayout_3.addWidget(self.changeButton, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(SpoolWidget)

        QMetaObject.connectSlotsByName(SpoolWidget)
    # setupUi

    def retranslateUi(self, SpoolWidget):
        SpoolWidget.setWindowTitle(QCoreApplication.translate("SpoolWidget", u"Form", None))
        self.frame.setTitle(QCoreApplication.translate("SpoolWidget", u"NUMER_SZPULI", None))
        self.changeButton.setText(QCoreApplication.translate("SpoolWidget", u"Zmie\u0144", None))
    # retranslateUi

