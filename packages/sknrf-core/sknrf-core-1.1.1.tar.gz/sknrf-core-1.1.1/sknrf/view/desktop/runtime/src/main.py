from PySide6.QtWidgets import QApplication
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl
 
app = QApplication([])
view = QQuickView()
widget = QQuickWidget()
url = QUrl("tutorial3.qml")
 
# view.setSource(url)
widget.setSource(url)
widget.show()
# view.show()
app.exec()
