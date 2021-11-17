import os.path
import sys
import six

from Qt import QtWidgets, QtCompat, QtCore

if six.PY2:
    from pathlib2 import Path
    import inspect2
else:
    from pathlib import Path
    import inspect

from lib import path_functions as pf
from engine.engine_base import BaseEngine
from engine.engine_maya import MayaEngine
from engine.engine_houdini import HoudiniEngine

ui_path = Path(__file__).parent / 'qt' / 'file_explorer.ui'


class ToolWindow(QtWidgets.QMainWindow):
    curr_engine = None

    def __init__(self):
        super(ToolWindow, self).__init__()
        self.curr_engine = BaseEngine.get_engine()

        if self.curr_engine is None:
            print("Engine not defined")
            return

        self.generateUI()

    def generateUI(self):
        QtCompat.loadUi(str(ui_path), self)
        self.field_curr_dir.setText(sys.executable)
        self.field_curr_dir.textChanged.connect(self.currentDirChanged)
        self.button_change_dir.clicked.connect(self.showFolderSelectionDialog)

        self.generateButtons()

    def generateButtons(self):
        for f in self.curr_engine.implements:
            method = getattr(self.curr_engine, f)
            if six.PY2:
                params = inspect2.signature(method)
            else:
                params = inspect.signature(method)

            button = QtWidgets.QPushButton(str(f).upper())
            button.clicked.connect(lambda m=method, p=params: self.generatedButtonClicked(m, p))
            self.verticalLayout.addWidget(button)
            button.show()

    def generatedButtonClicked(self, method, params):
        selected_file = self.list_file.currentItem().data(QtCore.Qt.UserRole)
        method(selected_file)

    def currentDirChanged(self):
        self.populateFileList()

    def showFolderSelectionDialog(self):
        folder_dialog = QtWidgets.QFileDialog(self)
        folder_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        folder_dialog.setViewMode(QtWidgets.QFileDialog.Detail)

        if folder_dialog.exec_():
            dir_name = folder_dialog.directory().absolutePath()
            self.field_curr_dir.setText(dir_name)

    def populateFileList(self):
        self.list_file.clear()
        dir_name = self.field_curr_dir.toPlainText()
        for f in pf.getFiles(dir_name, self.curr_engine.valid_extensions):
            self.addListWidgetItem(self.list_file, f, os.path.basename(f))

    def addListWidgetItem(self, list_widget, data, label):
        item = QtWidgets.QListWidgetItem()
        item.setData(QtCore.Qt.UserRole, data)
        item.setText(label)
        list_widget.addItem(item)
        return item


if __name__ == '__main__':

    curr_engine = BaseEngine.get_engine()

    if curr_engine is None:
        print("Engine not defined")
    else:
        app = QtWidgets.QApplication([])
        t = ToolWindow()
        t.show()
        app.exec_()
