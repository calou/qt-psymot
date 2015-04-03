# -*- coding: utf8 -*-

from PyQt4 import QtGui, QtCore
from gui.base import Window
from gui.design.StylesheetHelper import *
from gui.window.stimuli.testing import TestingWidget
from gui.button import *
from db.stimuli_repositories import ConfigurationRepository
from db.base_model_repository import PersonRepository


class SetUpWindow(Window):
    def __init__(self, parent=None):
        super(SetUpWindow, self).__init__(parent)
        self.root_widget = parent
        self.patient_select = QtGui.QComboBox(self)
        self.testing_select = QtGui.QComboBox(self)
        self.patient_text = QtGui.QLabel(self)
        self.session_text = QtGui.QLabel(self)
        self.spinBox = QtGui.QSpinBox(self)
        self.numbers_of_stimuli_text = QtGui.QLabel(self)
        self.start_button = QtGui.QPushButton(self)
        self.values_text = QtGui.QLabel(self)
        self.consigne_text = QtGui.QLabel(self)
        self.consigne = QtGui.QLabel(self)
        self.valid_values_text = QtGui.QLabel(self)
        self.all_values = QtGui.QTextEdit(self)
        self.valid_values = QtGui.QTextEdit(self)

        self.configurations = []
        self.patients = []

        self.conf_repository = ConfigurationRepository()
        self.person_repository = PersonRepository()

        self.current_patient = None
        self.current_configuration = None

        self.start_button.clicked.connect(self.start_testing)

        self.fetch_data()
        self.init_ui()
        Window.init(self, parent, u"Définition du test")

    def init_ui(self):
        self.numbers_of_stimuli_text.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.values_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.consigne_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.consigne.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.valid_values_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)

        self.patient_text.setText(u"Patient")
        self.session_text.setText(u"Test")
        self.numbers_of_stimuli_text.setText(u"Nombre de stimuli")
        self.start_button.setText(u"Démarrer")
        self.values_text.setText(u"Valeurs")
        self.consigne_text.setText(u"Consigne :")
        self.consigne.setText(u"consigne_text")
        self.valid_values_text.setText(u"Valeurs valides")


    def fetch_data(self):
        self.configurations = self.conf_repository.list()
        self.patients = self.person_repository.list()

        self.init_combos()

    def init_combos(self):
        self.patient_select.clear()
        for p in self.patients:
            self.patient_select.addItem(p.full_name())
        self.on_patient_changed()
        self.patient_select.activated['QString'].connect(self.on_patient_changed)


        self.testing_select.clear()
        for c in self.configurations:
            self.testing_select.addItem(c.name)
        self.on_conf_changed()
        self.testing_select.activated['QString'].connect(self.on_conf_changed)


    def on_patient_changed(self):
        self.current_patient = self.patients[self.patient_select.currentIndex()]

    def on_conf_changed(self):
        self.current_configuration = self.configurations[self.testing_select.currentIndex()]
        self.conf_repository.fetch_stimuli_values(self.current_configuration)

        self.spinBox.setValue(self.current_configuration.number_of_stimuli)
        self.consigne.setText(self.current_configuration.consigne)

        all_values = []
        valid_values = []
        for stimuli_value in self.current_configuration.stimuli_values:
            color = RED_COLOR
            if stimuli_value in self.current_configuration.valid_stimuli_values:
                color = GREEN_COLOR
            html = "<span style='%s'>%s</span>" % (color, stimuli_value.value)
            all_values.append(html)
        for stimuli_value in self.current_configuration.valid_stimuli_values:
            html = "<span>%s</span>" % (stimuli_value.value)
            valid_values.append(html)

        all_values_html = ", ".join(all_values)
        self.all_values.setText("<html><body>%s</body></html>" % all_values_html)

        valid_values_html = ", ".join(valid_values)
        self.valid_values.setText("<html><body>%s</body></html>" % valid_values_html)


    def start_testing(self):
        self.current_configuration.number_of_stimuli = self.spinBox.value()
        widget = TestingWidget(self.root_widget, self.current_configuration, self.current_patient)
        self.root_widget.replaceWindow(widget)

    def resizeEvent(self, ev):
        Window.on_resize(self)
        self.start_button.setGeometry(Window.get_right_button_geometry(self))

        self.patient_select.setGeometry(QtCore.QRect(40, 140, 300, 32))
        self.testing_select.setGeometry(QtCore.QRect(390, 140, 300, 32))
        self.patient_text.setGeometry(QtCore.QRect(40, 110, 191, 31))
        self.session_text.setGeometry(QtCore.QRect(390, 110, 191, 31))
        self.spinBox.setGeometry(QtCore.QRect(220, 250, 71, 32))
        self.numbers_of_stimuli_text.setGeometry(QtCore.QRect(50, 250, 151, 32))

        self.values_text.setGeometry(QtCore.QRect(50, 300, 151, 32))
        self.consigne_text.setGeometry(QtCore.QRect(50, 200, 151, 32))
        self.consigne.setGeometry(QtCore.QRect(220, 200, 591, 41))
        self.valid_values_text.setGeometry(QtCore.QRect(470, 300, 171, 32))
        self.all_values.setGeometry(QtCore.QRect(220, 290, 231, 211))
        self.valid_values.setGeometry(QtCore.QRect(660, 290, 231, 211))
