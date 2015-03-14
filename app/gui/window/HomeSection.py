# -*- coding: utf8 -*-
from PyQt5 import QtWidgets
from PyQt5 import QtSvg
from PyQt5 import QtGui, QtCore
from app.gui.design.StylesheetHelper import *

class HomeSection(QtWidgets.QWidget):
    def __init__(self, button_text, background_image):
        super(HomeSection, self).__init__()
        self.background_image = background_image

        frame = QtWidgets.QFrame(self)
        frame.setGeometry(0, 0, 440, 250)
        frame.setStyleSheet(DARK_GREY_BACKGROUND + NO_BORDER)
        self.background_widget = QtSvg.QSvgWidget(self)
        self.background_widget.load(background_image)
        self.background_widget.setGeometry(45, 0, 250, 250)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText(button_text)
        self.pushButton.setGeometry(210, 208, 220, 32)