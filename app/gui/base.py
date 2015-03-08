from PyQt5 import QtWidgets

__author__ = 'calou'


class Window(QtWidgets.QWidget):
    def setTitle(self, patients_):
        title = QtWidgets.QLabel(patients_)
        font = title.font()
        font.setPointSize(24)
        title.setFont(font)
        return title