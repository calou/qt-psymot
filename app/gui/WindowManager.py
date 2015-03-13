from PyQt5 import QtWidgets, uic

from app.gui.patients.ManageWindow import *
from app.gui.stimuli.TestingWidget import *
from app.gui.stimuli.ResultsWidget import *
from app.gui.stimuli.ConfigurationWidget import *
from app.gui.window.Home import Home
from app.model.stimuli import StimuliTestingConfiguration
from app.gui.font import FontManager


from app.db.StimuliTestingConfigurationRepository import *


class WindowManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowManager, self).__init__()
        FontManager.install_fonts()
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_window = Home()
        self.manage_patients_window = ManagePatientWindow()
        self.stimuli_testing_widget = TestingWidget()
        self.stimuli_results_widget = ResultsWidget()
        self.stimuli_conf_widget = ConfigurationWidget()

        self.init_ui()

        with open("assets/stylesheet.qss") as stylesheet_file:
            self.setStyleSheet(stylesheet_file.read())

    def init_ui(self):
        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('Psychomotriciel')

        self.stacked_widget.addWidget(self.home_window)
        self.home_window.go_to_patients.connect(self.go_to_manage_patients)
        self.home_window.go_to_testing.connect(self.go_to_stimuli_conf_widget)

        self.stacked_widget.addWidget(self.manage_patients_window)
        self.manage_patients_window.back_button.clicked.connect(self.go_to_home)

        self.stacked_widget.addWidget(self.stimuli_testing_widget)


        self.stacked_widget.addWidget(self.stimuli_results_widget)
        self.stimuli_testing_widget.testing_session_completed.connect(self.stimuli_results_widget.set_testing_session)
        self.stimuli_testing_widget.display_result_button.clicked.connect(self.go_to_stimuli_result_widget)
        self.stimuli_results_widget.back_button.clicked.connect(self.go_to_home)

        self.stacked_widget.addWidget(self.stimuli_conf_widget)
        self.stimuli_conf_widget.back_button.clicked.connect(self.go_to_home)
        self.stimuli_conf_widget.testing_session_started.connect(self.go_to_stimuli_test_widget)

        repo = StimuliTestingConfigurationRepository()
        confs = repo.list()
        c = confs[0]
        repo.fetch_stimuli_values(c)
        print(c)

    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_manage_patients(self):
        print("Manage patients")
        self.stacked_widget.setCurrentIndex(1)

    @pyqtSlot(StimuliTestingConfiguration)
    def go_to_stimuli_test_widget(self, conf):
        print("Clicked Start test")
        self.stacked_widget.setCurrentIndex(2)
        self.stimuli_testing_widget.set_configuration(conf)

    def go_to_stimuli_result_widget(self):
        print("Afficher les résultats")
        self.stacked_widget.setCurrentIndex(3)

    def go_to_stimuli_conf_widget(self):
        print("Clicked Start test")
        self.stacked_widget.setCurrentIndex(4)
        self.stimuli_conf_widget.fetch_data()
