# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QCalibration.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget, QWizard)
class Ui_calibrationWizard(object):
    def setupUi(self, calibrationWizard):
        if not calibrationWizard.objectName():
            calibrationWizard.setObjectName(u"calibrationWizard")
        calibrationWizard.resize(501, 300)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(calibrationWizard.sizePolicy().hasHeightForWidth())
        calibrationWizard.setSizePolicy(sizePolicy)
        calibrationWizard.setMaximumSize(QSize(600, 300))
        calibrationWizard.setModal(False)
        calibrationWizard.setWizardStyle(QWizard.ModernStyle)
        calibrationWizard.setOptions(QWizard.HaveCustomButton1|QWizard.HaveHelpButton|QWizard.IndependentPages|QWizard.NoBackButtonOnStartPage)
        calibrationWizard.setSubTitleFormat(Qt.RichText)

        self.retranslateUi(calibrationWizard)

        QMetaObject.connectSlotsByName(calibrationWizard)
    # setupUi

    def retranslateUi(self, calibrationWizard):
        calibrationWizard.setWindowTitle(QCoreApplication.translate("calibrationWizard", u"Calibration", None))
    # retranslateUi

