"""
================================================
Dataset (:mod:`sknrf.model.dataviewer.dataset`)
================================================

This module stores measurement data into a hierarchial HDF5 database consisting of the following organization.

* Datagroup
    * Dataset1
        * v1
        * i1
        * z1
        * ...
    * Dataset2
        * v1
        * i1
        * z1
        * ...
    * ...
    * DatasetN
        * v1
        * i1
        * z1
        * ...

This ensures that related measurement datasets can be stored inside the same database datagroup.

See Also
--------
sknrf.model.dataviewer.equation.EquationModel, sknrf.model.dataviewer.equation.SignalArray

"""
import os
import logging
from itertools import cycle

import re
import numpy as np
import torch as th
import yaml
import h5py as h5
from collections import OrderedDict
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon
from matplotlib.markers import MarkerStyle
from scipy.signal import resample

from sknrf.settings import Settings, InstrumentFlag
from sknrf.device.signal import tf
from sknrf.enums.device import Response, rid2b, rid2p
from sknrf.enums.device import response_name_map, response_shape_map, response_fill_map
from sknrf.enums.device import response_dtype_map, response_device_map, response_grad_map
from sknrf.enums.signal import transform_map, transform_label_map, transform_icon_map, transform_xlabel_map
from sknrf.enums.sequencer import Sweep, Goal, sid2b, sid2p
from sknrf.enums.sequencer import sweep_name_map, sweep_shape_map, sweep_fill_map
from sknrf.enums.sequencer import sweep_device_map, sweep_grad_map
from sknrf.enums.runtime import th_2_np_dtype_map
from sknrf.device import AbstractDevice
from sknrf.utilities.rf import real, imag
from sknrf.utilities.numeric import Domain, unravel_index
from sknrf.utilities.db import H5File
from sknrf.icons import black_32_rc

from sknrf.app.dataviewer.model.figure import AxesType, AxisType, PlotType, FormatType, format_map
from sknrf.app.dataviewer.model.figure import AxesModel, PlotModel


__author__ = 'dtbespal'
logger = logging.getLogger(__name__)


def preview_plot(ds, get_func, item: str, filters: list,
                 ax_model: AxesModel, plt_model: PlotModel,
                 transform_type: Domain, options_map):
    format_ = format_map[plt_model.y_format]
    x = y = np.empty((0, 0))
    transform = transform_map[transform_type]
    filters = [f for f in reversed(filters)]
    # Before Transform
    y = get_func(ds, item)[...].detach()
    if isinstance(ds, AbstractDevice):
        if transform_type in (Domain.FT, Domain.TT):
            pad_num = Settings().num_harmonics + 1 - y.shape[-1]
            pad = th.zeros((Settings().t_points, pad_num), dtype=y.dtype)
            harm_0 = ds["harmonics"][0] if isinstance(ds, BaseWCArrayGroup) else ds.harmonics[0]
            if harm_0 == Settings().harmonics[0]:  # LF Signal
                y = th.cat((y, pad), dim=-1)
            else:  # RF Signal
                y = th.cat((pad, y), dim=-1)
    y = transform(y)
    for dim, filter_ in enumerate(filters):
        y = y.narrow(dim, filter_[0], filter_[-1] + 1 - filter_[0])

    # After Transform
    if ax_model.type == AxesType.Rectangular:
        y = format_(y)
        if transform_type == Domain.TF:
            x = ds.time[...]
            for dim, filter_ in enumerate(filters):
                if x.shape[dim] > 1:
                    x = x.narrow(dim, filter_[0], filter_[-1] + 1 - filter_[0])
            x = th.moveaxis(x, -2, -1)
            x = x.reshape((-1, x.shape[-1]))
            y = th.moveaxis(y, -2, -1)
            y = y.reshape((th.prod(th.as_tensor(y.shape[:-1])), y.shape[-1]))
        elif transform_type == Domain.FF:
            x = ds.freq_m[...]
            for dim, filter_ in enumerate(filters):
                if x.shape[dim] > 1:
                    x = x.narrow(dim, filter_[0], filter_[-1] + 1 - filter_[0])
            x = th.moveaxis(x, -2, -1)
            x = x.reshape((-1, x.shape[-1]))
            y = th.moveaxis(y, -2, -1)
            y = y.reshape((th.prod(th.as_tensor(y.shape[:-1])), y.shape[-1]))
        elif transform_type == Domain.FT:
            x = ds.time_c[...]
            if len(x.shape) == 1:
                x = x.reshape(1, -1)
            for dim, filter_ in enumerate(filters):
                if x.shape[dim] > 1:
                    x = x.narrow(dim, filter_[0], filter_[-1] + 1 - filter_[0])
            x = x.reshape((-1, x.shape[-1]))
            y = y.reshape((th.prod(th.as_tensor(y.shape[:-1])), y.shape[-1]))
        elif transform_type == Domain.TT:
            x = ds.time_c[...]
            if len(x.shape) == 1:
                x = x.reshape(1, -1)
            for dim, filter_ in enumerate(filters):
                if x.shape[dim] > 1:
                    x = x.narrow(dim, filter_[0], filter_[-1] + 1 - filter_[0])
            x = x.reshape((-1, x.shape[-1]))
            y = y.reshape((th.prod(th.as_tensor(y.shape[:-1])), y.shape[-1]))
    elif ax_model.type == AxesType.Polar:
        x = y.angle()
        x = th.moveaxis(x, -2, -1)
        x = x.reshape((-1, x.shape[-1]))
        y = y.abs()
        y = th.moveaxis(y, -2, -1)
        y = y.reshape((-1, y.shape[-1]))
    elif ax_model.type == AxesType.Smith:
        x = real(y)
        x = th.moveaxis(x, -2, -1)
        x = x.reshape((-1, x.shape[-1]))
        y = imag(y)
        y = th.moveaxis(y, -2, -1)
        y = y.reshape((-1, y.shape[-1]))
    return ax_model, plt_model, x, y, options_map


