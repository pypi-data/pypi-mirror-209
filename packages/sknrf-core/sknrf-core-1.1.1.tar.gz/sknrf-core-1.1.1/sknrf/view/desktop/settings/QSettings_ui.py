# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QSettings.ui'
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
    QLabel, QLayout, QLineEdit, QSizePolicy,
    QSpinBox, QWidget)

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(513, 326)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings.sizePolicy().hasHeightForWidth())
        settings.setSizePolicy(sizePolicy)
        settings.setFrameShape(QFrame.WinPanel)
        settings.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tPointsLabel = QLabel(settings)
        self.tPointsLabel.setObjectName(u"tPointsLabel")

        self.gridLayout_4.addWidget(self.tPointsLabel, 3, 0, 1, 1)

        self.tStepLineEdit = QLineEdit(settings)
        self.tStepLineEdit.setObjectName(u"tStepLineEdit")

        self.gridLayout_4.addWidget(self.tStepLineEdit, 1, 1, 1, 1)

        self.tStepLabel = QLabel(settings)
        self.tStepLabel.setObjectName(u"tStepLabel")

        self.gridLayout_4.addWidget(self.tStepLabel, 1, 0, 1, 1)

        self.tPointsLineEdit = QLineEdit(settings)
        self.tPointsLineEdit.setObjectName(u"tPointsLineEdit")

        self.gridLayout_4.addWidget(self.tPointsLineEdit, 3, 1, 1, 1)

        self.tStopLineEdit = QLineEdit(settings)
        self.tStopLineEdit.setObjectName(u"tStopLineEdit")

        self.gridLayout_4.addWidget(self.tStopLineEdit, 2, 1, 1, 1)

        self.tStopLabel = QLabel(settings)
        self.tStopLabel.setObjectName(u"tStopLabel")

        self.gridLayout_4.addWidget(self.tStopLabel, 2, 0, 1, 1)

        self.tStepUnitLabel = QLabel(settings)
        self.tStepUnitLabel.setObjectName(u"tStepUnitLabel")

        self.gridLayout_4.addWidget(self.tStepUnitLabel, 1, 2, 1, 1)

        self.tStopUnitLabel = QLabel(settings)
        self.tStopUnitLabel.setObjectName(u"tStopUnitLabel")

        self.gridLayout_4.addWidget(self.tStopUnitLabel, 2, 2, 1, 1)

        self.tPointsUnitLabel = QLabel(settings)
        self.tPointsUnitLabel.setObjectName(u"tPointsUnitLabel")

        self.gridLayout_4.addWidget(self.tPointsUnitLabel, 3, 2, 1, 1)

        self.label_2 = QLabel(settings)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 3)


        self.gridLayout.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.fPointsLineEdit = QLineEdit(settings)
        self.fPointsLineEdit.setObjectName(u"fPointsLineEdit")
        self.fPointsLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.fPointsLineEdit, 3, 1, 1, 1)

        self.fPointsLabel = QLabel(settings)
        self.fPointsLabel.setObjectName(u"fPointsLabel")

        self.gridLayout_3.addWidget(self.fPointsLabel, 3, 0, 1, 1)

        self.numHarmonicsLineEdit = QLineEdit(settings)
        self.numHarmonicsLineEdit.setObjectName(u"numHarmonicsLineEdit")
        self.numHarmonicsLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.numHarmonicsLineEdit, 2, 1, 1, 1)

        self.f0Label = QLabel(settings)
        self.f0Label.setObjectName(u"f0Label")

        self.gridLayout_3.addWidget(self.f0Label, 1, 0, 1, 1)

        self.numHarmonicsLabel = QLabel(settings)
        self.numHarmonicsLabel.setObjectName(u"numHarmonicsLabel")

        self.gridLayout_3.addWidget(self.numHarmonicsLabel, 2, 0, 1, 1)

        self.f0LineEdit = QLineEdit(settings)
        self.f0LineEdit.setObjectName(u"f0LineEdit")
        self.f0LineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.f0LineEdit, 1, 1, 1, 1)

        self.f0UnitLabel = QLabel(settings)
        self.f0UnitLabel.setObjectName(u"f0UnitLabel")

        self.gridLayout_3.addWidget(self.f0UnitLabel, 1, 2, 1, 1)

        self.numHarmonicsUnitLabel = QLabel(settings)
        self.numHarmonicsUnitLabel.setObjectName(u"numHarmonicsUnitLabel")

        self.gridLayout_3.addWidget(self.numHarmonicsUnitLabel, 2, 2, 1, 1)

        self.fPointsUnitLabel = QLabel(settings)
        self.fPointsUnitLabel.setObjectName(u"fPointsUnitLabel")

        self.gridLayout_3.addWidget(self.fPointsUnitLabel, 3, 2, 1, 1)

        self.label = QLabel(settings)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.datagroupLabel = QLabel(settings)
        self.datagroupLabel.setObjectName(u"datagroupLabel")

        self.gridLayout_2.addWidget(self.datagroupLabel, 1, 0, 1, 1)

        self.datagroupLineEdit = QLineEdit(settings)
        self.datagroupLineEdit.setObjectName(u"datagroupLineEdit")
        sizePolicy.setHeightForWidth(self.datagroupLineEdit.sizePolicy().hasHeightForWidth())
        self.datagroupLineEdit.setSizePolicy(sizePolicy)
        self.datagroupLineEdit.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.datagroupLineEdit, 1, 1, 1, 1)

        self.datasetLabel = QLabel(settings)
        self.datasetLabel.setObjectName(u"datasetLabel")

        self.gridLayout_2.addWidget(self.datasetLabel, 2, 0, 1, 1)

        self.datasetLineEdit = QLineEdit(settings)
        self.datasetLineEdit.setObjectName(u"datasetLineEdit")

        self.gridLayout_2.addWidget(self.datasetLineEdit, 2, 1, 1, 1)

        self.label_10 = QLabel(settings)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setFont(font)

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.triggerDeviceLabel = QLabel(settings)
        self.triggerDeviceLabel.setObjectName(u"triggerDeviceLabel")

        self.gridLayout_5.addWidget(self.triggerDeviceLabel, 3, 0, 1, 1)

        self.triggerPortSpinBox = QSpinBox(settings)
        self.triggerPortSpinBox.setObjectName(u"triggerPortSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.triggerPortSpinBox.sizePolicy().hasHeightForWidth())
        self.triggerPortSpinBox.setSizePolicy(sizePolicy2)
        self.triggerPortSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.triggerPortSpinBox.setMinimum(1)

        self.gridLayout_5.addWidget(self.triggerPortSpinBox, 3, 3, 1, 1)

        self.portInstrumentLabel = QLabel(settings)
        self.portInstrumentLabel.setObjectName(u"portInstrumentLabel")

        self.gridLayout_5.addWidget(self.portInstrumentLabel, 3, 2, 1, 1)

        self.triggerDeviceComboBox = QComboBox(settings)
        self.triggerDeviceComboBox.setObjectName(u"triggerDeviceComboBox")
        sizePolicy.setHeightForWidth(self.triggerDeviceComboBox.sizePolicy().hasHeightForWidth())
        self.triggerDeviceComboBox.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.triggerDeviceComboBox, 3, 1, 1, 1)

        self.triggerLabel = QLabel(settings)
        self.triggerLabel.setObjectName(u"triggerLabel")
        sizePolicy1.setHeightForWidth(self.triggerLabel.sizePolicy().hasHeightForWidth())
        self.triggerLabel.setSizePolicy(sizePolicy1)
        self.triggerLabel.setFont(font)

        self.gridLayout_5.addWidget(self.triggerLabel, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 1, 0, 1, 2)


        self.retranslateUi(settings)

        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Frame", None))
        self.tPointsLabel.setText(QCoreApplication.translate("settings", u"t_points:", None))
        self.tStepLabel.setText(QCoreApplication.translate("settings", u"t_step:", None))
        self.tStopLabel.setText(QCoreApplication.translate("settings", u"t_stop:", None))
        self.tStepUnitLabel.setText(QCoreApplication.translate("settings", u"s", None))
        self.tStopUnitLabel.setText(QCoreApplication.translate("settings", u"s", None))
        self.tPointsUnitLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("settings", u"Time Sweep", None))
        self.fPointsLabel.setText(QCoreApplication.translate("settings", u"f_points:", None))
        self.f0Label.setText(QCoreApplication.translate("settings", u"f0:", None))
        self.numHarmonicsLabel.setText(QCoreApplication.translate("settings", u"num_harmonics:", None))
        self.f0UnitLabel.setText(QCoreApplication.translate("settings", u"Hz", None))
        self.numHarmonicsUnitLabel.setText(QCoreApplication.translate("settings", u"Hz", None))
        self.fPointsUnitLabel.setText("")
        self.label.setText(QCoreApplication.translate("settings", u"Frequency Sweep", None))
        self.datagroupLabel.setText(QCoreApplication.translate("settings", u"datagroup:", None))
        self.datasetLabel.setText(QCoreApplication.translate("settings", u"dataset:", None))
        self.label_10.setText(QCoreApplication.translate("settings", u"Dataset", None))
        self.triggerDeviceLabel.setText(QCoreApplication.translate("settings", u"Device:", None))
        self.portInstrumentLabel.setText(QCoreApplication.translate("settings", u"Port:", None))
        self.triggerLabel.setText(QCoreApplication.translate("settings", u"Trigger", None))
    # retranslateUi

