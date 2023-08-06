# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QRuntime.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStatusBar,
    QToolBar, QWidget)

class Ui_runtime(object):
    def setupUi(self, runtime):
        if not runtime.objectName():
            runtime.setObjectName(u"runtime")
        runtime.resize(1647, 765)
        runtime.setStyleSheet(u"")
        runtime.setUnifiedTitleAndToolBarOnMac(True)
        self.actionStop = QAction(runtime)
        self.actionStop.setObjectName(u"actionStop")
        self.actionStop.setCheckable(True)
        icon = QIcon()
        icon.addFile(u":/PNG/black/32/circled_stop.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/PNG/red/32/circled_stop.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionStop.setIcon(icon)
        self.actionPause = QAction(runtime)
        self.actionPause.setObjectName(u"actionPause")
        self.actionPause.setCheckable(True)
        icon1 = QIcon()
        icon1.addFile(u":/PNG/black/32/circled_pause.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/PNG/red/32/circled_pause.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionPause.setIcon(icon1)
        self.actionRun = QAction(runtime)
        self.actionRun.setObjectName(u"actionRun")
        self.actionRun.setCheckable(True)
        icon2 = QIcon()
        icon2.addFile(u":/PNG/black/32/circled_border_triangle_right.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/PNG/green/32/circled_border_triangle_right.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionRun.setIcon(icon2)
        self.actionSingle = QAction(runtime)
        self.actionSingle.setObjectName(u"actionSingle")
        self.actionSingle.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u":/PNG/black/32/circled_next.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/PNG/green/32/circled_next.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionSingle.setIcon(icon3)
        self.centralwidget = QWidget(runtime)
        self.centralwidget.setObjectName(u"centralwidget")
        runtime.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(runtime)
        self.statusbar.setObjectName(u"statusbar")
        runtime.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(runtime)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setStyleSheet(u"")
        self.toolBar.setMovable(True)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        runtime.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionSingle)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionStop)

        self.retranslateUi(runtime)

        QMetaObject.connectSlotsByName(runtime)
    # setupUi

    def retranslateUi(self, runtime):
        runtime.setWindowTitle(QCoreApplication.translate("runtime", u"MainWindow", None))
        self.actionStop.setText(QCoreApplication.translate("runtime", u"Stop", None))
#if QT_CONFIG(shortcut)
        self.actionStop.setShortcut(QCoreApplication.translate("runtime", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.actionPause.setText(QCoreApplication.translate("runtime", u"Pause", None))
#if QT_CONFIG(shortcut)
        self.actionPause.setShortcut(QCoreApplication.translate("runtime", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.actionRun.setText(QCoreApplication.translate("runtime", u"Run", None))
#if QT_CONFIG(tooltip)
        self.actionRun.setToolTip(QCoreApplication.translate("runtime", u"Run", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionRun.setShortcut(QCoreApplication.translate("runtime", u"F9", None))
#endif // QT_CONFIG(shortcut)
        self.actionSingle.setText(QCoreApplication.translate("runtime", u"Single", None))
#if QT_CONFIG(shortcut)
        self.actionSingle.setShortcut(QCoreApplication.translate("runtime", u"F8", None))
#endif // QT_CONFIG(shortcut)
        self.toolBar.setWindowTitle(QCoreApplication.translate("runtime", u"toolBar", None))
    # retranslateUi