class WCArray(h5.Dataset):
    """Subclass of PyTables CArray designed to avoid numpy limitation that arrays cannot exceed 32 dimensions"""

    @classmethod
    def create_array(cls, ds, name, shape=None, dtype=None, data=None, **kwds):
        squeeze_shape = tuple([s for s in shape if s > 1])
        self = WCArray(ds.create_dataset(name, shape=squeeze_shape, dtype=dtype, data=data, **kwds).id)
        self.attrs["shape"] = shape
        self.attrs["squeeze_shape"] = squeeze_shape
        return self

    def __init__(self, bind, *args, readonly=False):
        super(WCArray, self).__init__(bind, *args, readonly=readonly)

    def __getitem__(self, key, new_dtype=None):
        value = super(WCArray, self).__getitem__(key, new_dtype=new_dtype)
        shape = tuple(self.attrs["shape"])
        return th.as_tensor(value).reshape(shape)

    def __setitem__(self, key, value):
        shape = tuple(self.attrs["squeeze_shape"])
        if isinstance(key, (list, tuple)):
            key = tuple([k for s, k in zip(self.attrs["shape"], key) if s > 1])
            shape = tuple([1 if str(k).isdigit() else s for s, k in zip(self.attrs["squeeze_shape"], key)])
        value = value.reshape(shape).numpy()
        super(WCArray, self).__setitem__(key, value)


