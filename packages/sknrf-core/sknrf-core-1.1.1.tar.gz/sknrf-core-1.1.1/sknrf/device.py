import os
import sys
import logging
import site

from PySide6.QtWidgets import QApplication

from sknrf.settings import Settings
from sknrf.view.desktop.base import desktop_logger, unhandled_exception, cleanup

# Initialize Settings/Logging
Settings(os.sep.join((os.getenv('SKNRF_DIR', site.getsitepackages()[0]), "sknrf", "sknrf.yml")))
logger = desktop_logger(logging.getLogger(__name__))

if __name__ == "__main__":
    from PySide6.QtGui import QIcon

    from sknrf.device.instrument import rfreceiver
    from sknrf.device.instrument.rfreceiver import base
    from sknrf.model.base import AbstractModel
    from sknrf.view.desktop.device.menu import DeviceMenuView

    from sknrf.icons import black_64_rc

    app = QApplication(sys.argv)
    sys.excepthook = unhandled_exception
    AbstractModel.init()
    device = base.NoRFReceiver(AbstractModel.device_model(), 1)
    form = DeviceMenuView(rfreceiver, base.NoRFReceiver, device,
                          model_args=[AbstractModel.device_model(), 1], model_icon=QIcon(":/PNG/black/64/rfreceiver.png"))
    form.show()
    try:
        app.exec()
    except SystemExit:
        cleanup(form)
    sys.exit()

