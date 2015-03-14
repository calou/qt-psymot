from app.gui.window.patients.ManageWindow import *
from app.gui.window.stimuli.ConfigurationWindow import *
from app.gui.window.Home import Home
from app.gui.font import FontManager


from app.db.StimuliRepositories import *


class WindowManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowManager, self).__init__()
        FontManager.install_fonts()
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_window = Home(self)
        self.manage_patients_window = ManagePatientWindow(self)
        self.stimuli_conf_widget = ConfigurationWidget(self)

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

        self.stacked_widget.addWidget(self.stimuli_conf_widget)
        self.stimuli_conf_widget.back_button.clicked.connect(self.go_to_home)

        repo = ConfigurationRepository()
        confs = repo.list()
        c = confs[0]
        repo.fetch_stimuli_values(c)

    def display(self):
        self.go_to_home()

    def go_to_home(self):
        self.stacked_widget.setCurrentWidget(self.home_window)

    def go_to_manage_patients(self):
        self.stacked_widget.setCurrentIndex(1)

    def go_to_stimuli_conf_widget(self):
        self.stacked_widget.setCurrentIndex(2)
        self.stimuli_conf_widget.fetch_data()

    def replaceWindow(self, widget):
        self.stacked_widget.addWidget(widget)
        self.stacked_widget.setCurrentWidget(widget)

    def replaceAndRemoveWindow(self, widget):
        former_widget = self.stacked_widget.currentWidget()
        self.replaceWindow(widget)
        self.removeWidget(former_widget)

    def removeWidget(self, widget):
        self.stacked_widget.removeWidget(widget)