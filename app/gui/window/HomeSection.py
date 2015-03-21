# -*- coding: utf8 -*-
from PyQt4 import QtSvg, QtGui, Qt
from gui.design.StylesheetHelper import *


class HomeSection(QtGui.QWidget):
    def __init__(self, button_texts, background_image):
        super(HomeSection, self).__init__()
        self.background_image = background_image

        self.setMinimumSize(440, 250)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        self.background_widget = QtSvg.QSvgWidget(self)
        self.background_widget.load(background_image)

        self.push_buttons = []
        button_layout = QtGui.QVBoxLayout()
        for i in range(len(button_texts)):
            button = QtGui.QPushButton(self)
            button.setText(button_texts[i])
            self.push_buttons.append(button)
            button_layout.addWidget(button, 1)


    def resizeEvent(self, ev):
        w = self.width()
        h = self.height()

        for i in range(len(self.push_buttons)):
            button = self.push_buttons[i]
            button.setGeometry(Qt.QRect(w - 230, h - (45 + i * 35), 220, 32))

        m = min(w, h)
        self.background_widget.setGeometry(Qt.QRect((w - m) / 2, (h - m) / 2, m, m))