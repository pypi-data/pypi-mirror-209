# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QProgressFrame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QScrollArea,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_progressFrame(object):
    def setupUi(self, progressFrame):
        if not progressFrame.objectName():
            progressFrame.setObjectName(u"progressFrame")
        progressFrame.resize(517, 827)
        progressFrame.setFrameShape(QFrame.WinPanel)
        progressFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(progressFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progressLabel = QLabel(progressFrame)
        self.progressLabel.setObjectName(u"progressLabel")
        font = QFont()
        font.setBold(True)
        self.progressLabel.setFont(font)
        self.progressLabel.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.progressLabel)

        self.tabWidget = QTabWidget(progressFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.sweepTab = QWidget()
        self.sweepTab.setObjectName(u"sweepTab")
        self.verticalLayout = QVBoxLayout(self.sweepTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.sweepTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 481, 742))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.sweepTab, "")
        self.optimizationTab = QWidget()
        self.optimizationTab.setObjectName(u"optimizationTab")
        self.tabWidget.addTab(self.optimizationTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(progressFrame)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(progressFrame)
    # setupUi

    def retranslateUi(self, progressFrame):
        progressFrame.setWindowTitle(QCoreApplication.translate("progressFrame", u"Frame", None))
        self.progressLabel.setText(QCoreApplication.translate("progressFrame", u"Progress:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sweepTab), QCoreApplication.translate("progressFrame", u"Sweep", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optimizationTab), QCoreApplication.translate("progressFrame", u"Optimization", None))
    # retranslateUi

