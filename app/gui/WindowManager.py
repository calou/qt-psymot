from PyQt5 import uic
from app.gui.ManagePatientsWindow import *
from app.gui.StimuliTestingSessionWidget import *
from app.gui.DisplayStimuliSessionResultsWidget import *
from app.gui.font import FontManager

class WindowManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowManager, self).__init__()
        FontManager.install_fonts()
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_window = uic.loadUi("app/gui/home.ui")
        self.manage_patients_window = ManagePatientWindow()
        self.stimuli_test_widget = StimuliTestSessionWidget()
        self.display_stimuli_result_widget = DisplayStimuliSessionResultsDesignWidget()

        self.init_ui()

        with open("assets/stylesheet.qss") as stylesheet_file:
            self.setStyleSheet(stylesheet_file.read())

    def init_ui(self):
        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('Psychomotriciel')

        self.stacked_widget.addWidget(self.home_window)
        self.home_window.manage_patients_button.clicked.connect(self.go_to_manage_patients)

        self.stacked_widget.addWidget(self.manage_patients_window)
        self.manage_patients_window.back_button.clicked.connect(self.go_to_home)

        self.stacked_widget.addWidget(self.stimuli_test_widget)
        self.home_window.start_test_button.clicked.connect(self.go_to_stimuli_test_widget)


        self.stacked_widget.addWidget(self.display_stimuli_result_widget)
        self.stimuli_test_widget.testing_session_completed.connect(self.display_stimuli_result_widget.set_testing_session)
        self.stimuli_test_widget.display_result_button.clicked.connect(self.go_to_testing_result_widget)

    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_manage_patients(self):
        print("Manage patients")
        self.stacked_widget.setCurrentIndex(1)

    def go_to_stimuli_test_widget(self):
        print("Clicked Start test")
        self.stacked_widget.setCurrentIndex(2)
        self.stimuli_test_widget.start()

    def go_to_testing_result_widget(self):
        print("Afficher les résultats")
        self.stacked_widget.setCurrentIndex(3)
