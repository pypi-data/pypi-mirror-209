# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QLauncher.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QFrame,
    QGridLayout, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_launcherFrame(object):
    def setupUi(self, launcherFrame):
        if not launcherFrame.objectName():
            launcherFrame.setObjectName(u"launcherFrame")
        launcherFrame.resize(803, 551)
        launcherFrame.setFrameShape(QFrame.StyledPanel)
        launcherFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(launcherFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.iconGridLayout = QGridLayout()
        self.iconGridLayout.setObjectName(u"iconGridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.iconGridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.iconGridLayout)

        self.buttonBox = QDialogButtonBox(launcherFrame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Open)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(launcherFrame)

        QMetaObject.connectSlotsByName(launcherFrame)
    # setupUi

    def retranslateUi(self, launcherFrame):
        launcherFrame.setWindowTitle(QCoreApplication.translate("launcherFrame", u"Frame", None))
    # retranslateUi

