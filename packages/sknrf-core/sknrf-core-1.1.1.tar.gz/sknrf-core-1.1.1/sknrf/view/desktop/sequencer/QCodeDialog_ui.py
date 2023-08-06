# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QCodeDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QVBoxLayout, QWidget)

from sknrf.view.desktop.sequencer.code import CodeEditor

class Ui_codeDialog(object):
    def setupUi(self, codeDialog):
        if not codeDialog.objectName():
            codeDialog.setObjectName(u"codeDialog")
        codeDialog.resize(567, 560)
        codeDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(codeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.codePlainTextEdit = CodeEditor(codeDialog)
        self.codePlainTextEdit.setObjectName(u"codePlainTextEdit")
        self.codePlainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.codePlainTextEdit)

        self.buttonBox = QDialogButtonBox(codeDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(codeDialog)
        self.buttonBox.accepted.connect(codeDialog.accept)
        self.buttonBox.rejected.connect(codeDialog.reject)

        QMetaObject.connectSlotsByName(codeDialog)
    # setupUi

    def retranslateUi(self, codeDialog):
        codeDialog.setWindowTitle(QCoreApplication.translate("codeDialog", u"Sequencer Code", None))
    # retranslateUi

