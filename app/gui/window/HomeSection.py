# -*- coding: utf8 -*-

from PyQt5 import QtWidgets
from app.gui.design.window.HomeSectionDesign import *
from app.model.stimuli import *
from app.gui.design.StylesheetHelper import *

class HomeSection(QtWidgets.QWidget, Ui_HomeSectionDesign):
    testing_session_completed = QtCore.pyqtSignal(StimuliTestingSession, name='testingSessionCompleted')

    def __init__(self, button_text, background_image):
        super(HomeSection, self).__init__()
        self.setupUi(self)
        self.frame.setStyleSheet(DARK_GREY_BACKGROUND+NO_BORDER)
        self.pushButton.setText(button_text)
        self.pushButton.setStyleSheet(GREY_BACKGROUND)