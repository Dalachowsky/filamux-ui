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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SpoolWidget(object):
    def setupUi(self, SpoolWidget):
        if not SpoolWidget.objectName():
            SpoolWidget.setObjectName(u"SpoolWidget")
        SpoolWidget.resize(417, 672)
        self.gridLayout = QGridLayout(SpoolWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QGroupBox(SpoolWidget)
        self.frame.setObjectName(u"frame")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addSpoolButton = QPushButton(self.frame)
        self.addSpoolButton.setObjectName(u"addSpoolButton")

        self.verticalLayout.addWidget(self.addSpoolButton)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.producerLabel = QLabel(self.frame)
        self.producerLabel.setObjectName(u"producerLabel")

        self.verticalLayout.addWidget(self.producerLabel)

        self.colorLabel = QLabel(self.frame)
        self.colorLabel.setObjectName(u"colorLabel")

        self.verticalLayout.addWidget(self.colorLabel)

        self.lenghtLabel = QLabel(self.frame)
        self.lenghtLabel.setObjectName(u"lenghtLabel")

        self.verticalLayout.addWidget(self.lenghtLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.changeButton = QPushButton(self.frame)
        self.changeButton.setObjectName(u"changeButton")

        self.verticalLayout.addWidget(self.changeButton)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(SpoolWidget)

        QMetaObject.connectSlotsByName(SpoolWidget)
    # setupUi

    def retranslateUi(self, SpoolWidget):
        SpoolWidget.setWindowTitle(QCoreApplication.translate("SpoolWidget", u"Form", None))
        self.frame.setTitle(QCoreApplication.translate("SpoolWidget", u"NUMER_SZPULI", None))
        self.addSpoolButton.setText(QCoreApplication.translate("SpoolWidget", u"ADD Spool", None))
        self.label.setText(QCoreApplication.translate("SpoolWidget", u"Loaded Spool:", None))
        self.producerLabel.setText(QCoreApplication.translate("SpoolWidget", u"TextLabel", None))
        self.colorLabel.setText(QCoreApplication.translate("SpoolWidget", u"TextLabel", None))
        self.lenghtLabel.setText(QCoreApplication.translate("SpoolWidget", u"TextLabel", None))
        self.changeButton.setText(QCoreApplication.translate("SpoolWidget", u"Aktywuj", None))
    # retranslateUi

