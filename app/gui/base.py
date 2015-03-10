from PyQt5.QtWidgets import *

class Window(QWidget):
    def setTitle(self, title_text):
        title = QLabel(title_text)
        title.setStyleSheet("font-family: 'Source Sans Pro'; font-weight:100; font-size:26px; padding-left:0px; color: #CCCCCC;")
        title.setContentsMargins(0, 0, 0, 10)
        return title
