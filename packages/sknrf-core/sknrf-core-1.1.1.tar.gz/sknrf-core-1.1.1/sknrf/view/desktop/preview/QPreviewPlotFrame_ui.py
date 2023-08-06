# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QPreviewPlotFrame.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from sknrf.app.dataviewer.view.figure import ContentFigure

class Ui_previewPlotFrame(object):
    def setupUi(self, previewPlotFrame):
        if not previewPlotFrame.objectName():
            previewPlotFrame.setObjectName(u"previewPlotFrame")
        previewPlotFrame.setEnabled(True)
        previewPlotFrame.resize(713, 797)
        previewPlotFrame.setFrameShape(QFrame.StyledPanel)
        previewPlotFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(previewPlotFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.previewPlot = ContentFigure(previewPlotFrame)
        self.previewPlot.setObjectName(u"previewPlot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.previewPlot.sizePolicy().hasHeightForWidth())
        self.previewPlot.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.previewPlot)

        self.settingsHorizontalLayout = QHBoxLayout()
        self.settingsHorizontalLayout.setObjectName(u"settingsHorizontalLayout")
        self.itemVerticalLayout = QVBoxLayout()
        self.itemVerticalLayout.setObjectName(u"itemVerticalLayout")
        self.itemListLabel = QLabel(previewPlotFrame)
        self.itemListLabel.setObjectName(u"itemListLabel")

        self.itemVerticalLayout.addWidget(self.itemListLabel)

        self.itemListWidget = QListWidget(previewPlotFrame)
        self.itemListWidget.setObjectName(u"itemListWidget")
        self.itemListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.itemListWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.itemListWidget.setSelectionRectVisible(True)

        self.itemVerticalLayout.addWidget(self.itemListWidget)


        self.settingsHorizontalLayout.addLayout(self.itemVerticalLayout)

        self.scrollArea = QScrollArea(previewPlotFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(216, 0))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.settingsVerticalLayout = QWidget()
        self.settingsVerticalLayout.setObjectName(u"settingsVerticalLayout")
        self.settingsVerticalLayout.setGeometry(QRect(0, 0, 546, 215))
        self.verticalLayout = QVBoxLayout(self.settingsVerticalLayout)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.defaultGridLayout = QGridLayout()
        self.defaultGridLayout.setObjectName(u"defaultGridLayout")
        self.axesComboBox = QComboBox(self.settingsVerticalLayout)
        self.axesComboBox.addItem("")
        self.axesComboBox.addItem("")
        self.axesComboBox.addItem("")
        self.axesComboBox.setObjectName(u"axesComboBox")

        self.defaultGridLayout.addWidget(self.axesComboBox, 0, 1, 1, 1)

        self.formatLabel = QLabel(self.settingsVerticalLayout)
        self.formatLabel.setObjectName(u"formatLabel")

        self.defaultGridLayout.addWidget(self.formatLabel, 1, 0, 1, 1)

        self.formatComboBox = QComboBox(self.settingsVerticalLayout)
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.setObjectName(u"formatComboBox")

        self.defaultGridLayout.addWidget(self.formatComboBox, 1, 1, 1, 1)

        self.axesLabel = QLabel(self.settingsVerticalLayout)
        self.axesLabel.setObjectName(u"axesLabel")

        self.defaultGridLayout.addWidget(self.axesLabel, 0, 0, 1, 1)

        self.defaultGridLayout.setColumnStretch(0, 1)
        self.defaultGridLayout.setColumnStretch(1, 4)

        self.verticalLayout.addLayout(self.defaultGridLayout)

        self.customGridLayout = QGridLayout()
        self.customGridLayout.setObjectName(u"customGridLayout")
        self.customGridLayout.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout.addLayout(self.customGridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.settingsVerticalLayout)

        self.settingsHorizontalLayout.addWidget(self.scrollArea)

        self.settingsHorizontalLayout.setStretch(0, 1)
        self.settingsHorizontalLayout.setStretch(1, 4)

        self.verticalLayout_3.addLayout(self.settingsHorizontalLayout)

#if QT_CONFIG(shortcut)
        self.itemListLabel.setBuddy(self.itemListWidget)
        self.formatLabel.setBuddy(self.formatComboBox)
        self.axesLabel.setBuddy(self.axesComboBox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.itemListWidget, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.axesComboBox)
        QWidget.setTabOrder(self.axesComboBox, self.formatComboBox)

        self.retranslateUi(previewPlotFrame)

        self.formatComboBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(previewPlotFrame)
    # setupUi

    def retranslateUi(self, previewPlotFrame):
        previewPlotFrame.setWindowTitle(QCoreApplication.translate("previewPlotFrame", u"Frame", None))
        self.itemListLabel.setText(QCoreApplication.translate("previewPlotFrame", u"Items:", None))
        self.axesComboBox.setItemText(0, QCoreApplication.translate("previewPlotFrame", u"Rectangular", None))
        self.axesComboBox.setItemText(1, QCoreApplication.translate("previewPlotFrame", u"Polar", None))
        self.axesComboBox.setItemText(2, QCoreApplication.translate("previewPlotFrame", u"Smith", None))

        self.formatLabel.setText(QCoreApplication.translate("previewPlotFrame", u"Format:", None))
        self.formatComboBox.setItemText(0, QCoreApplication.translate("previewPlotFrame", u"Re", None))
        self.formatComboBox.setItemText(1, QCoreApplication.translate("previewPlotFrame", u"Re_Im", None))
        self.formatComboBox.setItemText(2, QCoreApplication.translate("previewPlotFrame", u"Lin_Deg", None))
        self.formatComboBox.setItemText(3, QCoreApplication.translate("previewPlotFrame", u"Log_Deg", None))

        self.axesLabel.setText(QCoreApplication.translate("previewPlotFrame", u"Axes:", None))
    # retranslateUi

