import logging
import time
import os

import numpy as np
import torch as th
from scipy.interpolate import interp1d
import pyvisa as visa
from pyvisa.errors import VisaIOError

from sknrf.enums.device import SI, si_eps_map, ReceiverZ
from sknrf.settings import Settings
from sknrf.device.base import device_logger
from sknrf.device.signal import tf
from sknrf.device.instrument.lfreceiver import base
# from sknrf.device.instrument.shared.oscilloscope import KeysightEXRxxxA
from sknrf.utilities.numeric import Info, bounded_property

__author__ = 'dtbespal'
logger = device_logger(logging.getLogger(__name__))


class SiglentSDS1xxxModulated(base.NoLFReceiverModulated):
    firmware_map = {}
    display_order = ["on", "initialized", "channel", "freq", "v", "i"]

    def __new__(cls, error_model, port, config_filename="",
                # resource_id='USB0::62700::60984::SDSMMFCQ5R7990::0::INSTR'):
                resource_id='TCPIP0::172.16.0.100::inst0::INSTR'):
        self = super(SiglentSDS1xxxModulated, cls).__new__(cls, error_model, port, config_filename)
        # Define object ATTRIBUTES
        self.resource_id = resource_id
        self._on_ = False
        return self

    def __getnewargs__(self):
        return tuple(list(super(SiglentSDS1xxxModulated, self).__getnewargs__())
                     + [self.resource_id])

    def __init__(self, error_model, port, config_filename="",
                # resource_id='USB0::62700::60984::SDSMMFCQ5R7990::0::INSTR'):
                 resource_id='TCPIP0::172.16.0.100::inst0::INSTR'):
        super().__init__(error_model, port, config_filename)
        self.resource_id = resource_id

        self.connect_handles()
        self.__info__()
        self.preset()

        # Initialize object PROPERTIES
        self._on = False
        self.measure()
        self.initialized = True

    def __getstate__(self, state={}):
        state = super(SiglentSDS1xxxModulated, self).__getstate__(state=state)
        return state

    def __setstate__(self, state, *args, **kwargs):
        super().__setstate__(state)
        self.resource_id = state["resource_id"]

        self.connect_handles()
        self.__info__()
        self.preset()

        # Initialize object PROPERTIES
        self._on = False
        self.measure()
        self.initialized = True

    def __info__(self):
        super(SiglentSDS1xxxModulated, self).__info__()
        abs_tol = 1e-3
        rel_tol = 1e-3
        v_max = self._config["voltage_limit"]
        i_max = self._config["current_limit"]
        # ### Manually generate info of ATTRIBUTES and PROPERTIES here ###
        self.info["resource_id"] = Info("resource_id", read=True, write=True, check=False)
        self.info["_v"] = Info("_v", read=False, write=False, check=False,
                               min_=si_eps_map[SI.V], max_=v_max,
                               abs_tol=abs_tol, rel_tol=rel_tol)
        self.info["_i"] = Info("_i", read=False, write=False, check=False,
                               min_=si_eps_map[SI.I], max_=i_max,
                               abs_tol=abs_tol, rel_tol=rel_tol)
        self.info["v"].min, self.info["v"].max = 0., v_max
        self.info["i"].min, self.info["i"].max = 0., i_max

    def connect_handles(self):
        rm = visa.ResourceManager(os.getenv('VISA_LIB', '@py'))
        self.handles["scope"] = rm.open_resource(self.resource_id)
        super(SiglentSDS1xxxModulated, self).connect_handles()

    def preset(self):
        super(SiglentSDS1xxxModulated, self).preset()
        if self.unique_handle(self.handles["scope"]):
            ch = self.port
            self.handles["scope"].query('*IDN?')
            self.handles["scope"].write('*CLS')
            self.handles["scope"].write('*RST')
            self.handles["scope"].query('CMR?')
            self.handles["scope"].query('*OPC?')
            time.sleep(5.0)

            self.handles["scope"].write(f'BANDWIDTH_LIMIT C1, ON')  # ON | OFF
            self.handles["scope"].write(f'BANDWIDTH_LIMIT C2, ON')  # ON | OFF
            self.handles["scope"].write(f'BANDWIDTH_LIMIT C3, ON')  # ON | OFF
            self.handles["scope"].write(f'BANDWIDTH_LIMIT C4, ON')  # ON | OFF
            self.handles["scope"].query('*OPC?')

            # x-axis
            self.handles["scope"].write('WFSU TYPE,1')  # 0 = screen, 1 = memory
            self.handles["scope"].write(f'MEMORY_SIZE 14K')
            sample_rate = self.handles["scope"].query(f'SARA?')
            sample_rate = eval(sample_rate[len('SARA '):-len('Sa/s') - 1])
            num_samples = self.handles["scope"].query(f'SANU? C{ch:d}')
            num_samples = round(eval(num_samples[len('SANU '):-len('pts') - 1]))
            self.handles["scope"].query('*OPC?')

            # y-axis
            self.handles["scope"].write(f'C{ch:d}:VDIV 1V')

            # Trigger
            self.handles["scope"].write(f'TRIG_DELAY 0MS')  # +ve pre trigger acquisition, -ve post trigger acquisition
            self.handles["scope"].write(f'TRIG_SELECT EDGE, SR, C{ch:d}')
            self.handles["scope"].write(f'C{ch:d}:TRIG_SLOPE POS')
            self.handles["scope"].write(f'C{ch:d}:TRIG_COUPLING HFREJ')  # AC,DC,HFREJ,LFREJ
            self.handles["scope"].write(f'C{ch:d}:TRIG_LEVEL 1.0V')
            self.handles["scope"].write(f'MEMORY_SIZE 14K')

    @property
    def _on(self):
        return bool(int(self.handles["scope"].query(":CHANnel%d:DISPlay?" % (self.port,))))

    @_on.setter
    def _on(self, _on):
        self.handles["scope"].write(":CHANnel%d:DISPlay %d" % (self.port, int(_on)))
        self._on_ = _on

    @bounded_property
    def _v(self):
        return self._v_

    @bounded_property
    def _i(self):
        return self._i_

    @property
    def z0(self):
        # z_str = self.handles["scope"].query(":CHANnel%d:INPut?" % (self.port,))
        # return ReceiverZ._1MOhm if z_str == "ONEMeg" else ReceiverZ._50Ohm
        return ReceiverZ._1MOhm

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
        self.handles["scope"].write(f'ARM')
        self.handles["scope"].write('WAIT')

    def trigger(self):
        self.handles["scope"].write('FORCE_TRIGGER')
        self.handles["scope"].query('*OPC?')
        self.handles["scope"].write('TRIG_MODE SINGLE')
        self.handles["scope"].query('*OPC?')

    def measure(self):
        ch = self.port
        num_samples = self.handles["scope"].query(f'SANU? C{ch:d}')
        num_samples = round(eval(num_samples[len('SANU '):-len('pts') - 1]))
        eof = False
        response = ' '
        desc = ''
        offset = 0
        data = np.zeros(num_samples, dtype='u1')
        self.handles["scope"].write(f'C{ch:d}:WF? DAT2')
        time.sleep(2)
        while eof is False and len(response):
            time.sleep(0.1)
            response = self.handles["scope"].read_raw()
            if len(response) == 0:
                raise BufferError('No Signal Detected')
            if len(desc) == 0:  # first message
                desc = response[0:21].decode('ascii')
                index = desc.index('#9')
                index_start_data = index + 2 + 9
                data_size = int(response[index + 2:index_start_data])
                offset = 0
                response = response[index_start_data:]
            if len(response) >= 2 and response[-2] == 10 and response[-1] == 10:  # last message
                response = response[:-2]
                eof = True
            arr = np.frombuffer(response, dtype="u1")
            print(f'{offset} {len(response)} {len(arr)}')
            data[offset:offset + len(response)] = arr
            offset += len(response)
        self._v_[:, 0:1] = th.as_tensor(data.reshape(-1, 1))
        super().measure()