class IQFile(H5File):
    """Database representation of an IQ Waveform

        Parameters
        ----------
        filename : str
            Absolute filename of the database.
        mode : str
            'r' - read access, 'w' - write access, 'a' - append to existing database.

        """

    def __init__(self, name, *args, mode='r', driver=None, libver=None, userblock_size=None, swmr=False,
                 rdcc_nslots=None, rdcc_nbytes=None, rdcc_w0=None, track_order=None,
                 fs_strategy=None, fs_persist=False, fs_threshold=1, fs_page_size=None,
                 page_buf_size=None, min_meta_keep=0, min_raw_keep=0, locking=None, **kwds):
        super(IQFile, self).__init__(
                 name, mode=mode, driver=driver, libver=libver, userblock_size=userblock_size, swmr=swmr,
                 rdcc_nslots=rdcc_nslots, rdcc_nbytes=rdcc_nbytes, rdcc_w0=rdcc_w0, track_order=track_order,
                 fs_strategy=fs_strategy, fs_persist=fs_persist, fs_threshold=fs_threshold, fs_page_size=fs_page_size,
                 page_buf_size=page_buf_size, min_meta_keep=min_meta_keep, min_raw_keep=min_raw_keep, locking=locking,
                 **kwds)
        t_points = Settings().t_points
        shape = (t_points,)
        if not mode.startswith('r'):
            if len(args) == 0:
                iq_array = np.ones(shape, dtype=complex)
                WCArray.create_array(self, "iq", shape=iq_array.shape, dtype=iq_array.dtype, data=iq_array)
                self.attrs["sample_point"] = t_points
                self.attrs["sample_rate"] = 1/Settings().t_step
                self.attrs["waveform_runtime_scaling"] = 1.0
                self.attrs["iq_modulation_filter"] = 40.0e6
                self.attrs["iq_output_filter"] = 40.0e6
                self.attrs["marker_1"] = "None"
                self.attrs["marker_2"] = "None"
                self.attrs["marker_3"] = "None"
                self.attrs["marker_4"] = "None"
                self.attrs["pulse__rf_blanking"] = 4
                self.attrs["alc_hold"] = 4
                self.attrs["alc_status"] = "Off"
                self.attrs["bandwidth"] = "Auto"
                self.attrs["power_search_reference"] = "Modulation"
            else:
                iq_array, header_map = args[0], args[1]
                WCArray.create_array(self, "iq", shape=iq_array.shape, dtype=iq_array.dtype, data=iq_array)
                for k, v in header_map.items():
                    self.attrs[k] = v

    def __getitem__(self, item):
        item = super(IQFile, self).__getitem__(item)
        if isinstance(item, h5.Dataset):
            item = WCArray(item.id)
        return item

    def __setitem__(self, item, value):
        if isinstance(item, IQFile):
            item = h5.Dataset(item.id)
        super(IQFile, self).__setitem__(item, value)

    @property
    def iq(self):
        t_step, t_points = Settings().t_step, Settings().t_points
        if self.filename.endswith("CW.h5"):
            upsample_factor = 1
        else:
            upsample_factor = int(np.ceil(1/t_step/self.header["sample_rate"]))
        iq_array = self["iq"][...].detach().numpy()
        iq_array = resample(iq_array, upsample_factor*iq_array.size)
        if t_points <= iq_array.size:
            iq_array = iq_array[0:t_points]
        else:
            iq_array = np.append(np.tile(iq_array, (int(np.floor(t_points / iq_array.size)),)),
                                 iq_array[0:np.mod(t_points, iq_array.size)])
        return th.as_tensor(iq_array)

    @property
    def header(self):
        header_map = OrderedDict()
        for k in self.attrs.keys():
            v = self.attrs[k]
            try:
                v = v.decode()
                if len(v) == 0:
                    v = "None"
            except AttributeError:
                pass
            header_map[k] = v
        return header_map

    @property
    def marker(self):
        t_step, t_points = Settings().t_step, Settings().t_points
        if self.filename.endswith("CW.h5"):
            upsample_factor = 1
        else:
            upsample_factor = int(np.ceil(1/t_step/self.header["sample_rate"]))
        m = np.zeros((t_points,), dtype=">i1")
        for marker_index in range(0, 4):
            marker_name = "marker_%d" % (marker_index + 1,)
            marker_str = self.attrs[marker_name]
            if marker_str.lower() == "none":
                m |= np.left_shift(0, marker_index)
            elif marker_str.lower() == "all":
                m |= np.left_shift(1, marker_index)
            elif len(marker_str) != 0:
                segments = marker_str.split(", ")
                for segment in segments:
                    start, stop = segment.strip().split("-")
                    start_val, stop_val = upsample_factor*(int(start.strip()) - 1), upsample_factor*int(stop.strip())
                    m[start_val:stop_val] |= np.left_shift(1, marker_index)

        if t_points <= m.size:
            m = m[0:t_points]
        else:
            m = np.append(np.tile(m, (int(np.floor(t_points / m.size)),)),
                          m[0:np.mod(t_points, m.size)])
        return th.as_tensor(m)

    @staticmethod
    def from_waveform(filename, iq_array, header_map):
        return IQFile(filename, iq_array, header_map, mode='w')

    def to_waveform(self):
        iq_array = self.iq.detach().numpy()
        iq_array.dtype = float  # Interleave IQ
        iq_array = np.round(iq_array*(32767/np.max(np.abs(iq_array))))  # Scaling
        iq_array = iq_array.astype(">i2")  # Convert to big endian uint16.
        marker = self.marker.detach().numpy()
        return iq_array, self.header, marker.astype(np.int8)

    @staticmethod
    def from_txt(filename, i_filename, q_filename, config_filename):
        iq_array = np.loadtxt(i_filename, delimiter=' ', dtype=complex) \
                   + 1j * np.loadtxt(q_filename, delimiter=' ', dtype=complex)
        with open(config_filename, "rt") as f:
            while not f.readline().startswith("### Don't Touch ###"):
                pass
            header_map = yaml.full_load(f)
            for k in list(header_map.keys()):
                k_list = re.split("\s+", k)
                k_, unit = ("_".join(k_list[:-1]), k_list[-1][1:-1]) if k_list[-1][0] == '(' else ("_".join(k_list), "")
                k_ = k_.lower().replace('/', "__")
                v = header_map.pop(k)
                try:
                    if unit == "MHz":
                        v *= 1e6
                    elif unit == "%":
                        v /= 100
                except TypeError:
                    v = np.nan
                header_map[k_] = v
        return IQFile(filename, iq_array, header_map, mode='w')

    def to_txt(self, i_filename, q_filename, config_filename):
        iq_array = self.iq.detach().numpy()
        np.savetxt(i_filename, iq_array.real)
        np.savetxt(q_filename, iq_array.imag)
        with open(config_filename, "wt") as f:
            f.write("### Don't Touch ###\n")
            f.write("\n")
            yaml.dump(dict(self.header), f, default_flow_style=False)

    def tostring(self):
        iq_array = self.iq.detach().numpy()
        iq_array.dtype = float
        return iq_array.astype(">i2").tostring()


