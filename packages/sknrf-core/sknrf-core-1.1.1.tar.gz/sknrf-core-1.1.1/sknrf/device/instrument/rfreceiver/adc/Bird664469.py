import logging
import time
import os
import select

import numpy as np
import torch as th
from scipy.interpolate import interp1d

from sknrf.utilities import myaml
from sknrf.enums.device import SI, si_eps_map
from sknrf.settings import Settings
from sknrf.device.base import device_logger
from sknrf.device.signal import tf, ff
from sknrf.device.instrument.rfreceiver import base
from sknrf.device.instrument.shared.adc import Bird664469
from sknrf.device.instrument.shared.adc.Bird664469 import Bird664469Controller
from sknrf.utilities.numeric import Info, bounded_property

__author__ = 'dtbespal'
logger = device_logger(logging.getLogger(__name__))


class Bird664469Modulated(base.NoRFReceiverModulated):
    firmware_map = {}
    display_order = ["on", "initialized", "port", "freq", "a_p", "b_p", "v", "i",
                     "num_harmonics", "harmonics",
                     "ch", "offset"]

    def __new__(cls, error_model, port, config_filename="", resource_id='172.16.0.135'):
        self = super(Bird664469Modulated, cls).__new__(cls, error_model, port, config_filename)
        # Define object ATTRIBUTES
        self.resource_id = resource_id
        self._on_ = False
        return self

    def __getnewargs__(self):
        return tuple(list(super(Bird664469Modulated, self).__getnewargs__())
                     + [self.resource_id, ])

    def __init__(self, error_model, port, config_filename="", resource_id='172.16.0.135'):
        super().__init__(error_model, port, config_filename)
        self.resource_id = resource_id

        self.connect_handles()
        self.__info__()
        self.preset()

        # Initialize object PROPERTIES
        self.on = False
        # self.adc = 0  # The adc must be manually specified by the test procedure and should be the same for all ch.
        self.offset = self._config["offset"][self.port - 1]
        self.gain = self._config["gain"][self.port - 1]
        self.measure()
        self.initialized = True

    def __getstate__(self, state={}):
        state = super(Bird664469Modulated, self).__getstate__(state=state)
        state["adc"] = self.adc
        state["offset"] = self.offset
        return state

    def __setstate__(self, state, *args, **kwargs):
        super().__setstate__(state)
        self.resource_id = state["resource_id"]

        self.connect_handles()
        self.__info__()
        self.preset()

        # Initialize object PROPERTIES
        self.on = False
        self.adc = state["adc"]
        self.offset = state["offset"]
        self.measure()
        self.initialized = True

    def __info__(self):
        super(Bird664469Modulated, self).__info__()
        cfg = self._config
        v_atol = 1e-3
        i_atol = v_atol/50.
        a_atol, b_atol = v_atol/np.sqrt(50.), v_atol/np.sqrt(50.)
        rtol = 1e-3
        v_max = cfg["voltage_limit"]
        i_max = v_max/50.
        a_max = b_max = v_max/np.sqrt(50.)
        # ### Manually generate info of ATTRIBUTES and PROPERTIES here ###
        self.info["resource_id"] = Info("resource_id", read=True, write=True, check=False)
        self.info["adc"] = Info("adc", read=True, write=True, check=False, min_=0, max_=cfg["ADC_PER_BRD"] - 1)
        self.info["ch"] = Info("ch", read=True, write=False, check=False, min_=0, max_=cfg["CH_PER_ADC"] - 1)
        self.info["offset"] = Info("offset", read=True, write=True, check=False, min_=0, max_=0xFFFF)
        self.info["gain"] = Info("gain", read=True, write=True, check=False, min_=0, max_=0xFFFF)
        self.info["_a_p"] = Info("_a_p", read=False, write=False, check=False,
                                 min_=si_eps_map[SI.A], max_=a_max, abs_tol=a_atol, rel_tol=rtol)
        self.info["_b_p"] = Info("_b", read=False, write=False, check=False,
                                 min_=si_eps_map[SI.B], max_=b_max, abs_tol=b_atol, rel_tol=rtol)
        self.info["_v"] = Info("_v", read=False, write=False, check=False,
                               min_=si_eps_map[SI.V], max_=v_max, abs_tol=v_atol, rel_tol=rtol)
        self.info["_i"] = Info("_i", read=False, write=False, check=False,
                               min_=si_eps_map[SI.I], max_=i_max, abs_tol=i_atol, rel_tol=rtol)
        self.info["a_p"].min, self.info["a_p"].max = 0., a_max
        self.info["b_p"].min, self.info["b_p"].max = 0., b_max
        self.info["v"].min, self.info["v"].max = 0, v_max
        self.info["i"].min, self.info["i"].max = 0, i_max

    def connect_handles(self):
        self.handles["adc"] = Bird664469Controller(self._config, self.resource_id)
        super(Bird664469Modulated, self).connect_handles()

    def preset(self):
        super(Bird664469Modulated, self).preset()
        if self.unique_handle(self.handles["adc"]):
            Bird664469.preset(self)

    @property
    def adc(self):
        ctrl = self.handles["adc"]
        fpga = self._config["FPGA_NAME"]
        if fpga == "metis":
            bus = ctrl.get_reg(f"{fpga}_fpga", 0, "rx_testbus_adc_sel")
            adc = bus - self._config["BRD_SLOT"] * 2
        else:
            adc = 0
        return adc

    @adc.setter
    def adc(self, adc):
        ctrl = self.handles["adc"]
        fpga = self._config["FPGA_NAME"]
        if fpga == "metis":
            bus = self._config["BRD_SLOT"] * 2 + adc
            ctrl.set_reg(f"{fpga}_fpga", 0, "rx_testbus_adc_sel", bus)

    @property
    def ch(self):
        return self.port - 1

    @property
    def offset(self):
        return 0.0

    @offset.setter
    def offset(self, offset):
        pass

    @property
    def _on(self):
        return self._on_

    @_on.setter
    def _on(self, _on):
        self._on_ = _on

    @bounded_property
    def _a_p(self):
        return self._a_p_

    @bounded_property
    def _b_p(self):
        return self._b_p_

    @property
    def _delay(self):
        return self._delay_

    @_delay.setter
    def _delay(self, _delay):
        self._delay_ = _delay

    @property
    def _pulse_width(self):
        return self._pulse_width_

    @_pulse_width.setter
    def _pulse_width(self, _pulse_width):
        self._pulse_width_ = _pulse_width

    def arm(self):
        Bird664469.arm(self)

    def trigger(self):
        Bird664469.trigger(self)

    def measure(self):
        if self.port == 1:
            self.handles["adc"].measure()
        ch = (self.port - 1) % 8
        v_ = self.handles["adc"].data[:Settings().t_points, ch:ch+1]
        self._b_p_[:, 0:1] = v_/np.sqrt(50.)
        super().measure()


