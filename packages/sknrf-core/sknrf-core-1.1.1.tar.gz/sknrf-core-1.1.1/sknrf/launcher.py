import os
import sys
import logging
import site

from PySide6.QtWidgets import QApplication

from sknrf.settings import Settings
from sknrf.view.desktop.base import desktop_logger, unhandled_exception, cleanup

# Initialize Logging
Settings(os.sep.join((os.getenv('SKNRF_DIR', site.getsitepackages()[0]), "sknrf", "sknrf.yml")))
logger = desktop_logger(logging.getLogger(__name__))

if __name__ == "__main__":
    from collections import OrderedDict

    from sknrf.model.base import AbstractModel
    from sknrf.model.sequencer.base import SequencerSideModel
    from sknrf.view.desktop.launcher.menu import LauncherMenuView

    from sknrf.view.desktop import calibration

    app = QApplication(sys.argv)
    sys.excepthook = unhandled_exception
    AbstractModel.init()
    package_map = OrderedDict((("Calibration", [calibration]),))
    side_model = SequencerSideModel(package_map)
    form = LauncherMenuView(AbstractModel.device_model(), AbstractModel.datagroup_model(), side_model)
    form.showMaximized()
    try:
        app.exec()
    except SystemExit:
        cleanup(form)
    sys.exit()