class DatasetIterator(object):

    def __init__(self, dataset, step=1, sweep_enabled=True):
        self.dataset = dataset
        self.sweep_enabled = sweep_enabled
        self.sweep_map = dataset.sweep_map
        self.sweep_shape = list(dataset.sweep_shape)
        self.slice_index = []
        while self.sweep_shape and not step % self.sweep_shape[-1]:
            step = int(step / self.sweep_shape[-1])
            del self.sweep_shape[-1]
            self.slice_index.append(slice(None))
        self.sweep_shape = tuple(self.sweep_shape)
        self.slice_index = tuple(self.slice_index)
        self.array_index = self.slice_index
        self.i = 0
        self.n = int(np.prod(self.sweep_shape))

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.n:
            self.array_index = unravel_index(self.i, self.sweep_shape) + self.slice_index
            i = self.i
            ds = self.dataset
            viz_bag = [None]*(Settings().num_ports + 1)
            step_shape = (-1, ds.sweep_shape[-1])
            if self.sweep_enabled:
                for port_index in range(Settings().num_ports + 1):
                    if port_index in ds.ports:
                        lf_index = self.array_index[0:-1] + (slice(0, 1),)
                        zg = ds[sid2p(Sweep.Z_SET, port_index, 0)][...][lf_index]
                        vb = ds[sid2p(Sweep.V_SET, port_index, 0)][...][lf_index]
                        ia = th.zeros_like(zg)
                        for harm_index in range(1, Settings().f_points):
                            rf_index = self.array_index[0:-1] + (slice(harm_index, harm_index+1),)
                            g = ds[sid2p(Sweep.G_SET, port_index, harm_index)][...][rf_index]
                            b = th.zeros_like(g)
                            a = ds[sid2p(Sweep.A_SET, port_index, harm_index)][...][rf_index]
                            vb, ia, zg = th.cat((vb, b), -1), th.cat((ia, a), -1), th.cat((zg, g), -1)
                        viz_bag[port_index] = [vb.reshape(step_shape), ia.reshape(step_shape), zg.reshape(step_shape)]
            self.i += 1
            return i, viz_bag
        else:
            raise StopIteration()

    def save(self, viz_bag, aux):
        ds = self.dataset
        num_harmonics = Settings().num_harmonics
        array_index = self.array_index
        array_shape = tuple([shape if isinstance(index, slice) else 1 for index, shape in zip(array_index, ds.sweep_shape)])

        for port_index in ds.ports:
            vb, ia, zg = viz_bag[port_index]
            shape_ = array_shape[0:-1] + (num_harmonics + 1,)
            vb = vb.detach().reshape(shape_)
            ia = ia.detach().reshape(shape_)
            zg = zg.detach().reshape(shape_)
            ds[rid2p(Response.V_GET, port_index)][array_index] = vb
            ds[rid2p(Response.I_GET, port_index)][array_index] = ia
            ds[rid2p(Response.Z_GET, port_index)][array_index] = zg
            ds[rid2p(Response.B_GET, port_index)][array_index] = vb
            ds[rid2p(Response.A_GET, port_index)][array_index] = ia
            ds[rid2p(Response.G_GET, port_index)][array_index] = zg
        array_index = self.array_index[0:-2] + (slice(None, ),)*3
        array_shape = array_shape[0:-2]
        freq, pm, sa, sp = aux
        freq = freq.detach().reshape(array_shape + response_shape_map[Response.SS_FREQ])
        pm = pm.detach().reshape(array_shape + response_shape_map[Response.P])
        sa = sa.detach().reshape(array_shape + response_shape_map[Response.PSD])
        sp = sp.detach().reshape(array_shape + response_shape_map[Response.SP])
        # ds[rid2p(Response.SS_FREQ)].__setitem__(array_index, freq)
        # ds[rid2p(Response.P)].__setitem__(array_index, pm)
        # ds[rid2p(Response.PSD)].__setitem__(array_index, sa)
        # ds[rid2p(Response.SP)].__setitem__(array_index, sp)


