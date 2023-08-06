import sys

from PySide6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout

import sknrf
from qprogressindicator import QProgressIndicator


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = QDialog()
    layout = QVBoxLayout()
    label = QLabel("Hello World", parent=dialog)
    indicator = QProgressIndicator(parent=dialog)

    layout.addWidget(label)
    layout.addWidget(indicator)
    dialog.setLayout(layout)

    indicator.startAnimation()
    dialog.show()
    sys.exit(app.exec())
