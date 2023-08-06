# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QLauncherSideView.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QSplitter,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_launcherSideViewFrame(object):
    def setupUi(self, launcherSideViewFrame):
        if not launcherSideViewFrame.objectName():
            launcherSideViewFrame.setObjectName(u"launcherSideViewFrame")
        launcherSideViewFrame.resize(516, 670)
        launcherSideViewFrame.setFrameShape(QFrame.StyledPanel)
        launcherSideViewFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(launcherSideViewFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_5 = QSplitter(launcherSideViewFrame)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Vertical)
        self.actionTabWidget = QTabWidget(self.splitter_5)
        self.actionTabWidget.setObjectName(u"actionTabWidget")
        self.splitter_5.addWidget(self.actionTabWidget)
        self.infoEdit = QTextEdit(self.splitter_5)
        self.infoEdit.setObjectName(u"infoEdit")
        self.infoEdit.setEnabled(True)
        font = QFont()
        font.setPointSize(15)
        self.infoEdit.setFont(font)
        self.infoEdit.setReadOnly(True)
        self.splitter_5.addWidget(self.infoEdit)

        self.verticalLayout.addWidget(self.splitter_5)


        self.retranslateUi(launcherSideViewFrame)

        self.actionTabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(launcherSideViewFrame)
    # setupUi

    def retranslateUi(self, launcherSideViewFrame):
        launcherSideViewFrame.setWindowTitle(QCoreApplication.translate("launcherSideViewFrame", u"Frame", None))
    # retranslateUi

