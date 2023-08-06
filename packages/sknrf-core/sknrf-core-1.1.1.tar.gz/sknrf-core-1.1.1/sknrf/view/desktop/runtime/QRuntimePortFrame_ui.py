# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QRuntimePortFrame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from sknrf.app.dataviewer.view.figure import ContentFigure

class Ui_runtimePortFrame(object):
    def setupUi(self, runtimePortFrame):
        if not runtimePortFrame.objectName():
            runtimePortFrame.setObjectName(u"runtimePortFrame")
        runtimePortFrame.resize(780, 931)
        runtimePortFrame.setFrameShape(QFrame.WinPanel)
        runtimePortFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(runtimePortFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.portLabel = QLabel(runtimePortFrame)
        self.portLabel.setObjectName(u"portLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLabel.sizePolicy().hasHeightForWidth())
        self.portLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        self.portLabel.setFont(font)
        self.portLabel.setStyleSheet(u"")
        self.portLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.portLabel)

        self.meterFrame = QFrame(runtimePortFrame)
        self.meterFrame.setObjectName(u"meterFrame")
        self.meterFrame.setFrameShape(QFrame.StyledPanel)
        self.meterFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.meterFrame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.meterFrame)

        self.previewPlotWidget = ContentFigure(runtimePortFrame)
        self.previewPlotWidget.setObjectName(u"previewPlotWidget")
        self.previewPlotWidget.setEnabled(True)

        self.verticalLayout.addWidget(self.previewPlotWidget)


        self.retranslateUi(runtimePortFrame)

        QMetaObject.connectSlotsByName(runtimePortFrame)
    # setupUi

    def retranslateUi(self, runtimePortFrame):
        runtimePortFrame.setWindowTitle(QCoreApplication.translate("runtimePortFrame", u"Frame", None))
        self.portLabel.setText(QCoreApplication.translate("runtimePortFrame", u"Port 1:", None))
    # retranslateUi