class BaseWCArrayGroup(h5.Group):

    def __init__(self, bind):
        super(BaseWCArrayGroup, self).__init__(bind)

    def __getitem__(self, item):
        item = super(BaseWCArrayGroup, self).__getitem__(item)
        if isinstance(item, h5.Dataset):
            item = WCArray(item.id)
        return item

    def __setitem__(self, item, value):
        if isinstance(item, WCArray):
            item = h5.Dataset(item.id)
        super(BaseWCArrayGroup, self).__setitem__(item, value)


class SweepMapGroup(BaseWCArrayGroup):
    pass


class IndepMapGroup(BaseWCArrayGroup):
    pass


class DatasetModel(BaseWCArrayGroup):
    """Database representation of a Dataset
    """

    @property
    def sweep_map(self):
        return SweepMapGroup(self["sweep_map"].id)

    @property
    def sweep_shape(self):
        return self.attrs["sweep_shape"]

    @property
    def indep_map(self):
        return IndepMapGroup(self["indep_map"].id)

    @property
    def ports(self):
        return self.attrs["ports"]

    @property
    def duts(self):
        return self.attrs["duts"]

    @property
    def videos(self):
        return self.attrs["videos"]

    @property
    def time(self):
        return self["time"]

    @property
    def freq(self):
        return self["freq"]

    @property
    def freq_m(self):
        return self["freq_m"]

    @property
    def time_c(self):
        return self["time_c"]

    def add(self, name, value):
        """ Add new dataset.

        Parameters
        ----------
        name : str
            Equation name.
        value : th.Tensor

        """
        v_dtype = th_2_np_dtype_map[value.dtype]
        v = WCArray.create_array(self, name, value.shape, dtype=v_dtype, data=value)
        return v

    def has_equation(self, name):
        """ Returns true if dataset has existing equation name.

        Parameters
        ----------
        name : str
            Equation name.

        Returns
        -------
        bool
            True if dataset has equation name, else False.

        """
        return name in self

    def equation(self, name):
        """ Gets the equation by name.

        Parameters
        ----------
        name : str
            Equation name.

        """
        return self[name]

    def set_equation(self, name, value):
        """ Sets the equation by name.

        Parameters
        ----------
        name : str
            Equation name.

        """
        self[name][...] = value

    def remove(self, name):
        """ Remove the equation by name.

        Parameters
        ----------
        name : str
            Equation name.

        """
        del self[name]


