# -*- coding: utf8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets

from app.model.stimuli import *
from app.gui.button import *
from app.gui.design.StylesheetHelper import *
from app.gui.stimuli.design.ResultsDesign import Ui_ResultWidget
from app.db.StimuliRepositories import *


class ResultsWidget(QtWidgets.QWidget, Ui_ResultWidget):
    def __init__(self):
        super(ResultsWidget, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.correct_responses_percentage_text.setStyleSheet(BIG_TEXT_STYLESHEET + DARK_COLOR)
        self.response_time_text.setStyleSheet(BIG_TEXT_STYLESHEET + DARK_COLOR)
        self.correct_forbidden_responses_percentage_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET + DARK_COLOR)
        self.correct_authorized_response_number.setStyleSheet(SMALL_TEXT_STYLESHEET)
        self.correct_authorized_responses_percentage_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET + DARK_COLOR)
        self.correct_forbidden_response_number.setStyleSheet(SMALL_TEXT_STYLESHEET)
        self.min_response_time_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET + DARK_COLOR)
        self.max_response_time_text.setStyleSheet(MEDIUM_TEXT_STYLESHEET + DARK_COLOR)

        self.response_time.setStyleSheet(BIG_RESULT_STYLESHEET)
        self.min_response_time.setStyleSheet(MEDIUM_RESULT_STYLESHEET)
        self.max_response_time.setStyleSheet(MEDIUM_RESULT_STYLESHEET)

    @staticmethod
    def set_percentage(text, value, colorless_stylesheet):
        text.setText("%d%%" % value)
        colored_stylesheet = colorless_stylesheet
        if value > 80:
            colored_stylesheet += GREEN_COLOR
        elif value > 60:
            colored_stylesheet += ORANGE_COLOR
        else:
            colored_stylesheet += RED_COLOR
        text.setStyleSheet(colored_stylesheet)

    @pyqtSlot(StimuliTestingSession)
    def set_testing_session(self, ts):
        ts.compute_results()
        repository = SessionRepository()
        repository.save(ts)
        self.set_percentage(self.correct_response_percentage, ts.get_correct_responses_percentage(),
                            BIG_RESULT_STYLESHEET)

        self.set_percentage(self.correct_authorized_response_percentage,
                            ts.get_correct_authorized_responses_percentage(), MEDIUM_RESULT_STYLESHEET)
        number_of_authorized = "%d sur %d" % (len(ts.correct_authorized_responses), ts.get_number_of_valid_stimuli())
        self.correct_authorized_response_number.setText(number_of_authorized)

        self.set_percentage(self.correct_forbidden_response_percentage, ts.get_correct_forbidden_responses_percentage(),
                            MEDIUM_RESULT_STYLESHEET)
        number_of_forbidden = "%d sur %d" % (len(ts.correct_forbidden_responses), ts.get_number_of_forbidden_stimuli())
        self.correct_forbidden_response_number.setText(number_of_forbidden)

        avg_rt = "%d ms" % ts.average_response_time if ts.average_response_time > 0 else "N.D."
        self.response_time.setText(avg_rt)

        min_rt = "%d ms" % ts.min_response_time if ts.max_response_time > ts.min_response_time else "N.D."
        self.min_response_time.setText(min_rt)

        max_rt = "%d ms" % ts.max_response_time if ts.max_response_time > 0 else "N.D."
        self.max_response_time.setText(max_rt)
