# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QTabWidget,
    QToolBar, QVBoxLayout, QWidget)

from sknrf.widget.propertybrowser.view.base import PropertyScrollArea

class Ui_settingsView(object):
    def setupUi(self, settingsView):
        if not settingsView.objectName():
            settingsView.setObjectName(u"settingsView")
        settingsView.resize(509, 461)
        self.actionDocumentation = QAction(settingsView)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        icon = QIcon(QIcon.fromTheme(u"help-about"))
        self.actionDocumentation.setIcon(icon)
        self.centralwidget = QWidget(settingsView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.tabWidget.addTab(self.mainTab, "")
        self.generalTab = QWidget()
        self.generalTab.setObjectName(u"generalTab")
        self.verticalLayout_2 = QVBoxLayout(self.generalTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.propertyTable = PropertyScrollArea(self.generalTab)
        self.propertyTable.setObjectName(u"propertyTable")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propertyTable.sizePolicy().hasHeightForWidth())
        self.propertyTable.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.propertyTable)

        self.tabWidget.addTab(self.generalTab, "")
        self.appTab = QWidget()
        self.appTab.setObjectName(u"appTab")
        self.verticalLayout_3 = QVBoxLayout(self.appTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.appPropertyTable = PropertyScrollArea(self.appTab)
        self.appPropertyTable.setObjectName(u"appPropertyTable")

        self.verticalLayout_3.addWidget(self.appPropertyTable)

        self.tabWidget.addTab(self.appTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        settingsView.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(settingsView)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 509, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        settingsView.setMenuBar(self.menubar)
        self.toolBar = QToolBar(settingsView)
        self.toolBar.setObjectName(u"toolBar")
        settingsView.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)
        self.toolBar.addAction(self.actionDocumentation)

        self.retranslateUi(settingsView)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settingsView)
    # setupUi

    def retranslateUi(self, settingsView):
        settingsView.setWindowTitle(QCoreApplication.translate("settingsView", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("settingsView", u"Documentation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), QCoreApplication.translate("settingsView", u"Main", None))
#if QT_CONFIG(tooltip)
        self.propertyTable.setToolTip(QCoreApplication.translate("settingsView", u"Property Browser", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.propertyTable.setWhatsThis(QCoreApplication.translate("settingsView", u"The Property Browser Controls Table Properties", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalTab), QCoreApplication.translate("settingsView", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.appTab), QCoreApplication.translate("settingsView", u"App", None))
        self.menuHelp.setTitle(QCoreApplication.translate("settingsView", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("settingsView", u"toolBar", None))
    # retranslateUi