class DatagroupModel(H5File):
    """Database representation of a Datagroup

    Parameters
    ----------
    name
            Name of the file on disk, or file-like object.  Note: for files
            created with the 'core' driver, HDF5 still requires this be
            non-empty.
    mode
        r        Readonly, file must exist (default)
        r+       Read/write, file must exist
        w        Create file, truncate if exists
        w- or x  Create file, fail if exists
        a        Read/write if exists, create otherwise
    driver
        Name of the driver to use.  Legal values are None (default,
        recommended), 'core', 'sec2', 'stdio', 'mpio', 'ros3'.

    See Also
    --------
    h5py.File
    """

    def __init__(self,  name=None, **kwargs):
        if not name:
            name = os.sep.join([Settings().data_root, "datagroups", Settings().datagroup + ".h5"])
        super(DatagroupModel, self).__init__(name, **kwargs)

    def add(self, name, ports=tuple(), duts=tuple(), mipis=tuple(), videos=tuple(),
            sweep_map=OrderedDict(), indep_map=OrderedDict(),
            **kwargs):
        """ Add new dataset.

        Parameters
        ----------
        name : str
            Dataset name.
        ports : tuple
            Ports to be included in measurement.
        duts : tuple
            DUTS to be included in measurement.
        mipi : tuple
            MIPIs to be included in measurement.
        video : tuple
            Videos to be included in measurement.
        sweeep_map : dict
            Parametric sweeps stored inside the dataset.
        indep_map : dict
            Single measurement stored inside the dataset

        """
        sweep_names = []
        sweep_shape = []
        for index, (k, v) in enumerate(reversed(sweep_map.items())):
            sweep_names.append(k.encode('utf-8'))
            sweep_shape.append(v.shape[index])
        ds = DatasetModel(self.create_group(name, **kwargs).id)
        ds.attrs["ports"] = ports if len(ports) else tuple(range(0, Settings().num_ports+1))
        ds.attrs["duts"] = duts if len(duts) else tuple(range(0, Settings().num_duts))
        ds.attrs["mipis"] = mipis if len(mipis) else tuple(range(0, Settings().num_mipi))
        ds.attrs["videos"] = videos if len(videos) else tuple(range(0, Settings().num_video))
        ds.attrs["sweep_names"] = sweep_names
        ds.attrs["sweep_shape"] = sweep_shape
        sweep_group = SweepMapGroup(ds.create_group("sweep_map", track_order=True).id)
        for index, (k, v) in enumerate(reversed(sweep_map.items())):
            v_dtype = th_2_np_dtype_map[v.dtype]
            fill = th.zeros(sweep_shape, dtype=v.dtype)
            WCArray.create_array(ds, k, sweep_shape, dtype=v_dtype)
            ds[k][...] = v.detach() + fill
            sweep_group[k] = h5.SoftLink(f"{ds.name}/{k}")
        indep_group = IndepMapGroup(ds.create_group("indep_map", track_order=True).id)
        for index, (k, v) in enumerate(reversed(indep_map.items())):
            v_dtype = th_2_np_dtype_map[v.dtype]
            fill_shape = [1]*(len(sweep_shape))
            fill_shape[-len(v.shape)] = v.numel()
            WCArray.create_array(ds, k, fill_shape, dtype=v_dtype)
            ds[k][...] = v.reshape(fill_shape).detach()
            indep_group[k] = h5.SoftLink(f"{ds.name}/{k}")

        for resp_id in (Response.V_GET, Response.I_GET, Response.Z_GET, Response.B_GET, Response.A_GET, Response.G_GET):
            for port_index in ds.ports:
                k = rid2p(resp_id, port_index)
                resp_shape = sweep_shape[0:-2] + list(response_shape_map[resp_id])
                resp_dtype = th_2_np_dtype_map[response_dtype_map[resp_id]]
                WCArray.create_array(ds, k, resp_shape, dtype=resp_dtype)
                ds[k][...] = th.zeros(resp_shape, dtype=response_dtype_map[resp_id]).detach()

        if "sp_fund" in ds and "sp_harm" in ds and "sp_port" in ds:
            # (sp_harm*sp_fund, sp_port, sp_port)
            k = 's'
            s_shape = th.prod(th.as_tensor(ds.sweep_shape[-4:-2])), ds.sweep_shape[-5], ds.sweep_shape[-5]
            s_dtype = th_2_np_dtype_map[th.complex128]
            WCArray.create_array(ds, k, s_shape, dtype=s_dtype)
            ds[k][...] = th.zeros(s_shape, dtype=th.complex128).detach()
        return ds
    
    def __getitem__(self, item):
        item = super(DatagroupModel, self).__getitem__(item)
        if isinstance(item, h5.Group):
            item = DatasetModel(item.id)
        return item

    def __setitem__(self, item, value):
        if isinstance(item, DatasetModel):
            item = h5.Group(item.id)
        super(DatagroupModel, self).__setitem__(item, value)

    def has_dataset(self, name):
        """ Returns true if datagroup has existing dataset name.

        Parameters
        ----------
        name : str
            Dataset name.

        Returns
        -------
        bool
            True if datagroup has dataset name, else False.

        """
        return name in self

    def dataset(self, name):
        """ Gets the dataset by name.

        Parameters
        ----------
        name : str
            Dataset name.

        Returns
        -------
        DatasetModel
            The selected dataset.

        """
        return DatasetModel(self[name].id)

    def remove(self, name):
        """ Remove the dataset by name.

        Parameters
        ----------
        name : str
            Dataset name.

        """
        del self[name]


