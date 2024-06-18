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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SpoolWidget(object):
    def setupUi(self, SpoolWidget):
        if not SpoolWidget.objectName():
            SpoolWidget.setObjectName(u"SpoolWidget")
        SpoolWidget.resize(419, 672)
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

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.producerLabel = QLabel(self.frame)
        self.producerLabel.setObjectName(u"producerLabel")

        self.horizontalLayout_3.addWidget(self.producerLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.resetProducer = QPushButton(self.frame)
        self.resetProducer.setObjectName(u"resetProducer")

        self.horizontalLayout_3.addWidget(self.resetProducer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.colorLabel = QLabel(self.frame)
        self.colorLabel.setObjectName(u"colorLabel")

        self.horizontalLayout_2.addWidget(self.colorLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.resetColor = QPushButton(self.frame)
        self.resetColor.setObjectName(u"resetColor")

        self.horizontalLayout_2.addWidget(self.resetColor)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.lenghtLabel = QLabel(self.frame)
        self.lenghtLabel.setObjectName(u"lenghtLabel")

        self.horizontalLayout.addWidget(self.lenghtLabel)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.resetlenght = QPushButton(self.frame)
        self.resetlenght.setObjectName(u"resetlenght")

        self.horizontalLayout.addWidget(self.resetlenght)


        self.verticalLayout.addLayout(self.horizontalLayout)

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
        self.label_2.setText(QCoreApplication.translate("SpoolWidget", u"Producent Szpuli:", None))
        self.producerLabel.setText("")
        self.resetProducer.setText(QCoreApplication.translate("SpoolWidget", u"Reset", None))
        self.label_3.setText(QCoreApplication.translate("SpoolWidget", u"Color szpuli:", None))
        self.colorLabel.setText("")
        self.resetColor.setText(QCoreApplication.translate("SpoolWidget", u"Reset", None))
        self.label_4.setText(QCoreApplication.translate("SpoolWidget", u"D\u0142ugo\u015b\u0107 szpuli:", None))
        self.lenghtLabel.setText("")
        self.label_5.setText(QCoreApplication.translate("SpoolWidget", u"[m]", None))
        self.resetlenght.setText(QCoreApplication.translate("SpoolWidget", u"Reset", None))
        self.changeButton.setText(QCoreApplication.translate("SpoolWidget", u"Aktywuj", None))
    # retranslateUi

