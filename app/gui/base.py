from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def setTitle(self, patients_):
        title = QtWidgets.QLabel(patients_)
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)
        title.setContentsMargins(0, 0, 0, 10)
        return title