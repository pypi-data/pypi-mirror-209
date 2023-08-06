"""
==================================================
Equation (:mod:`sknrf.model.dataviewer.equation`)
==================================================

This module stores custom post-measurement calculations inside a dataset.

See Also
--------
sknrf.model.dataviewer.dataset.DatagroupModel, sknrf.model.dataviewer.dataset.DatasetModel

"""

import re
import logging

from PySide6 import QtCore
from PySide6.QtCore import Qt, QAbstractTableModel
import torch as th
import h5py as h5
from toposort import toposort_flatten

__author__ = 'dtbespal'
logger = logging.getLogger(__name__)


class DatasetEquationModel(object):
    """Dataset Equation Model

    A temporary dataset attribute defined by:
        * A string name
        * A string expression in terms of current dataset attributes that evaluates to a value using the built-in eval() function.

    Parameters
    ----------
    dataset : DatasetModel
        Reference to the current dataset.
    name : str
        Name of the dataset equation.

    """
    _eval_order = []
    _eval_map = {}

    def __init__(self, dataset, name="Untitled"):
        super(DatasetEquationModel, self).__init__()
        index = 1
        self.name = name
        while dataset.__contains__(self.name):
            self.name = name + str(index)
            index += 1
        self.eqn = "0"
        self._eqn = "0"
        self.is_valid = False
        self.eval(dataset, eqn=self.eqn)

    def eval(self, dataset, eqn=""):
        """Evaluate the Dataset Equation expression based on attributes in the current dataset

        Parameters
        ----------
        dataset : str
            Reference to the current dataset.
        eqn : str
            A string expression in terms of current dataset attributes that evaluates to a value using the built-in eval() function.

        """
        if eqn:
            if "__" in eqn:
                raise ValueError("Invalid equation character sequence")
            _eqn = eqn
            eqn_refs = re.findall(r"\.(\w+)", _eqn)
            for eqn_ref in eqn_refs:
                if '[' not in eqn_ref:
                    _eqn = _eqn.replace(eqn_ref, eqn_ref + "[...]")
            _eqn, _ = re.subn(r"\.(\w+)((?=\[.+\]))", r'dataset["\1"]\2', _eqn)
            self.eqn, self._eqn = eqn, _eqn
            DatasetEquationModel._eval_map[self.name] = set(re.findall(r"\.(\w+)", self.eqn))
            DatasetEquationModel._eval_order = toposort_flatten(DatasetEquationModel._eval_map)
        try:
            r_val = eval(self._eqn, {'__builtins__': {}}, {"dataset": dataset})
            if isinstance(r_val, (h5.Dataset)):
                raise TypeError("Database Equation cannot be accessed without indexation.")
        except (SyntaxError, TypeError, NameError, AttributeError, ValueError):
            self.is_valid = False
            logger.error("Invalid Equation: %s = %s", self.name, self.eqn, exc_info=True)
            raise
        else:
            self.is_valid = True
            if not isinstance(r_val, th.Tensor):
                r_val = th.as_tensor(r_val)
            if len(r_val.shape) == 0:
                r_val = r_val.unsqueeze(0)
            return r_val


class EquationTableModel(QAbstractTableModel):
    """The equation table Model.

        Parameters
        ----------
        root : OrderedDict
            The dictionary of items that populate the equation table.
    """
    def __init__(self, root, parent=None):
        super(EquationTableModel, self).__init__(parent)
        self.header = ["Variable", "Shape", "Unit"]
        self._root = root
        self._num_rows = 0
        self._num_cols = 3
        self._selected_row = 0
        self._selected_name = ""
        self._selected_value = None
        self._selected_shape = tuple()
        self._selected_unit = ""
        self._row_key_map = {}
        self.shape_map = dict.fromkeys(tuple(root.keys()), "")
        self.unit_map = dict.fromkeys(tuple(root.keys()), "")
        for k, v in self._root.items():
            if hasattr(v, "data"):
                self._row_key_map[self._num_rows] = k
                self.shape_map[k] = v[...].shape
                self.unit_map[k] = ""
                self._num_rows += 1

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def rowCount(self, parent):
        return self._num_rows

    def columnCount(self, parent):
        return self._num_cols

    def selected(self):
        """
            Returns
            -------
            ndarray
                The selected dictionary value based on the selected row.
        """
        return self._selected_row, self._selected_name, self._selected_value, self._selected_shape, self._selected_unit

    @QtCore.Slot(int)
    def set_selected(self, index):
        """ Set the selected dictionary value

            Parameters
            ----------
            index : QtCore.QModelIndex
                The table row to be selected.
        """
        index = index.row()
        self._selected_row = index
        self._selected_name = self._row_key_map[index]
        self._selected_value = self._root[self._row_key_map[index]]
        self._selected_shape = self.shape_map[self._row_key_map[index]]
        self._selected_unit = self.unit_map[self._row_key_map[index]]

    def data(self, index, role=Qt.DisplayRole):
        """ Get the table data.

            Parameters
            ----------
            index : QtCore.QModelIndex
                The table index to get.
            role : Qt.DisplayRole, optional
                The requested data role to get.

            Returns
            -------
            QtCore.QVariant :
                The return type is determined by the data role.

        """
        if not index.isValid():
            return None
        row, col = index.row(), index.column()
        if role == Qt.DisplayRole:
            key = self._row_key_map[row]
            if col == 0:
                return key
            elif col == 1:
                return str(self.shape_map[key])
            elif col == 2:
                return self.unit_map[key]
        else:
            return None

