# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QTransformDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from sknrf.widget.propertybrowser.view.base import PropertyScrollArea

class Ui_transformDialog(object):
    def setupUi(self, transformDialog):
        if not transformDialog.objectName():
            transformDialog.setObjectName(u"transformDialog")
        transformDialog.resize(824, 362)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(transformDialog.sizePolicy().hasHeightForWidth())
        transformDialog.setSizePolicy(sizePolicy)
        transformDialog.setSizeGripEnabled(True)
        transformDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(transformDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.transformFrame = QFrame(transformDialog)
        self.transformFrame.setObjectName(u"transformFrame")
        self.transformFrame.setFrameShape(QFrame.WinPanel)
        self.transformFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.transformFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.transformLabel = QLabel(self.transformFrame)
        self.transformLabel.setObjectName(u"transformLabel")

        self.gridLayout.addWidget(self.transformLabel, 0, 0, 1, 1)

        self.transformComboBox = QComboBox(self.transformFrame)
        self.transformComboBox.setObjectName(u"transformComboBox")

        self.gridLayout.addWidget(self.transformComboBox, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)

        self.verticalLayout.addWidget(self.transformFrame)

        self.previewFrame = QFrame(transformDialog)
        self.previewFrame.setObjectName(u"previewFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.previewFrame.sizePolicy().hasHeightForWidth())
        self.previewFrame.setSizePolicy(sizePolicy1)
        self.previewFrame.setFrameShape(QFrame.WinPanel)
        self.previewFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.previewFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 7)
        self.previewLabel = QLabel(self.previewFrame)
        self.previewLabel.setObjectName(u"previewLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.previewLabel.sizePolicy().hasHeightForWidth())
        self.previewLabel.setSizePolicy(sizePolicy2)
        self.previewLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.previewLabel.setScaledContents(False)
        self.previewLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.previewLabel, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.previewFrame)

        self.argumentFrame = QFrame(transformDialog)
        self.argumentFrame.setObjectName(u"argumentFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.argumentFrame.sizePolicy().hasHeightForWidth())
        self.argumentFrame.setSizePolicy(sizePolicy3)
        self.argumentFrame.setFrameShape(QFrame.WinPanel)
        self.argumentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.argumentFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.transformTable = PropertyScrollArea(self.argumentFrame)
        self.transformTable.setObjectName(u"transformTable")
        self.transformTable.setEnabled(True)

        self.verticalLayout_2.addWidget(self.transformTable)


        self.verticalLayout.addWidget(self.argumentFrame)

        self.buttonBox = QDialogButtonBox(transformDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(transformDialog)
        self.buttonBox.accepted.connect(transformDialog.accept)
        self.buttonBox.rejected.connect(transformDialog.reject)

        QMetaObject.connectSlotsByName(transformDialog)
    # setupUi

    def retranslateUi(self, transformDialog):
        transformDialog.setWindowTitle(QCoreApplication.translate("transformDialog", u"Dialog", None))
        self.transformLabel.setText(QCoreApplication.translate("transformDialog", u"Transform:", None))
        self.previewLabel.setText("")
#if QT_CONFIG(tooltip)
        self.transformTable.setToolTip(QCoreApplication.translate("transformDialog", u"Property Browser", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.transformTable.setWhatsThis(QCoreApplication.translate("transformDialog", u"The Property Browser Controls Table Properties", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

