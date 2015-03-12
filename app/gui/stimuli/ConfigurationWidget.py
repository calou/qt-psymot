# -*- coding: utf8 -*-

from threading import *
import time

from app.model.stimuli import *
from app.gui.widget import *
from app.gui.stimuli.design.ConfigurationDesign import Ui_TestingSetupDesign
from app.db.StimuliTestingConfigurationRepository import StimuliTestingConfigurationRepository
from app.db.PersonRepository import PersonRepository

class ConfigurationWidget(QtWidgets.QWidget, Ui_TestingSetupDesign):
    testing_session_started = QtCore.pyqtSignal(StimuliTestingConfiguration)


    def __init__(self):
        super(ConfigurationWidget, self).__init__()
        self.setupUi(self)

        self.configurations = []
        self.patients = []

        self.conf_repository = StimuliTestingConfigurationRepository()
        self.person_repository = PersonRepository()

        self.current_patient = None
        self.current_configuration = None

        self.start_button.clicked.connect(self.emit_testing_session_started)


    def fetch_data(self):
        self.configurations = self.conf_repository.list()
        self.patients = self.person_repository.list()

        self.init_combos()

    def init_combos(self):
        self.patient_select.clear()
        for p in self.patients:
            self.patient_select.addItem(p.full_name())
        self.patient_select.setCurrentIndex(0)
        self.patient_select.activated['QString'].connect(self.on_patient_changed)

        self.testing_select.clear()
        for c in self.configurations:
            self.testing_select.addItem(c.name)
        self.testing_select.setCurrentIndex(0)
        self.testing_select.activated['QString'].connect(self.on_conf_changed)


    def on_patient_changed(self):
        self.current_patient = self.patients[self.patient_select.currentIndex()]

    def on_conf_changed(self):
        self.current_configuration = self.configurations[self.testing_select.currentIndex()]
        self.spinBox.setValue(self.current_configuration.number_of_stimuli)

    def emit_testing_session_started(self):
        self.current_configuration.number_of_stimuli = self.spinBox.value()
        self.testing_session_started.emit(self.current_configuration)
