# -*- coding: utf8 -*-

from PyQt5.QtCore import pyqtSlot

from app.model.stimuli import *
from app.gui.widget import *
from app.gui.stimuli.design.ResultsDesign import Ui_ResultWidget


BIG_TEXT_STYLESHEET = "font-size:48px;color:#555a5a;"
MEDIUM_TEXT_STYLESHEET = "font-size:32px;color:#555a5a;"
BIG_RESULT_STYLESHEET = "font-size:120px; font-weight:500;"
MEDIUM_RESULT_STYLESHEET = "font-size:64px; font-weight:500;"


class ResultsWidget(QtWidgets.QWidget, Ui_ResultWidget):
    def __init__(self):
        super(ResultsWidget, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.correct_responses_percentage_text.setStyleSheet(BIG_TEXT_STYLESHEET)
        self.response_time_text.setStyleSheet(BIG_TEXT_STYLESHEET)
        self.correct_forbidden_responses_percentage_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET)
        self.correct_authorized_responses_percentage_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET)
        self.min_response_time_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET)
        self.max_response_time_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET)

        self.correct_response_percentage.setStyleSheet(BIG_RESULT_STYLESHEET)
        self.response_time.setStyleSheet(BIG_RESULT_STYLESHEET)
        self.correct_authorized_response_percentage.setStyleSheet(MEDIUM_RESULT_STYLESHEET)
        self.correct_forbidden_response_percentage.setStyleSheet(MEDIUM_RESULT_STYLESHEET)
        self.min_response_time.setStyleSheet(MEDIUM_RESULT_STYLESHEET)
        self.max_response_time.setStyleSheet(MEDIUM_RESULT_STYLESHEET)

    @pyqtSlot(StimuliTestingSession)
    def set_testing_session(self, ts):
        ts.compute_results()
        self.correct_response_percentage.setText("%d%%" % ts.get_correct_responses_percentage())
        self.correct_authorized_response_percentage.setText("%d%%" % ts.get_correct_authorized_responses_percentage())
        self.correct_forbidden_response_percentage.setText("%d%%" % ts.get_correct_forbidden_responses_percentage())

        avg_rt = "%d ms" % ts.average_response_time if ts.average_response_time > 0 else "N.D."
        self.response_time.setText(avg_rt)

        min_rt = "%d ms" % ts.min_response_time if ts.max_response_time > ts.min_response_time else "N.D."
        self.min_response_time.setText(min_rt)

        max_rt = "%d ms" % ts.max_response_time if ts.max_response_time > 0 else "N.D."
        self.max_response_time.setText(max_rt)
