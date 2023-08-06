import h5py as h5


class H5File(h5.File):

    def __init__(self, name, *args, **kwds):
        super(H5File, self).__init__(name, *args, **kwds)
        self._filename = name

    @property
    def filename(self):
        return self._filename