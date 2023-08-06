import os

import numpy as np

from sknrf.settings import Settings
from sknrf.app.dataviewer.model.dataset import IQFile

header_map = {"sample_point": 2,
                  "sample_rate": 1/Settings().t_step,
                  "waveform_runtime_scaling": 1.0,
                  "iq_modulation_filter": 40e6,
                  "iq_output_filter": 40e6,
                  "marker_1": "0-1",
                  "marker_2": "None",
                  "marker_3": "None",
                  "marker_4": "None",
                  "pulse__rf_blanking": 4,
                  "alc_hold": 3,
                  "alc_status": "On",
                  "bandwidth": "Auto",
                  "power_search_reference": "Modulation"}

def generate_test_waveforms():
    iq_array = np.asarray([1 + 0j], dtype=complex)
    f = IQFile(os.sep.join((Settings().data_root, 'signals', 'CW.h5')), iq_array, header_map, mode='w')
    f.close()

    iq_array = np.random.normal(0, 1, [2 ** 15])
    iq_array /= np.abs(iq_array).max()
    f = IQFile(os.sep.join((Settings().data_root, 'signals', 'AWGN_real.h5')), iq_array, header_map, mode='w')
    f.close()

    iq_array = np.random.normal(0, 1, [2 ** 15]) + 1j * np.random.normal(0, 1, [2 ** 15])
    iq_array /= np.abs(iq_array).max()
    f = IQFile(os.sep.join((Settings().data_root, 'signals', 'AWGN.h5')), iq_array, header_map, mode='w')
    f.close()


def generate_waveforms():

    generate_test_waveforms()
    t_step = Settings().t_step
    t_points_max = 12500
    for freq in np.arange(1.2e6, 80e6, 0.2e6):
        t_period = 1/freq
        cycles = int(np.floor(t_points_max * t_step/t_period))
        t_points = int(np.ceil(cycles * t_period/t_step))   # Complete Full Cycles
        if t_points > 0:
            t_stop = t_points*t_step
            t = np.linspace(0, t_stop, t_points, endpoint=False)
            iq_array = np.sin(2*np.pi*freq*t)
            iq_array /= np.abs(iq_array).max()
            filename = 'SIN_{:g}Hz_{:g}Sa.h5'.format(freq, int(np.round(1/t_step)))
            f = IQFile(os.sep.join((Settings().data_root, 'signals', filename)), iq_array, header_map, mode='w')
            f.close()


if __name__ == "__main__":
    generate_test_waveforms()
