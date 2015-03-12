# -*- coding: utf8 -*-

from threading import *
from app.db.StimuliTestingConfigurationRepository import StimuliTestingConfigurationRepository
import time

from app.model.stimuli import *
from app.gui.widget import *
from app.gui.stimuli.design.TestingDesign import Ui_TextStimuliTestingDesignWidget


class TestingWidget(QtWidgets.QWidget, Ui_TextStimuliTestingDesignWidget):
    testing_session_completed = QtCore.pyqtSignal(StimuliTestingSession, name='testingSessionCompleted')

    def __init__(self):
        super(TestingWidget, self).__init__()
        self.setupUi(self)
        self.testing_session = None
        self.current_stimulus = None
        self.init_ui()

    def init_ui(self):
        self.text_widget.setText("")
        self.text_widget.setStyleSheet("font-family:'Source Sans Pro'; font-weight: 600; font-size:96px;")
        self.display_result_button.hide()

    def start(self, configuration):
        repository = StimuliTestingConfigurationRepository()
        repository.fetch_stimuli_values(configuration)
        self.testing_session = configuration.generate_testing_session()
        for stimulus in self.testing_session.stimuli:
            Timer(stimulus.time, self.print_value, [stimulus]).start()
            Timer(stimulus.time + stimulus.get_duration(), self.hide_value).start()

        Timer(self.testing_session.stimuli[-1].time + 3, self.display_testing_end).start()

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
        self.current_stimulus.stimulus_responses.append(StimulusResponse())
        QtCore.qDebug("%f - click" % (time.time()))

    def display_testing_end(self):
        #self.testing_session.compute_results()
        self.display_result_button.show()
        self.testing_session_completed.emit(self.testing_session)