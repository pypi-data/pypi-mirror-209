# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QSequencerFrame.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QSizePolicy,
    QSpacerItem, QSplitter, QTabWidget, QVBoxLayout,
    QWidget)

from sknrf.view.desktop.sequencer.widgets import (ImportListView, SequenceTreeView, VariableTableWidget)

class Ui_sequencerFrame(object):
    def setupUi(self, sequencerFrame):
        if not sequencerFrame.objectName():
            sequencerFrame.setObjectName(u"sequencerFrame")
        sequencerFrame.resize(1385, 681)
        sequencerFrame.setFrameShape(QFrame.StyledPanel)
        sequencerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(sequencerFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(sequencerFrame)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.sequenceFrame = QFrame(self.splitter)
        self.sequenceFrame.setObjectName(u"sequenceFrame")
        self.sequenceFrame.setFrameShape(QFrame.StyledPanel)
        self.sequenceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.sequenceFrame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter_2 = QSplitter(self.sequenceFrame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.importLabel = QLabel(self.layoutWidget)
        self.importLabel.setObjectName(u"importLabel")

        self.verticalLayout_2.addWidget(self.importLabel)

        self.importListView = ImportListView(self.layoutWidget)
        self.importListView.setObjectName(u"importListView")
        self.importListView.setAcceptDrops(True)
        self.importListView.setDragEnabled(True)
        self.importListView.setDragDropMode(QAbstractItemView.DragDrop)
        self.importListView.setAlternatingRowColors(True)
        self.importListView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.importListView)

        self.splitter_2.addWidget(self.layoutWidget)
        self.layoutWidget_2 = QWidget(self.splitter_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.variableLabel = QLabel(self.layoutWidget_2)
        self.variableLabel.setObjectName(u"variableLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variableLabel.sizePolicy().hasHeightForWidth())
        self.variableLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.variableLabel)

        self.variableTabWidget = QTabWidget(self.layoutWidget_2)
        self.variableTabWidget.setObjectName(u"variableTabWidget")
        self.propertyTab = QWidget()
        self.propertyTab.setObjectName(u"propertyTab")
        self.verticalLayout_10 = QVBoxLayout(self.propertyTab)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.variableTableWidget = VariableTableWidget(self.propertyTab)
        self.variableTableWidget.setObjectName(u"variableTableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.variableTableWidget.sizePolicy().hasHeightForWidth())
        self.variableTableWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.variableTableWidget)

        self.variableTabWidget.addTab(self.propertyTab, "")
        self.limitTab = QWidget()
        self.limitTab.setObjectName(u"limitTab")
        self.verticalLayout_11 = QVBoxLayout(self.limitTab)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.variableTabWidget.addTab(self.limitTab, "")
        self.optimizationTab = QWidget()
        self.optimizationTab.setObjectName(u"optimizationTab")
        self.verticalLayout_12 = QVBoxLayout(self.optimizationTab)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.variableTabWidget.addTab(self.optimizationTab, "")

        self.verticalLayout_5.addWidget(self.variableTabWidget)

        self.splitter_2.addWidget(self.layoutWidget_2)
        self.layoutWidget_3 = QWidget(self.splitter_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.sequenceLabel = QLabel(self.layoutWidget_3)
        self.sequenceLabel.setObjectName(u"sequenceLabel")

        self.verticalLayout_6.addWidget(self.sequenceLabel)

        self.sequenceTreeView = SequenceTreeView(self.layoutWidget_3)
        self.sequenceTreeView.setObjectName(u"sequenceTreeView")
        self.sequenceTreeView.setMouseTracking(False)
        self.sequenceTreeView.setAcceptDrops(True)
        self.sequenceTreeView.setDragEnabled(True)
        self.sequenceTreeView.setDragDropMode(QAbstractItemView.DragDrop)
        self.sequenceTreeView.setHeaderHidden(True)

        self.verticalLayout_6.addWidget(self.sequenceTreeView)

        self.splitter_2.addWidget(self.layoutWidget_3)

        self.verticalLayout_7.addWidget(self.splitter_2)

        self.splitter.addWidget(self.sequenceFrame)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)

        self.previewTabWidget = QTabWidget(sequencerFrame)
        self.previewTabWidget.setObjectName(u"previewTabWidget")

        self.horizontalLayout.addWidget(self.previewTabWidget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(sequencerFrame)

        self.variableTabWidget.setCurrentIndex(0)
        self.previewTabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(sequencerFrame)
    # setupUi

    def retranslateUi(self, sequencerFrame):
        sequencerFrame.setWindowTitle(QCoreApplication.translate("sequencerFrame", u"Frame", None))
        self.importLabel.setText(QCoreApplication.translate("sequencerFrame", u"Imports:", None))
        self.variableLabel.setText(QCoreApplication.translate("sequencerFrame", u"Variables:", None))
        self.variableTabWidget.setTabText(self.variableTabWidget.indexOf(self.propertyTab), QCoreApplication.translate("sequencerFrame", u"Properties", None))
        self.variableTabWidget.setTabText(self.variableTabWidget.indexOf(self.limitTab), QCoreApplication.translate("sequencerFrame", u"Limits", None))
        self.variableTabWidget.setTabText(self.variableTabWidget.indexOf(self.optimizationTab), QCoreApplication.translate("sequencerFrame", u"Optimization", None))
        self.sequenceLabel.setText(QCoreApplication.translate("sequencerFrame", u"Sequence:", None))
    # retranslateUi

