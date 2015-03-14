# -*- coding: utf8 -*-

from PyQt5 import QtWidgets
from PyQt5 import QtSvg
from PyQt5 import QtGui, QtCore
# from app.gui.design.window.HomeSectionDesign import *
from PyQt5.QtWidgets import QSizePolicy
from app.gui.design.StylesheetHelper import *


class HomeSection(QtWidgets.QWidget):
    def __init__(self, button_text, background_image):
        super(HomeSection, self).__init__()
        self.background_image = background_image

        frame = QtWidgets.QFrame(self)
        frame.setGeometry(0, 0, 440, 250)
        frame.setStyleSheet(DARK_GREY_BACKGROUND + NO_BORDER)

        self.svgBackground = QtSvg.QSvgRenderer(self)
        self.svgBackground.setViewBox(QtCore.QRectF(0, 0, frame.width(), frame.height()))

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText(button_text)
        self.pushButton.setGeometry(210, 208, 220, 32)
        self.pushButton.setStyleSheet(GREY_BACKGROUND)

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter()
        painter.begin(self)

        self.svgBackground.load(self.background_image)
        painter.setPen(QtGui.QColor(168, 34, 3))
        self.svgBackground.render(painter, QtCore.QRectF(0, 0, 440, 250))
        painter.end()