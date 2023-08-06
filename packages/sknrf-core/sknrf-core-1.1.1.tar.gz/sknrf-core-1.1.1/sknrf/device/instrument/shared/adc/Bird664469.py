import os
import csv
import time
import logging
import subprocess
import socket

import math as mt
import warnings

import numpy as np
from scipy.interpolate import interp1d
import torch as th
import requests

from sknrf.settings import Settings
from sknrf.device.base import device_logger
from sknrf.utilities.patterns import SingletonType

logger = device_logger(logging.getLogger(__name__))


class Bird664469Controller(object, metaclass=SingletonType):

    def __init__(self, config, id):
        self._config = config
        self.id = id
        self.data = 2**15 * th.ones((Settings().t_points, config["CH_PER_ADC"]), dtype=th.complex128)

        # Socket Interface
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((self._config["REM_IP"], self._config["REM_SOCKET_PORT"]))
        sock.setblocking(False)
        self.socket = sock

    def get_reg(self, group, group_ind, name):
        cmd_str = 'http://{REM_IP:s}:{REM_PORT:d}/{REM_INTERFACE:s}/{group:s}/{group_ind:d}/{name:s}'.format(
            REM_IP=self._config["REM_IP"], REM_PORT=5000, REM_INTERFACE=self._config["REM_IFACE"],
            group=group, group_ind=group_ind, name=name)
        return requests.get(cmd_str).json()[name]

    def set_reg(self, group, group_ind, name, value):
        cmd_str = 'http://{REM_IP:s}:{REM_PORT:d}/{REM_INTERFACE:s}/{group:s}/{group_ind:d}/'.format(
            REM_IP=self._config["REM_IP"], REM_PORT=self._config["REM_PORT"], REM_INTERFACE=self._config["REM_IFACE"],
            group=group, group_ind=group_ind)
        requests.put(cmd_str, json=dict(((name, value),)))

    def measure(self):

        def scale(x, x_min, x_max, y_min, y_max):
            return (x - x_min) / (x_max - x_min) * (y_max - y_min) + y_min
        time.sleep(self._config["REM_MEASURE_DELAY"])
        loc_db = os.sep.join((Settings().data_root, "testdata", "data.csv"))
        rem_db = os.sep.join((self._config["REM_ROOT"], "data.csv"))
        rem_cmd = self._config["REM_SCP_DN"].format(FROM=rem_db, TO=loc_db)
        logger.debug(rem_cmd), os.system(rem_cmd + Settings().system_buffers)
        pad = "0"*5
        num_chan = self._config["CH_PER_ADC"]
        t_points = int(np.ceil(Settings().t_points * self._config["resample"]))
        with open(loc_db, 'r') as f:
            data_str = f.read()
            data_list = data_str.replace("\n", ", ").split(", ")[0:9*t_points]
            data_list = ["%s%s" % (pad[:len(pad) - len(i)], i) for i in data_list]
            n_points = mt.floor(len(data_list)/(num_chan + 1))
            if n_points == 0:
                warnings.warn("Bird664469Controller:No Ext trigger")
            elif n_points < t_points:
                raise BufferError(f"Bird664469Controller:ADC only captured {n_points:d}")
            else:
                try:
                    data_array = np.asarray(data_list, "S5").astype("u2")
                except ValueError:
                    raise BufferError(f"Bird664469Controller:ADC bad capture")
                data_array = data_array[0:(num_chan + 1) * n_points]
                data_array = data_array.reshape(mt.floor(data_array.shape[0]/(num_chan + 1)), (num_chan + 1))[:, 1:]
                data_array = data_array[0:t_points, :]
                t_sys = np.linspace(0, 1, Settings().t_points)
                t_dev = np.linspace(0, 1, t_points)
                iq = interp1d(t_dev, data_array, kind="linear", axis=0)(t_sys)  # Upsample or Downsample
                self.data = th.as_tensor(scale(iq, 0, (1 << 16) - 1, -0.5, 0.5))


def preset(self):

    ctrl = self.handles["adc"]
    fpga = self._config["FPGA_NAME"]

    # Trigger
    ctrl.set_reg(f"{fpga}_fpga", 0, "pulsegen_trig_ctrl", 1)

    # ADC
    if fpga == "metis":
        ctrl.set_reg(f"{fpga}_fpga", 0, "rx_testbus_reg_ctrl_en", 1)

    # Clear FIFO
    trig_id = 8 if fpga == "metis" else 4
    ctrl.set_reg(f"stream_fifo_trigger_control_{trig_id:d}", 0, "trigger_window_size", 4090)
    ctrl.set_reg(f"stream_fifo_trigger_control_{trig_id:d}", 0, "clear_trigger", True)
    ctrl.set_reg(f"stream_fifo_trigger_control_{trig_id:d}", 0, "clear_fifo", 0xffff)
    ctrl.set_reg(f"stream_fifo_trigger_control_{trig_id:d}", 0, "clear_fifo", 0x0000)
    ctrl.set_reg(f"stream_fifo_trigger_control_{trig_id:d}", 0, "clear_trigger", False)
    ctrl.set_reg(f"stream_fifo_trigger_control_{trig_id:d}", 0, "enable", True)

    arm(self)


def arm(self):
    if self.port == 1:
        meas_delay = self._config["REM_MEASURE_DELAY"]
        rem_cmd = "timeout %f %s " % (meas_delay, os.sep.join((self._config["REM_ROOT"], "nucleus_adc_dump")))
        loc_cmd = self._config["REM_SSH"].format(REM_CMD=rem_cmd)
        logger.debug(loc_cmd), subprocess.Popen(loc_cmd, shell=True, **Settings().subprocess_buffers)
        time.sleep(self._config["REM_ARM_DELAY"])


def trigger(self):
    pass


