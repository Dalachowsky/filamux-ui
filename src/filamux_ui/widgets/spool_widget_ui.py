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
    QPushButton, QSizePolicy, QWidget)

class Ui_SpoolWidget(object):
    def setupUi(self, SpoolWidget):
        if not SpoolWidget.objectName():
            SpoolWidget.setObjectName(u"SpoolWidget")
        SpoolWidget.resize(417, 351)
        self.gridLayout = QGridLayout(SpoolWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QGroupBox(SpoolWidget)
        self.frame.setObjectName(u"frame")
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.changeButton = QPushButton(self.frame)
        self.changeButton.setObjectName(u"changeButton")

        self.gridLayout_3.addWidget(self.changeButton, 2, 0, 1, 1)

        self.lenghtLabel = QLabel(self.frame)
        self.lenghtLabel.setObjectName(u"lenghtLabel")

        self.gridLayout_3.addWidget(self.lenghtLabel, 7, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 4, 0, 1, 1)

        self.addSpoolButton = QPushButton(self.frame)
        self.addSpoolButton.setObjectName(u"addSpoolButton")

        self.gridLayout_3.addWidget(self.addSpoolButton, 3, 0, 1, 1)

        self.producerLabel = QLabel(self.frame)
        self.producerLabel.setObjectName(u"producerLabel")

        self.gridLayout_3.addWidget(self.producerLabel, 5, 0, 1, 1)

        self.colorLabel = QLabel(self.frame)
        self.colorLabel.setObjectName(u"colorLabel")

        self.gridLayout_3.addWidget(self.colorLabel, 6, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.label_5 = QLabel(SpoolWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)


        self.retranslateUi(SpoolWidget)

        QMetaObject.connectSlotsByName(SpoolWidget)
    # setupUi

    def retranslateUi(self, SpoolWidget):
        SpoolWidget.setWindowTitle(QCoreApplication.translate("SpoolWidget", u"Form", None))
        self.frame.setTitle(QCoreApplication.translate("SpoolWidget", u"NUMER_SZPULI", None))
        self.changeButton.setText(QCoreApplication.translate("SpoolWidget", u"Change on spool", None))
        self.lenghtLabel.setText(QCoreApplication.translate("SpoolWidget", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("SpoolWidget", u"TextLabel", None))
        self.addSpoolButton.setText(QCoreApplication.translate("SpoolWidget", u"ADD Spool", None))
        self.producerLabel.setText(QCoreApplication.translate("SpoolWidget", u"TextLabel", None))
        self.colorLabel.setText(QCoreApplication.translate("SpoolWidget", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("SpoolWidget", u"TextLabel", None))
    # retranslateUi

