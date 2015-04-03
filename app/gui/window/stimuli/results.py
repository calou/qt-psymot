# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui

from model.stimuli import *
from gui.base import Window
from gui.design.StylesheetHelper import *
from db.stimuli_repositories import *


class ResultsWidget(Window):
    def __init__(self, parent, session):
        super(ResultsWidget, self).__init__(parent)
        self.root_widget = parent

        self.correct_responses_percentage_text = QtGui.QLabel(self)
        self.correct_response_percentage = QtGui.QLabel(self)
        self.correct_authorized_response_percentage = QtGui.QLabel(self)
        self.correct_authorized_responses_percentage_text = QtGui.QLabel(self)
        self.correct_forbidden_response_percentage = QtGui.QLabel(self)
        self.correct_forbidden_responses_percentage_text = QtGui.QLabel(self)
        self.response_time_text = QtGui.QLabel(self)
        self.response_time = QtGui.QLabel(self)
        self.max_response_time_text = QtGui.QLabel(self)
        self.max_response_time = QtGui.QLabel(self)
        self.min_response_time = QtGui.QLabel(self)
        self.min_response_time_text = QtGui.QLabel(self)
        self.correct_authorized_response_number = QtGui.QLabel(self)
        self.correct_forbidden_response_number = QtGui.QLabel(self)
        self.set_testing_session(session)


        self.init_ui()
        Window.init(self, self.root_widget)

    def init_ui(self):
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.correct_responses_percentage_text.setFont(font)
        self.correct_responses_percentage_text.setText(u"Taux de réussite")
        self.correct_responses_percentage_text.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.correct_response_percentage.setFont(font)
        self.correct_response_percentage.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.response_time.setFont(font)
        self.response_time.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.correct_authorized_responses_percentage_text.setFont(font)
        self.correct_authorized_responses_percentage_text.setText(u"Valeurs autorisées")
        self.correct_authorized_responses_percentage_text.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)

        self.correct_forbidden_responses_percentage_text.setFont(font)
        self.correct_forbidden_responses_percentage_text.setText("Valeurs interdites")
        self.correct_forbidden_responses_percentage_text.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)

        self.response_time_text.setFont(font)
        self.response_time_text.setText(u"Réaction moyenne")
        self.response_time_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.min_response_time_text.setFont(font)
        self.min_response_time_text.setText(u"Min.")
        self.min_response_time_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)

        self.max_response_time_text.setFont(font)
        self.max_response_time_text.setText(u"Max.")
        self.max_response_time_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.correct_authorized_response_percentage.setFont(font)
        self.correct_authorized_response_percentage.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)

        self.correct_forbidden_response_percentage.setFont(font)
        self.correct_forbidden_response_percentage.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)

        self.correct_forbidden_response_number.setFont(font)
        self.correct_forbidden_response_number.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)

        self.correct_authorized_response_number.setFont(font)
        self.correct_authorized_response_number.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)

        self.max_response_time.setFont(font)
        self.max_response_time.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)

        self.min_response_time.setFont(font)
        self.min_response_time.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)


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

    @QtCore.pyqtSlot(object)
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

    def resizeEvent(self, ev):
        Window.on_resize(self)
        self.correct_responses_percentage_text.setGeometry(QtCore.QRect(10, 20, 500, 61))
        self.correct_response_percentage.setGeometry(QtCore.QRect(10, 70, 700, 161))

        self.response_time_text.setGeometry(QtCore.QRect(10, 270, 511, 61))
        self.response_time.setGeometry(QtCore.QRect(10, 320, 431, 201))

        self.correct_authorized_response_number.setGeometry(QtCore.QRect(515, 77, 161, 51))
        self.correct_authorized_responses_percentage_text.setGeometry(QtCore.QRect(570, 20, 261, 51))
        self.max_response_time.setGeometry(QtCore.QRect(550, 420, 281, 81))

        self.max_response_time_text.setGeometry(QtCore.QRect(580, 390, 251, 51))

        self.correct_forbidden_response_number.setGeometry(QtCore.QRect(515, 197, 161, 51))
        self.correct_authorized_response_percentage.setGeometry(QtCore.QRect(670, 50, 161, 75))
        self.correct_forbidden_responses_percentage_text.setGeometry(QtCore.QRect(580, 140, 251, 50))

        self.min_response_time_text.setGeometry(QtCore.QRect(570, 270, 261, 51))
        self.min_response_time.setGeometry(QtCore.QRect(550, 300, 281, 81))

        self.correct_forbidden_response_percentage.setGeometry(QtCore.QRect(670, 170, 161, 75))
