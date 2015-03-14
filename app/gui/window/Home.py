# -*- coding: utf8 -*-

from PyQt5 import QtWidgets
from app.gui.design.window.HomeDesign import *
from app.gui.window.HomeSection import *
from app.model.stimuli import *
from app.gui.window.stimuli.DetailsWindow import DetailsWindow
from app.gui.window.patients.ManageWindow import ManagePatientWindow
from app.gui.window.stimuli.ConfigurationWindow import ConfigurationWindow

class Home(QtWidgets.QWidget, Ui_HomeDesign):
    go_to_testing = QtCore.pyqtSignal()
    go_to_patients = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.root_widget = parent
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        testing_section = HomeSection(["Démarrer un test", "Consulter un test"], "assets/images/checklist.svg")
        testing_section.push_buttons[0].clicked.connect(self.emit_go_to_testing)
        testing_section.push_buttons[1].clicked.connect(self.go_to_testing_details)

        self.gridLayout.addWidget(testing_section, 0, 0)

        patients_section = HomeSection(["Gérer les patients"], "assets/images/people.svg")
        patients_section.push_buttons[0].clicked.connect(self.emit_go_to_patients)
        self.gridLayout.addWidget(patients_section, 0, 1)


    def emit_go_to_testing(self):
        widget = ConfigurationWindow(self.root_widget)
        self.root_widget.replaceWindow(widget)

    def emit_go_to_patients(self):
        widget = ManagePatientWindow(self.root_widget)
        self.root_widget.replaceWindow(widget)

    def go_to_testing_details(self):
        widget = DetailsWindow(self.root_widget)
        self.root_widget.replaceWindow(widget)