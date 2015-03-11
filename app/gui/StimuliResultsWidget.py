# -*- coding: utf8 -*-

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from app.model.stimuli import *
from app.gui.widget import *
from app.gui.DisplayStimuliSessionResultsDesignWidget import Ui_Form

BIG_TEXT_STYLESHEET = "font-size:48px;"
MEDIUM_TEXT_STYLESHEET = "font-size:32px;"
BIG_RESULT_STYLESHEET = "font-size:120px; font-weight:500;"
MEDIUM_RESULT_STYLESHEET = "font-size:64px; font-weight:500;"


class DisplayStimuliSessionResultsDesignWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(DisplayStimuliSessionResultsDesignWidget, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.correct_responses_percentage_text.setStyleSheet(BIG_TEXT_STYLESHEET)
        self.response_time_text.setStyleSheet(BIG_TEXT_STYLESHEET)
        self.correct_invalid_responses_percentage_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET)
        self.correct_valid_responses_percentage_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET)
        self.min_response_time_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET)
        self.max_response_time_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET)

        self.correct_response_percentage.setStyleSheet(BIG_RESULT_STYLESHEET)
        self.response_time.setStyleSheet(BIG_RESULT_STYLESHEET)
        self.correct_valid_response_percentage.setStyleSheet(MEDIUM_RESULT_STYLESHEET)
        self.correct_invalid_response_percentage.setStyleSheet(MEDIUM_RESULT_STYLESHEET)
        self.min_response_time.setStyleSheet(MEDIUM_RESULT_STYLESHEET)
        self.max_response_time.setStyleSheet(MEDIUM_RESULT_STYLESHEET)

    @pyqtSlot(StimuliTestingSession)
    def set_testing_session(self, testing_session):
        testing_session.compute_results()
        self.correct_response_percentage.setText("%d%%" % testing_session.get_correct_responses_percentage())
        self.correct_valid_response_percentage.setText("%d%%" % testing_session.get_correct_valid_responses_percentage())
        self.correct_invalid_response_percentage.setText("%d%%" % testing_session.get_correct_invalid_responses_percentage())
        self.response_time.setText("%d ms" % testing_session.average_response_time)
        self.min_response_time.setText("%d ms" % testing_session.min_response_time)
        self.max_response_time.setText("%d ms" % testing_session.max_response_time)