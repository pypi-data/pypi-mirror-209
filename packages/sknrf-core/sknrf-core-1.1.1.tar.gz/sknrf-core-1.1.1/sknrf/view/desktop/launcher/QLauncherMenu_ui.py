# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QLauncherMenu.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_launcherMenu(object):
    def setupUi(self, launcherMenu):
        if not launcherMenu.objectName():
            launcherMenu.setObjectName(u"launcherMenu")
        launcherMenu.resize(800, 600)
        self.centralwidget = QWidget(launcherMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        launcherMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(launcherMenu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        launcherMenu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(launcherMenu)
        self.statusbar.setObjectName(u"statusbar")
        launcherMenu.setStatusBar(self.statusbar)

        self.retranslateUi(launcherMenu)

        QMetaObject.connectSlotsByName(launcherMenu)
    # setupUi

    def retranslateUi(self, launcherMenu):
        launcherMenu.setWindowTitle(QCoreApplication.translate("launcherMenu", u"MainWindow", None))
    # retranslateUi

