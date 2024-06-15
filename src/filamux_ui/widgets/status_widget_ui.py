# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'status_widget.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_StatusWidget(object):
    def setupUi(self, StatusWidget):
        if not StatusWidget.objectName():
            StatusWidget.setObjectName(u"StatusWidget")
        StatusWidget.resize(400, 300)
        self.gridLayout = QGridLayout(StatusWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(StatusWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(6)
        self.statusXchange = QLabel(self.groupBox)
        self.statusXchange.setObjectName(u"statusXchange")

        self.gridLayout_2.addWidget(self.statusXchange, 1, 1, 1, 1)

        self.status = QLabel(self.groupBox)
        self.status.setObjectName(u"status")

        self.gridLayout_2.addWidget(self.status, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.currentSpool = QLabel(self.groupBox)
        self.currentSpool.setObjectName(u"currentSpool")

        self.gridLayout_2.addWidget(self.currentSpool, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(StatusWidget)

        QMetaObject.connectSlotsByName(StatusWidget)
    # setupUi

    def retranslateUi(self, StatusWidget):
        StatusWidget.setWindowTitle(QCoreApplication.translate("StatusWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("StatusWidget", u"Status", None))
        self.statusXchange.setText("")
        self.status.setText("")
        self.label.setText(QCoreApplication.translate("StatusWidget", u"Status:", None))
        self.label_3.setText(QCoreApplication.translate("StatusWidget", u"Status xchange:", None))
        self.currentSpool.setText("")
        self.label_4.setText(QCoreApplication.translate("StatusWidget", u"Aktualna szpula:", None))
    # retranslateUi

