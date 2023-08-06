# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QLogSideView.ui'
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
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
class Ui_logFrame(object):
    def setupUi(self, logFrame):
        if not logFrame.objectName():
            logFrame.setObjectName(u"logFrame")
        logFrame.resize(462, 300)
        logFrame.setFrameShape(QFrame.StyledPanel)
        logFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(logFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.clearButton = QPushButton(logFrame)
        self.clearButton.setObjectName(u"clearButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/PNG/black/32/document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearButton.setIcon(icon)

        self.gridLayout.addWidget(self.clearButton, 1, 2, 1, 1)

        self.levelComboBox = QComboBox(logFrame)
        icon1 = QIcon()
        icon1.addFile(u":/PNG/black/32/bug.png", QSize(), QIcon.Normal, QIcon.On)
        self.levelComboBox.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/PNG/green/32/information.png", QSize(), QIcon.Normal, QIcon.Off)
        self.levelComboBox.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/PNG/orange/32/warning.png", QSize(), QIcon.Normal, QIcon.Off)
        self.levelComboBox.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/PNG/red/32/exclamation_mark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.levelComboBox.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/PNG/magenta/32/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.levelComboBox.addItem(icon5, "")
        self.levelComboBox.setObjectName(u"levelComboBox")

        self.gridLayout.addWidget(self.levelComboBox, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(logFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 434, 210))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 4, 0, 1, 3)

        self.levelLabel = QLabel(logFrame)
        self.levelLabel.setObjectName(u"levelLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.levelLabel.sizePolicy().hasHeightForWidth())
        self.levelLabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.levelLabel, 1, 0, 1, 1)

        self.label = QLabel(logFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.levelLabel.setBuddy(self.levelComboBox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.textEdit, self.scrollArea)

        self.retranslateUi(logFrame)
        self.clearButton.clicked.connect(self.textEdit.clear)

        QMetaObject.connectSlotsByName(logFrame)
    # setupUi

    def retranslateUi(self, logFrame):
        logFrame.setWindowTitle(QCoreApplication.translate("logFrame", u"Frame", None))
#if QT_CONFIG(tooltip)
        self.clearButton.setToolTip(QCoreApplication.translate("logFrame", u"Clear", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.clearButton.setStatusTip(QCoreApplication.translate("logFrame", u"Clear", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.clearButton.setWhatsThis(QCoreApplication.translate("logFrame", u"Clear Log", None))
#endif // QT_CONFIG(whatsthis)
        self.clearButton.setText("")
        self.levelComboBox.setItemText(0, QCoreApplication.translate("logFrame", u"Debug", None))
        self.levelComboBox.setItemText(1, QCoreApplication.translate("logFrame", u"Info", None))
        self.levelComboBox.setItemText(2, QCoreApplication.translate("logFrame", u"Warning", None))
        self.levelComboBox.setItemText(3, QCoreApplication.translate("logFrame", u"Error", None))
        self.levelComboBox.setItemText(4, QCoreApplication.translate("logFrame", u"Critical", None))

        self.textEdit.setHtml(QCoreApplication.translate("logFrame", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'.Helvetica Neue DeskInterface';\"><br /></p></body></html>", None))
        self.levelLabel.setText(QCoreApplication.translate("logFrame", u"Level:", None))
        self.label.setText(QCoreApplication.translate("logFrame", u"Log:", None))
    # retranslateUi

