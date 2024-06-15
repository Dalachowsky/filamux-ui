# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extruder_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ExtruderWidget(object):
    def setupUi(self, ExtruderWidget):
        if not ExtruderWidget.objectName():
            ExtruderWidget.setObjectName(u"ExtruderWidget")
        ExtruderWidget.resize(592, 556)
        self.gridLayout = QGridLayout(ExtruderWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(ExtruderWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(6)
        self.feedDistance = QDoubleSpinBox(self.groupBox_2)
        self.feedDistance.setObjectName(u"feedDistance")
        self.feedDistance.setValue(5.000000000000000)

        self.gridLayout_2.addWidget(self.feedDistance, 1, 1, 1, 1)

        self.feedSpeed = QDoubleSpinBox(self.groupBox_2)
        self.feedSpeed.setObjectName(u"feedSpeed")
        self.feedSpeed.setSingleStep(0.500000000000000)
        self.feedSpeed.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.feedSpeed, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.feedButton = QPushButton(self.groupBox_2)
        self.feedButton.setObjectName(u"feedButton")

        self.gridLayout_3.addWidget(self.feedButton, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(ExtruderWidget)

        QMetaObject.connectSlotsByName(ExtruderWidget)
    # setupUi

    def retranslateUi(self, ExtruderWidget):
        ExtruderWidget.setWindowTitle(QCoreApplication.translate("ExtruderWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("ExtruderWidget", u"Extruder", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ExtruderWidget", u"Sterowanie r\u0119czne", None))
        self.label.setText(QCoreApplication.translate("ExtruderWidget", u"Pr\u0119dko\u015b\u0107 [mm/s]", None))
        self.label_2.setText(QCoreApplication.translate("ExtruderWidget", u"D\u0142ugo\u015b\u0107 [mm]", None))
        self.feedButton.setText(QCoreApplication.translate("ExtruderWidget", u"Wy\u015blij", None))
    # retranslateUi

