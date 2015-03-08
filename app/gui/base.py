from PyQt4 import QtGui
from PyQt4.QtGui import QWidget

__author__ = 'calou'


class Window(QWidget):
    def setTitle(self, patients_):
        title = QtGui.QLabel(patients_)
        font = title.font()
        font.setPointSize(24)
        title.setFont(font)
        return title