class DatagroupTreeModel(QStandardItemModel):
    """The equation table Model.

        Parameters
        ----------
        root : OrderedDict
            The dictionary of items that populate the equation table.
    """
    def __init__(self, parent=None, root={}):
        super(DatagroupTreeModel, self).__init__(parent)
        self.header = ['Datagroups']
        self._root = root
        self._selected_names = []
        self._selected_values = []
        self._selected_markers = []
        self.__marker_cycle = cycle(MarkerStyle.filled_markers)
        for k, v in self._root.keys():
            self.appendRow(k, v)

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        if index.child(0, 0).row() == -1:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        else:
            return Qt.ItemIsEnabled

    def appendRow(self, dg_name, dg, dg_model):
        base_name = dg_name
        count = 0
        dg_name = base_name
        while dg_name in dg_model:
            count += 1
            dg_name = "%s%d" % (base_name, count)
        dg_item = QStandardItem(dg_name)
        super(DatagroupTreeModel, self).appendRow(dg_item)
        for ds_name, ds in dg.root._v_children.items():
            if not ds_name.startswith("_"):
                name = ".".join((dg_name, ds_name))
                marker = self.__marker_cycle.__next__()
                icon_filename = os.sep.join((Settings().root, "icons/markers/", MarkerStyle.markers[marker] + ".png"))
                ds_item = QStandardItem(QIcon(icon_filename), ds_name)
                ds_item.setData(marker, Qt.UserRole)
                dg_item.appendRow(ds_item)
                self._root[name] = ds
        dg_model[dg_name] = dg

    def removeRow(self, index, parent, dg_model):
        dg_name = index.data(Qt.DisplayRole)
        super(DatagroupTreeModel, self).removeRow(index.row(), parent)
        for ds_name, ds in dg_model[dg_name].root._v_children.items():
            if not ds_name.startswith("_"):
                name = ".".join((dg_name, ds_name))
                self._root.pop(name)
        dg_model[dg_name].close()
        dg_model.pop(dg_name)

    def selected(self):
        """
            Returns
            -------
            ndarray
                The selected dictionary value based on the selected row.
        """
        return self._selected_names, self._selected_values, self._selected_markers

    @QtCore.Slot(int)
    def set_selected(self, indices):
        """ Set the selected dictionary value

            Parameters
            ----------
            index : QtCore.QModelIndex
                The table row to be selected.
        """
        self._selected_names.clear(), self._selected_values.clear(), self._selected_markers.clear()
        for index in indices:
            item = self.itemFromIndex(index)
            name = ".".join((item.parent().text(), item.text()))
            self._selected_names.append(name)
            self._selected_values.append(self._root[name])
            self._selected_markers.append(index.data(Qt.UserRole))


if __name__ == "__main__":
    from collections import OrderedDict
    sweep_map = OrderedDict((("a_1", th.arange(0, 10, dtype=th.float64)),))
    indep_map = OrderedDict((("freq", Settings().freq.reshape(1, -1)), ("time", Settings().time.reshape(-1, 1)),))
    dg = DatagroupModel("dg.h5", mode="w")

    ds1 = dg.add("ds1")
    v1 = ds1["v_1"]

    # ds2 = dg.add("ds2", sweep_map=indep_map, indep_map=indep_map)
    # time = ds2.indep_map["time"]
    #
    # ds2 = dg.add("ds2", sweep_map=sweep_map, indep_map=indep_map)
    # a_1 = ds2.sweep_map["a_1"]



