# -*- coding: utf8 -*-
from PyQt4 import QtSvg, QtGui
from gui.design.StylesheetHelper import *


class HomeSection(QtGui.QWidget):
    def __init__(self, button_texts, background_image):
        super(HomeSection, self).__init__()
        self.background_image = background_image

        frame = QtGui.QFrame(self)
        frame.setGeometry(0, 0, 440, 250)
        frame.setStyleSheet(DARK_GREY_BACKGROUND + NO_BORDER)
        self.background_widget = QtSvg.QSvgWidget(self)
        self.background_widget.load(background_image)
        self.background_widget.setGeometry(0, 0, 250, 250)

        self.push_buttons = []
        for i in range(len(button_texts)):
            button = QtGui.QPushButton(self)
            button.setText(button_texts[i])
            button.setGeometry(210, (208 - 40 * i), 220, 32)
            self.push_buttons.append(button)
