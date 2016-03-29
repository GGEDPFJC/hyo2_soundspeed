from __future__ import absolute_import, division, print_function, unicode_literals

import os
import logging

logger = logging.getLogger(__name__)

here = os.path.abspath(os.path.dirname(__file__))


def get_testing_data_folder():
    data_folder = os.path.abspath(os.path.join(here, os.pardir, os.pardir, "data", "downloaded"))
    if not os.path.exists(data_folder):
        raise RuntimeError("The testing folder does not exist: %s" % data_folder)
    return data_folder


def get_testing_data_subfolders():
    df = get_testing_data_folder()
    return [o for o in os.listdir(df) if os.path.isdir(os.path.join(df, o))]


class FileManager(object):

    def __init__(self, data_path, mode):
        """Open the passed file and store related info"""

        self._path = os.path.abspath(data_path)
        if not os.path.exists(self._path):
            raise RuntimeError('the passed file does not exist: %s' % self._path)
        self._io = open(self._path, mode=mode)
        self._basename = os.path.basename(self._path).split('.')[0]
        self._ext = os.path.basename(self._path).split('.')[-1]

    @property
    def path(self):
        return self._path

    @property
    def basename(self):
        return self._basename

    @property
    def ext(self):
        return self._ext

    @property
    def io(self):
        return self._io

    @property
    def lines(self):
        return self._lines

    def __repr__(self):
        msg = "<%s:%s:%s>" % (self.__class__.__name__, self._basename, self._ext)

        return msg