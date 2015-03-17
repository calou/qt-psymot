# -*- coding: utf8 -*-

from threading import *

from PyQt5 import QtWidgets, QtCore

from gui.window.stimuli.ResultsWindow import ResultsWidget
from gui.design.StylesheetHelper import *
from model.stimuli import StimuliTestingSession, Stimulus, StimulusResponse
from gui.window.stimuli.design.TestingDesign import Ui_TextStimuliTestingDesignWidget
import datetime
import time


class TestingWidget(QtWidgets.QWidget, Ui_TextStimuliTestingDesignWidget):
    testing_session_completed = QtCore.pyqtSignal(object)

    def __init__(self, parent=None, configuration=None, patient=None):
        super(TestingWidget, self).__init__(parent)
        self.root_widget = parent
        self.setupUi(self)

        self.testing_session = configuration.generate_testing_session()
        self.testing_session.person = patient
        self.consigne.setText("Consigne:\n%s" % configuration.consigne)
        self.current_stimulus = None
        self.init_ui()
        self.started = False

    def init_ui(self):
        self.text_widget.setText("")
        self.text_widget.setStyleSheet("font-family:'Source Sans Pro'; font-weight: 600; font-size:96px;" + DARK_COLOR)
        self.display_result_button.hide()
        self.consigne.setStyleSheet(THIN_MEDIUM_RESULT_STYLESHEET)
        self.consigne.setWordWrap(True)
        self.begin_text.setStyleSheet(THIN_MEDIUM_RESULT_STYLESHEET + DARK_COLOR)
        self.begin_text.setWordWrap(True)
        self.display_result_button.clicked.connect(self.display_result)

    def start(self):
        for stimulus in self.testing_session.stimuli:
            Timer(stimulus.time, self.print_value, [stimulus]).start()
            Timer(stimulus.time + stimulus.get_duration(), self.hide_value).start()

        Timer(self.testing_session.stimuli[-1].time + 3, self.display_testing_end).start()

        self.testing_session.start_date = datetime.datetime.now()

        # Initialisation d'un premier stimulus "vide"
        self.current_stimulus = Stimulus()
        self.testing_session.stimuli.insert(0, self.current_stimulus)

    def hide_value(self):
        self.text_widget.setText("")

    def print_value(self, stimulus):
        text = stimulus.stimulus_value.value
        self.current_stimulus = stimulus
        self.text_widget.setText(text)
        stimulus.effective_time = time.time()
        QtCore.qDebug("%f - Set text %s" % (stimulus.effective_time, text))

    def mousePressEvent(self, event):
        self.on_click()

    def on_click(self):
        if not self.started:
            self.started = True
            self.start()
            self.consigne.hide()
            self.begin_text.hide()
        else:
            self.current_stimulus.stimulus_responses.append(StimulusResponse())
            QtCore.qDebug("%f - click" % (time.time()))

    def display_testing_end(self):
        self.display_result_button.show()

    def display_result(self):
        widget = ResultsWidget(self.root_widget, self.testing_session)
        self.root_widget.replaceAndRemoveWindow(widget)

