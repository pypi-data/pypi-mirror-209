# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QPropertyFrame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

from sknrf.widget.propertybrowser.view.base import PropertyScrollArea

class Ui_propertyFrame(object):
    def setupUi(self, propertyFrame):
        if not propertyFrame.objectName():
            propertyFrame.setObjectName(u"propertyFrame")
        propertyFrame.resize(400, 300)
        propertyFrame.setFrameShape(QFrame.WinPanel)
        propertyFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(propertyFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.propertyTabWidget = QTabWidget(propertyFrame)
        self.propertyTabWidget.setObjectName(u"propertyTabWidget")
        self.propertyTab = QWidget()
        self.propertyTab.setObjectName(u"propertyTab")
        self.verticalLayout_5 = QVBoxLayout(self.propertyTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.propertyTable = PropertyScrollArea(self.propertyTab)
        self.propertyTable.setObjectName(u"propertyTable")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propertyTable.sizePolicy().hasHeightForWidth())
        self.propertyTable.setSizePolicy(sizePolicy)
        self.propertyTable.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.propertyTable)

        self.propertyTabWidget.addTab(self.propertyTab, "")
        self.limitTab = QWidget()
        self.limitTab.setObjectName(u"limitTab")
        self.verticalLayout_6 = QVBoxLayout(self.limitTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 694, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.propertyTabWidget.addTab(self.limitTab, "")
        self.optimizationTab = QWidget()
        self.optimizationTab.setObjectName(u"optimizationTab")
        self.verticalLayout_8 = QVBoxLayout(self.optimizationTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 694, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.propertyTabWidget.addTab(self.optimizationTab, "")
        self.displayTab = QWidget()
        self.displayTab.setObjectName(u"displayTab")
        self.verticalLayout_9 = QVBoxLayout(self.displayTab)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 694, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.propertyTabWidget.addTab(self.displayTab, "")

        self.verticalLayout.addWidget(self.propertyTabWidget)


        self.retranslateUi(propertyFrame)

        self.propertyTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(propertyFrame)
    # setupUi

    def retranslateUi(self, propertyFrame):
        propertyFrame.setWindowTitle(QCoreApplication.translate("propertyFrame", u"Frame", None))
#if QT_CONFIG(tooltip)
        self.propertyTable.setToolTip(QCoreApplication.translate("propertyFrame", u"Property Browser", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.propertyTable.setWhatsThis(QCoreApplication.translate("propertyFrame", u"The Property Browser Controls Table Properties", None))
#endif // QT_CONFIG(whatsthis)
        self.propertyTabWidget.setTabText(self.propertyTabWidget.indexOf(self.propertyTab), QCoreApplication.translate("propertyFrame", u"Properties", None))
        self.propertyTabWidget.setTabText(self.propertyTabWidget.indexOf(self.limitTab), QCoreApplication.translate("propertyFrame", u"Limits", None))
        self.propertyTabWidget.setTabText(self.propertyTabWidget.indexOf(self.optimizationTab), QCoreApplication.translate("propertyFrame", u"Optimization", None))
        self.propertyTabWidget.setTabText(self.propertyTabWidget.indexOf(self.displayTab), QCoreApplication.translate("propertyFrame", u"Display", None))
    # retranslateUi

