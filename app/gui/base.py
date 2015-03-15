from PyQt5 import QtWidgets
from app.gui.design.StylesheetHelper import *

class Window(QtWidgets.QWidget):

    def init(self, root_widget, title):
        self.root_widget = root_widget
        self.set_title(title)
        self.init_back_button()

    def set_title(self, title_text):
        title_widget = QtWidgets.QLabel(self)
        title_widget.setText(title_text)
        title_widget.setStyleSheet(BIG_TEXT_STYLESHEET+DARK_COLOR)
        title_widget.setContentsMargins(0, 0, 0, 10)
        title_widget.setGeometry(30, 30, 840, 50)
        return title_widget

    def init_back_button(self):
        back_button = QtWidgets.QPushButton(self)
        back_button.setText("Retour")
        back_button.setGeometry(10, 560, 160, 32)
        back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.root_widget.display()

class DummyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
