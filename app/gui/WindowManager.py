from PyQt5 import uic
from app.gui.ManagePatientsWindow import *
from app.gui.font import FontManager

class WindowManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowManager, self).__init__()
        FontManager.install_fonts()
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_window = uic.loadUi("app/gui/home.ui")
        self.manage_patients_window = ManagePatientWindow()

        self.init_ui()

        with open("assets/stylesheet.qss") as stylesheet_file:
            self.setStyleSheet(stylesheet_file.read())

    def init_ui(self):
        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('Psychomotriciel')

        self.home_window.manage_patients_button.clicked.connect(self.go_to_manage_patients)
        self.stacked_widget.addWidget(self.home_window)

        self.manage_patients_window.back_button.clicked.connect(self.go_to_home)
        self.stacked_widget.addWidget(self.manage_patients_window)

    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_manage_patients(self):
        print("Manage patients")
        self.stacked_widget.setCurrentIndex(1)