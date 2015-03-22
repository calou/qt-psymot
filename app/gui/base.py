from PyQt4 import QtGui, Qt
from gui.design.StylesheetHelper import *


class Window(QtGui.QWidget):
    def init(self, root_widget, title):
        self.root_widget = root_widget
        self.set_title(title)
        self.back_button = QtGui.QPushButton(self)
        self.init_back_button()

    def set_title(self, title_text):
        title_widget = QtGui.QLabel(self)
        title_widget.setText(title_text)
        title_widget.setStyleSheet(BIG_TEXT_STYLESHEET + DARK_COLOR)
        title_widget.setContentsMargins(0, 0, 0, 10)
        title_widget.setGeometry(30, 30, 840, 50)
        return title_widget

    def init_back_button(self):
        self.back_button.setText("Retour")
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.root_widget.display()

    def on_resize(self):
        h = self.height()
        self.back_button.setGeometry(10, h - 42, 160, 32)

    def get_right_button_geometry(self):
        h = self.height()
        w = self.width()
        return Qt.QRect(w - 170, h - 42, 160, 32)

    def get_central_geometry(self):
        h = self.height()
        w = self.width()
        return Qt.QRect(30, 90, w - 60, h - 142)


class DummyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(QtGui.QWidget, self).__init__(parent)
