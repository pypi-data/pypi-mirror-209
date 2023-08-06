# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDeviceLoadFrame.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

from sknrf.widget.propertybrowser.view.base import PropertyScrollArea

class Ui_deviceLoadFrame(object):
    def setupUi(self, deviceLoadFrame):
        if not deviceLoadFrame.objectName():
            deviceLoadFrame.setObjectName(u"deviceLoadFrame")
        deviceLoadFrame.setEnabled(True)
        deviceLoadFrame.resize(400, 544)
        deviceLoadFrame.setFrameShape(QFrame.WinPanel)
        deviceLoadFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(deviceLoadFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.imageLabel = QLabel(deviceLoadFrame)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QSize(128, 128))
        self.imageLabel.setMaximumSize(QSize(128, 128))
        self.imageLabel.setPixmap(QPixmap(u":/PNG/64/rfsource.png"))
        self.imageLabel.setScaledContents(True)

        self.gridLayout_2.addWidget(self.imageLabel, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.onButton = QPushButton(deviceLoadFrame)
        self.onButton.setObjectName(u"onButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.onButton.sizePolicy().hasHeightForWidth())
        self.onButton.setSizePolicy(sizePolicy1)
        self.onButton.setMinimumSize(QSize(64, 50))
        self.onButton.setMaximumSize(QSize(64, 50))
        font = QFont()
        font.setPointSize(28)
        self.onButton.setFont(font)
        self.onButton.setAutoFillBackground(False)
        self.onButton.setStyleSheet(u"QPushButton#onButton {color: black; background-color: grey }")
        self.onButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.onButton)

        self.offButton = QPushButton(deviceLoadFrame)
        self.offButton.setObjectName(u"offButton")
        sizePolicy1.setHeightForWidth(self.offButton.sizePolicy().hasHeightForWidth())
        self.offButton.setSizePolicy(sizePolicy1)
        self.offButton.setMinimumSize(QSize(64, 50))
        self.offButton.setMaximumSize(QSize(64, 50))
        self.offButton.setFont(font)
        self.offButton.setAutoFillBackground(False)
        self.offButton.setStyleSheet(u"QPushButton#offButton { color: white; background-color: red }")
        self.offButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.offButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.driverLabel = QLabel(deviceLoadFrame)
        self.driverLabel.setObjectName(u"driverLabel")

        self.verticalLayout.addWidget(self.driverLabel)

        self.driverComboBox = QComboBox(deviceLoadFrame)
        self.driverComboBox.setObjectName(u"driverComboBox")

        self.verticalLayout.addWidget(self.driverComboBox)

        self.addressTabWidget = QTabWidget(deviceLoadFrame)
        self.addressTabWidget.setObjectName(u"addressTabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.addressTabWidget.sizePolicy().hasHeightForWidth())
        self.addressTabWidget.setSizePolicy(sizePolicy2)
        self.addressTab = QWidget()
        self.addressTab.setObjectName(u"addressTab")
        self.verticalLayout_10 = QVBoxLayout(self.addressTab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.addressTable = PropertyScrollArea(self.addressTab)
        self.addressTable.setObjectName(u"addressTable")
        self.addressTable.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.addressTable.sizePolicy().hasHeightForWidth())
        self.addressTable.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.addressTable)

        self.addressTabWidget.addTab(self.addressTab, "")
        self.firmwareTab = QWidget()
        self.firmwareTab.setObjectName(u"firmwareTab")
        self.verticalLayout_11 = QVBoxLayout(self.firmwareTab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.firmwareTable = PropertyScrollArea(self.firmwareTab)
        self.firmwareTable.setObjectName(u"firmwareTable")
        sizePolicy2.setHeightForWidth(self.firmwareTable.sizePolicy().hasHeightForWidth())
        self.firmwareTable.setSizePolicy(sizePolicy2)

        self.verticalLayout_11.addWidget(self.firmwareTable)

        self.addressTabWidget.addTab(self.firmwareTab, "")

        self.verticalLayout.addWidget(self.addressTabWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.testButton = QPushButton(deviceLoadFrame)
        self.testButton.setObjectName(u"testButton")

        self.horizontalLayout_3.addWidget(self.testButton)

        self.loadDriverButton = QPushButton(deviceLoadFrame)
        self.loadDriverButton.setObjectName(u"loadDriverButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.loadDriverButton.sizePolicy().hasHeightForWidth())
        self.loadDriverButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.loadDriverButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

#if QT_CONFIG(shortcut)
        self.driverLabel.setBuddy(self.driverComboBox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.onButton, self.offButton)
        QWidget.setTabOrder(self.offButton, self.driverComboBox)
        QWidget.setTabOrder(self.driverComboBox, self.addressTabWidget)
        QWidget.setTabOrder(self.addressTabWidget, self.testButton)
        QWidget.setTabOrder(self.testButton, self.loadDriverButton)

        self.retranslateUi(deviceLoadFrame)

        self.addressTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(deviceLoadFrame)
    # setupUi

    def retranslateUi(self, deviceLoadFrame):
        deviceLoadFrame.setWindowTitle(QCoreApplication.translate("deviceLoadFrame", u"Frame", None))
        self.imageLabel.setText("")
        self.onButton.setText(QCoreApplication.translate("deviceLoadFrame", u"ON", None))
        self.offButton.setText(QCoreApplication.translate("deviceLoadFrame", u"OFF", None))
        self.driverLabel.setText(QCoreApplication.translate("deviceLoadFrame", u"Select Driver:", None))
#if QT_CONFIG(tooltip)
        self.addressTable.setToolTip(QCoreApplication.translate("deviceLoadFrame", u"Property Browser", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.addressTable.setWhatsThis(QCoreApplication.translate("deviceLoadFrame", u"The Property Browser Controls Table Properties", None))
#endif // QT_CONFIG(whatsthis)
        self.addressTabWidget.setTabText(self.addressTabWidget.indexOf(self.addressTab), QCoreApplication.translate("deviceLoadFrame", u"Address", None))
#if QT_CONFIG(tooltip)
        self.firmwareTable.setToolTip(QCoreApplication.translate("deviceLoadFrame", u"Property Browser", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.firmwareTable.setWhatsThis(QCoreApplication.translate("deviceLoadFrame", u"The Property Browser Controls Table Properties", None))
#endif // QT_CONFIG(whatsthis)
        self.addressTabWidget.setTabText(self.addressTabWidget.indexOf(self.firmwareTab), QCoreApplication.translate("deviceLoadFrame", u"Firmware", None))
        self.testButton.setText(QCoreApplication.translate("deviceLoadFrame", u"Test", None))
        self.loadDriverButton.setText(QCoreApplication.translate("deviceLoadFrame", u"Load", None))
    # retranslateUi