class Bird664469CeresModulated(Bird664469Modulated):

    def __new__(cls, error_model, port, config_filename="Bird664469Ceres2.yml", resource_id='172.16.0.135'):
        self = super(Bird664469CeresModulated, cls).__new__(cls, error_model, port, config_filename)
        return self

    def __init__(self, error_model, port, config_filename="Bird664469Ceres2.yml", resource_id='172.16.0.135'):
        super().__init__(error_model, port, config_filename)

    def preset(self):
        super().preset()
        if self.unique_handle(self.handles["adc"]):
            ctrl = self.handles["adc"]
            # ADC offset (Flakey)
            ctrl.socket.sendall(bytes("from radius_adac import adac_offset, adac_gain, adac_led, adac_wr_reg\n", "utf-8"))
            while select.select([ctrl.socket], [], [], self._config["REM_SOCKET_TIMEOUT"])[0]:  # ready
                str(ctrl.socket.recv(self._config["REM_BUFFER_LEN"]), "utf-8")
            time.sleep(0.1)
            ctrl.socket.sendall(bytes("from radius_adac import adac_offset, adac_gain, adac_led, adac_wr_reg\n", "utf-8"))
            while select.select([ctrl.socket], [], [], self._config["REM_SOCKET_TIMEOUT"])[0]:  # ready
                str(ctrl.socket.recv(self._config["REM_BUFFER_LEN"]), "utf-8")
            time.sleep(0.1)
            self.adc = 0

    @property
    def offset(self):
        return self._config["offset"][self.port - 1]

    @offset.setter
    def offset(self, offset):
        ctrl = self.handles["adc"]
        slot, chan, offset = self._config["BRD_SLOT"], self.port - 1, offset
        ctrl.socket.sendall(bytes(f"adac_offset({offset}, {chan})\n", "utf-8"))
        ready = select.select([ctrl.socket], [], [], self._config["REM_SOCKET_TIMEOUT"])[0]
        if ready:
            resp = str(ctrl.socket.recv(self._config["REM_BUFFER_LEN"]), "utf-8")
            if len(resp.strip()):
                raise ConnectionError("Unable to set offset: {:s}".format(resp))
        self._config["offset"][self.port - 1] = offset

    @property
    def gain(self):
        return self._config["gain"][self.port - 1]

    @gain.setter
    def gain(self, gain):
        cfg = self._config
        ctrl = self.handles["adc"]
        slot, chan, gain = self._config["BRD_SLOT"], self.port - 1, gain
        if cfg["CH_TYPE"][self.ch].lower() != "pmt":  # PMT does not have a VGA
            ctrl.socket.sendall(bytes(f"adac_gain({gain}, {chan})\n", "utf-8"))
            ready = select.select([ctrl.socket], [], [], self._config["REM_SOCKET_TIMEOUT"])[0]
            if ready:
                resp = str(ctrl.socket.recv(self._config["REM_BUFFER_LEN"]), "utf-8")
                if len(resp.strip()):
                    raise ConnectionError("Unable to set gain: {:s}".format(resp))
        self._config["gain"][self.port - 1] = gain


