# -*- coding: utf8 -*-

from threading import *

from PyQt4 import QtGui, QtCore

from gui.window.stimuli.ResultsWindow import ResultsWidget
from gui.design.StylesheetHelper import *
from model.stimuli import StimuliTestingSession, Stimulus, StimulusResponse
from gui.base import Window
import datetime
import time


class TestingWidget(Window):
    completed = QtCore.pyqtSignal()

    def __init__(self, parent=None, configuration=None, patient=None):
        super(TestingWidget, self).__init__(parent)
        self.root_widget = parent

        self.session = configuration.generate_testing_session()
        self.session.person = patient
        self.consigne = QtGui.QLabel(self)
        self.consigne.setText("Consigne:\n%s" % configuration.consigne)
        self.consigne.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.text_widget = QtGui.QLabel(self)
        self.text_widget.setAlignment(QtCore.Qt.AlignCenter)
        self.text_widget.setObjectName("text_widget")
        self.result_button = QtGui.QPushButton(self)
        self.result_button.setObjectName("display_result_button")

        self.begin_text = QtGui.QLabel(self)
        self.begin_text.setAlignment(QtCore.Qt.AlignCenter)

        self.end_text = QtGui.QLabel(self)
        self.end_text.setAlignment(QtCore.Qt.AlignCenter)

        self.init_ui()
        self.current_stimulus = None
        self.started = False

    def init_ui(self):
        self.text_widget.setText("")
        self.text_widget.setStyleSheet("font-family:'Source Sans Pro'; font-weight: 600; font-size:96px;" + DARK_COLOR)
        self.result_button.setText("Terminer")
        self.result_button.hide()
        self.end_text.setText("Le test est terminé, merci.")
        self.end_text.hide()
        self.end_text.setStyleSheet(THIN_MEDIUM_RESULT_STYLESHEET + DARK_COLOR)
        self.end_text.setWordWrap(True)
        self.consigne.setStyleSheet(THIN_MEDIUM_RESULT_STYLESHEET)
        self.consigne.setWordWrap(True)
        self.begin_text.setText(u"Cliquer pour commencer")
        self.begin_text.setStyleSheet(THIN_MEDIUM_RESULT_STYLESHEET + DARK_COLOR)
        self.begin_text.setWordWrap(True)
        self.result_button.clicked.connect(self.display_result)
        self.completed.connect(self.on_completion)

    def start(self):
        for stimulus in self.session.stimuli:
            Timer(stimulus.time, self.print_value, [stimulus]).start()
            Timer(stimulus.time + stimulus.get_duration(), self.hide_value).start()

        Timer(self.session.stimuli[-1].time + 3, self.emit_completed).start()

        self.session.start_date = datetime.datetime.now()

        # Initialisation d'un premier stimulus "vide"
        self.current_stimulus = Stimulus()
        self.session.stimuli.insert(0, self.current_stimulus)

    def hide_value(self):
        self.text_widget.setText("")

    def print_value(self, stimulus):
        text = stimulus.stimulus_value.value
        self.current_stimulus = stimulus
        self.text_widget.setText(text)
        stimulus.effective_time = time.time()
        QtCore.qDebug("%f - Set text %s" % (stimulus.effective_time, text))

    def mousePressEvent(self, event):
        self.on_action()

    def on_action(self):
        if not self.started:
            self.started = True
            self.start()
            self.consigne.hide()
            self.begin_text.hide()
        else:
            self.current_stimulus.stimulus_responses.append(StimulusResponse())
            QtCore.qDebug("%f - click" % (time.time()))

    def emit_completed(self):
        self.completed.emit()

    def on_completion(self):
        self.result_button.show()
        self.end_text.show()

    def display_result(self):
        widget = ResultsWidget(self.root_widget, self.session)
        self.root_widget.replaceAndRemoveWindow(widget)

    def resizeEvent(self, ev):
        w = self.width()
        h = self.height()
        self.text_widget.setGeometry(QtCore.QRect(0, 0, w, h - 100))
        self.end_text.setGeometry(QtCore.QRect(10, 0, w, h - 100))
        self.begin_text.setGeometry(QtCore.QRect(10, 0, w, h - 100))
        self.consigne.setGeometry(QtCore.QRect(50, 50, w, 200))
        self.result_button.setGeometry(Window.get_right_button_geometry(self))
