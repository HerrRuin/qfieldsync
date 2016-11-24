import os
import inspect
from qgis.PyQt import QtGui
from functools import partial
import importlib


def selectFolder(lineEditWidget):
    lineEditWidget.setText(QtGui.QFileDialog.getExistingDirectory(directory=lineEditWidget.text()))


def make_folder_selector(widget):
    return partial(selectFolder, lineEditWidget=widget)


def get_ui_class(ui_file):
    """Get UI Python class from .ui file.
       Can be filename.ui or subdirectory/filename.ui
    :param ui_file: The file of the ui in safe.gui.ui
    :type ui_file: str
    """
    m = importlib.import_module("qfieldsync.ui." + ui_file + '_ui4')
    return [obj for _, obj in inspect.getmembers(m) if inspect.isclass(obj) and obj.__name__[:3] == 'Ui_'][0]