class Bird664469MetisModulated(Bird664469Modulated):

    def __new__(cls, error_model, port, config_filename="Bird664469Metis.yml", resource_id='172.16.0.135'):
        self = super(Bird664469MetisModulated, cls).__new__(cls, error_model, port, config_filename)
        return self

    def __init__(self, error_model, port, config_filename="Bird664469Metis.yml", resource_id='172.16.0.135'):
        super().__init__(error_model, port, config_filename)

    def preset(self):
        super().preset()
        if self.unique_handle(self.handles["adc"]):
            ctrl = self.handles["adc"]
            # ADC offset
            ctrl.socket.sendall(bytes("from nucleus_apd_darc import nucleus_apd_darc\n", "utf-8"))
            ctrl.socket.sendall(bytes("nu = nucleus_apd_darc(allDevices)\n", "utf-8"))
            while select.select([ctrl.socket], [], [], self._config["REM_SOCKET_TIMEOUT"])[0]:  # ready
                str(ctrl.socket.recv(self._config["REM_BUFFER_LEN"]), "utf-8")
            self.adc = 0

    @property
    def offset(self):
        return self._config["offset"][self.port - 1]

    @offset.setter
    def offset(self, offset):
        ctrl = self.handles["adc"]
        slot, chan, offset = self._config["BRD_SLOT"], self.adc * 8 + self.port - 1, offset
        ctrl.socket.sendall(bytes(f"nu.dac_write({slot}, {chan + 16}, {offset})\n", "utf-8"))
        ready = select.select([ctrl.socket], [], [], self._config["REM_SOCKET_TIMEOUT"])[0]
        if ready:
            resp = str(ctrl.socket.recv(self._config["REM_BUFFER_LEN"]), "utf-8")
            if len(resp.strip()):
                raise ConnectionError("Unable to set offset: {:s}".format(resp))
        self._config["offset"][self.port - 1] = offset

    @property
    def gain(self):
        return self._config["gain"][self.port - 1]

    @gain.setter
    def gain(self, gain):
        self._config["gain"][self.port - 1] = gain
