from PyQt5.QtWidgets import *
from app.gui.design.StylesheetHelper import *

class Window(QWidget):
    def setTitle(self, title_text):
        title_widget = QLabel(self)
        title_widget.setText(title_text)
        title_widget.setStyleSheet(BIG_TEXT_STYLESHEET+DARK_COLOR)
        title_widget.setContentsMargins(0, 0, 0, 10)
        title_widget.setGeometry(30, 30, 840, 50)
        return title_widget


class DummyWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
