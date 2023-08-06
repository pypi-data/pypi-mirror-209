# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QDeviceMenuView.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QToolBar,
    QWidget)

class Ui_deviceMenuView(object):
    def setupUi(self, deviceMenuView):
        if not deviceMenuView.objectName():
            deviceMenuView.setObjectName(u"deviceMenuView")
        deviceMenuView.resize(1600, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(deviceMenuView.sizePolicy().hasHeightForWidth())
        deviceMenuView.setSizePolicy(sizePolicy)
        deviceMenuView.setMinimumSize(QSize(1600, 900))
        deviceMenuView.setMaximumSize(QSize(2880, 1800))
        deviceMenuView.setTabShape(QTabWidget.Rounded)
        self.actionDocumentation = QAction(deviceMenuView)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        icon = QIcon(QIcon.fromTheme(u"help-about"))
        self.actionDocumentation.setIcon(icon)
        self.actionSingle = QAction(deviceMenuView)
        self.actionSingle.setObjectName(u"actionSingle")
        icon1 = QIcon()
        icon1.addFile(u":/PNG/black/32/circled_border_triangle_right.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/PNG/green/32/circled_border_triangle_right.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionSingle.setIcon(icon1)
        self.centralwidget = QWidget(deviceMenuView)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(2880, 1800))
        self.centralwidget.setSizeIncrement(QSize(0, 0))
        deviceMenuView.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(deviceMenuView)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1600, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        deviceMenuView.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(deviceMenuView)
        self.statusbar.setObjectName(u"statusbar")
        deviceMenuView.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(deviceMenuView)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        deviceMenuView.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuRun.addAction(self.actionSingle)
        self.toolBar.addAction(self.actionDocumentation)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSingle)

        self.retranslateUi(deviceMenuView)

        QMetaObject.connectSlotsByName(deviceMenuView)
    # setupUi

    def retranslateUi(self, deviceMenuView):
        deviceMenuView.setWindowTitle(QCoreApplication.translate("deviceMenuView", u"Device Menu", None))
        self.actionDocumentation.setText(QCoreApplication.translate("deviceMenuView", u"Documentation", None))
        self.actionSingle.setText(QCoreApplication.translate("deviceMenuView", u"Single", None))
        self.menuHelp.setTitle(QCoreApplication.translate("deviceMenuView", u"Help", None))
        self.menuRun.setTitle(QCoreApplication.translate("deviceMenuView", u"Run", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("deviceMenuView", u"toolBar", None))
    # retranslateUi

