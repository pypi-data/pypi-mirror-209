# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QBusyFrame.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qprogressindicator import QProgressIndicator

class Ui_busyFrame(object):
    def setupUi(self, busyFrame):
        if not busyFrame.objectName():
            busyFrame.setObjectName(u"busyFrame")
        busyFrame.resize(400, 300)
        font = QFont()
        font.setBold(True)
        busyFrame.setFont(font)
        busyFrame.setAutoFillBackground(False)
        busyFrame.setStyleSheet(u"")
        busyFrame.setFrameShape(QFrame.NoFrame)
        busyFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(busyFrame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.busyIndicator = QProgressIndicator(busyFrame)
        self.busyIndicator.setObjectName(u"busyIndicator")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.busyIndicator.sizePolicy().hasHeightForWidth())
        self.busyIndicator.setSizePolicy(sizePolicy)
        self.busyIndicator.setMaximumSize(QSize(250, 250))
        self.busyIndicator.setProperty("displayedWhenStopped", True)

        self.horizontalLayout_2.addWidget(self.busyIndicator)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(busyFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(busyFrame)

        QMetaObject.connectSlotsByName(busyFrame)
    # setupUi

    def retranslateUi(self, busyFrame):
        busyFrame.setWindowTitle(QCoreApplication.translate("busyFrame", u"Frame", None))
#if QT_CONFIG(tooltip)
        self.busyIndicator.setToolTip(QCoreApplication.translate("busyFrame", u"Progress Indicator", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.busyIndicator.setWhatsThis(QCoreApplication.translate("busyFrame", u"The Progress Indicator indicates the system is busy", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("busyFrame", u"Loading...", None))
    # retranslateUi

