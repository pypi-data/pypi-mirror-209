# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QTransformFrame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_transformFrame(object):
    def setupUi(self, transformFrame):
        if not transformFrame.objectName():
            transformFrame.setObjectName(u"transformFrame")
        transformFrame.resize(400, 300)
        transformFrame.setFrameShape(QFrame.StyledPanel)
        transformFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(transformFrame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(transformFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.calibrationLabel = QLabel(transformFrame)
        self.calibrationLabel.setObjectName(u"calibrationLabel")
        self.calibrationLabel.setFont(font)
        self.calibrationLabel.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.calibrationLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.calibrationLabel)

        self.transformTable = QTableWidget(transformFrame)
        self.transformTable.setObjectName(u"transformTable")
        self.transformTable.horizontalHeader().setCascadingSectionResizes(False)
        self.transformTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.transformTable.horizontalHeader().setStretchLastSection(True)
        self.transformTable.verticalHeader().setVisible(False)
        self.transformTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.transformTable)

        self.dutLabel = QLabel(transformFrame)
        self.dutLabel.setObjectName(u"dutLabel")
        self.dutLabel.setFont(font)
        self.dutLabel.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.dutLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.dutLabel)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(transformFrame)
        self.addButton.setObjectName(u"addButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile(u":/PNG/black/32/circled_plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.addButton)

        self.removeButton = QPushButton(transformFrame)
        self.removeButton.setObjectName(u"removeButton")
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setMinimumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/PNG/black/32/circled_minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removeButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.removeButton)

        self.infoButton = QPushButton(transformFrame)
        self.infoButton.setObjectName(u"infoButton")
        self.infoButton.setMinimumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/PNG/black/32/information.png", QSize(), QIcon.Normal, QIcon.Off)
        self.infoButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.infoButton)

        self.upButton = QPushButton(transformFrame)
        self.upButton.setObjectName(u"upButton")
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        self.upButton.setMinimumSize(QSize(32, 32))
        icon3 = QIcon()
        icon3.addFile(u":/PNG/black/32/circled_border_triangle_up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.upButton)

        self.downButton = QPushButton(transformFrame)
        self.downButton.setObjectName(u"downButton")
        sizePolicy.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy)
        self.downButton.setMinimumSize(QSize(32, 32))
        icon4 = QIcon()
        icon4.addFile(u":/PNG/black/32/circled_border_triangle_down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.downButton.setIcon(icon4)

        self.horizontalLayout.addWidget(self.downButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(transformFrame)

        QMetaObject.connectSlotsByName(transformFrame)
    # setupUi

    def retranslateUi(self, transformFrame):
        transformFrame.setWindowTitle(QCoreApplication.translate("transformFrame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("transformFrame", u"Circuit Transforms:", None))
        self.calibrationLabel.setText(QCoreApplication.translate("transformFrame", u"Calibration Reference Plane", None))
        self.dutLabel.setText(QCoreApplication.translate("transformFrame", u"DUT Reference Plane", None))
#if QT_CONFIG(tooltip)
        self.addButton.setToolTip(QCoreApplication.translate("transformFrame", u"Add", None))
#endif // QT_CONFIG(tooltip)
        self.addButton.setText("")
#if QT_CONFIG(tooltip)
        self.removeButton.setToolTip(QCoreApplication.translate("transformFrame", u"Remove", None))
#endif // QT_CONFIG(tooltip)
        self.removeButton.setText("")
#if QT_CONFIG(tooltip)
        self.infoButton.setToolTip(QCoreApplication.translate("transformFrame", u"Info", None))
#endif // QT_CONFIG(tooltip)
        self.infoButton.setText("")
#if QT_CONFIG(tooltip)
        self.upButton.setToolTip(QCoreApplication.translate("transformFrame", u"Shift Up", None))
#endif // QT_CONFIG(tooltip)
        self.upButton.setText("")
#if QT_CONFIG(tooltip)
        self.downButton.setToolTip(QCoreApplication.translate("transformFrame", u"Shift Down", None))
#endif // QT_CONFIG(tooltip)
        self.downButton.setText("")
    # retranslateUi

