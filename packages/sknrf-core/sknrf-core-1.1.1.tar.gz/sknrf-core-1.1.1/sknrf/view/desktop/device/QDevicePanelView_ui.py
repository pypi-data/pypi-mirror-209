# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDevicePanelView.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from sknrf.widget.propertybrowser.view.base import PropertyScrollArea

class Ui_devicePanelView(object):
    def setupUi(self, devicePanelView):
        if not devicePanelView.objectName():
            devicePanelView.setObjectName(u"devicePanelView")
        devicePanelView.resize(475, 131)
        devicePanelView.setFrameShape(QFrame.WinPanel)
        devicePanelView.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(devicePanelView)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.menuButton = QPushButton(devicePanelView)
        self.menuButton.setObjectName(u"menuButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
        self.menuButton.setMinimumSize(QSize(64, 64))
        self.menuButton.setMaximumSize(QSize(256, 256))
        font = QFont()
        font.setPointSize(23)
        self.menuButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/PNG/64/rfsource.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(50, 50))
        self.menuButton.setFlat(False)

        self.verticalLayout.addWidget(self.menuButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.onButton = QPushButton(devicePanelView)
        self.onButton.setObjectName(u"onButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.onButton.sizePolicy().hasHeightForWidth())
        self.onButton.setSizePolicy(sizePolicy1)
        self.onButton.setMinimumSize(QSize(50, 32))
        self.onButton.setMaximumSize(QSize(50, 32))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.onButton.setFont(font1)
        self.onButton.setAutoFillBackground(False)
        self.onButton.setStyleSheet(u"QPushButton#onButton {color: black; background-color: grey }")
        self.onButton.setFlat(False)

        self.horizontalLayout.addWidget(self.onButton)

        self.offButton = QPushButton(devicePanelView)
        self.offButton.setObjectName(u"offButton")
        sizePolicy1.setHeightForWidth(self.offButton.sizePolicy().hasHeightForWidth())
        self.offButton.setSizePolicy(sizePolicy1)
        self.offButton.setMinimumSize(QSize(50, 32))
        self.offButton.setMaximumSize(QSize(50, 32))
        self.offButton.setFont(font1)
        self.offButton.setAutoFillBackground(False)
        self.offButton.setStyleSheet(u"QPushButton#offButton { color: white; background-color: red }")
        self.offButton.setFlat(False)

        self.horizontalLayout.addWidget(self.offButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.propertyTable = PropertyScrollArea(devicePanelView)
        self.propertyTable.setObjectName(u"propertyTable")
        self.propertyTable.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.propertyTable)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.retranslateUi(devicePanelView)

        QMetaObject.connectSlotsByName(devicePanelView)
    # setupUi

    def retranslateUi(self, devicePanelView):
        devicePanelView.setWindowTitle(QCoreApplication.translate("devicePanelView", u"Frame", None))
        self.menuButton.setText("")
        self.onButton.setText(QCoreApplication.translate("devicePanelView", u"ON", None))
        self.offButton.setText(QCoreApplication.translate("devicePanelView", u"OFF", None))
#if QT_CONFIG(tooltip)
        self.propertyTable.setToolTip(QCoreApplication.translate("devicePanelView", u"Property Browser", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.propertyTable.setWhatsThis(QCoreApplication.translate("devicePanelView", u"The Property Browser Controls Table Properties", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

