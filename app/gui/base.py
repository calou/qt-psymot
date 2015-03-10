from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFontDatabase


class Window(QWidget):
    def setTitle(self, title_text):
        title = QLabel(title_text)
        font_families = QFontDatabase().families()
        title.setStyleSheet("font-family: 'Source Sans Pro'; font-weight:200; font-size:26px; padding-left:0px;")
        title.setContentsMargins(0, 0, 0, 10)
        return title
