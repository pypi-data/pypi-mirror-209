# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QObjectDialog.ui'
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
    QFrame, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_objectDialog(object):
    def setupUi(self, objectDialog):
        if not objectDialog.objectName():
            objectDialog.setObjectName(u"objectDialog")
        objectDialog.resize(362, 362)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(objectDialog.sizePolicy().hasHeightForWidth())
        objectDialog.setSizePolicy(sizePolicy)
        objectDialog.setSizeGripEnabled(True)
        objectDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(objectDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.moduleFrame = QFrame(objectDialog)
        self.moduleFrame.setObjectName(u"moduleFrame")
        self.moduleFrame.setFrameShape(QFrame.WinPanel)
        self.moduleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.moduleFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.moduleLabel = QLabel(self.moduleFrame)
        self.moduleLabel.setObjectName(u"moduleLabel")

        self.gridLayout.addWidget(self.moduleLabel, 0, 0, 1, 1)

        self.moduleLineEdit = QLineEdit(self.moduleFrame)
        self.moduleLineEdit.setObjectName(u"moduleLineEdit")
        self.moduleLineEdit.setEnabled(False)
        self.moduleLineEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.moduleLineEdit, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.moduleFrame)

        self.returnFrame = QFrame(objectDialog)
        self.returnFrame.setObjectName(u"returnFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.returnFrame.sizePolicy().hasHeightForWidth())
        self.returnFrame.setSizePolicy(sizePolicy1)
        self.returnFrame.setFrameShape(QFrame.WinPanel)
        self.returnFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.returnFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.returnLabel = QLabel(self.returnFrame)
        self.returnLabel.setObjectName(u"returnLabel")

        self.gridLayout_2.addWidget(self.returnLabel, 0, 0, 1, 1)

        self.returnLineEdit = QLineEdit(self.returnFrame)
        self.returnLineEdit.setObjectName(u"returnLineEdit")

        self.gridLayout_2.addWidget(self.returnLineEdit, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.returnFrame)

        self.argumentFrame = QFrame(objectDialog)
        self.argumentFrame.setObjectName(u"argumentFrame")
        self.argumentFrame.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.argumentFrame.sizePolicy().hasHeightForWidth())
        self.argumentFrame.setSizePolicy(sizePolicy2)
        self.argumentFrame.setFrameShape(QFrame.WinPanel)
        self.argumentFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.argumentFrame)

        self.buttonBox = QDialogButtonBox(objectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.moduleLineEdit, self.returnLineEdit)
        QWidget.setTabOrder(self.returnLineEdit, self.buttonBox)

        self.retranslateUi(objectDialog)
        self.buttonBox.accepted.connect(objectDialog.accept)
        self.buttonBox.rejected.connect(objectDialog.reject)

        QMetaObject.connectSlotsByName(objectDialog)
    # setupUi

    def retranslateUi(self, objectDialog):
        objectDialog.setWindowTitle(QCoreApplication.translate("objectDialog", u"Dialog", None))
        self.moduleLabel.setText(QCoreApplication.translate("objectDialog", u"Module: ", None))
        self.moduleLineEdit.setText("")
        self.returnLabel.setText(QCoreApplication.translate("objectDialog", u"Return: ", None))
    # retranslateUi

