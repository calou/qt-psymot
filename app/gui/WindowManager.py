from app.gui.window.stimuli.ConfigurationWindow import *
from app.gui.window.Home import Home
from app.gui.font import FontManager



class WindowManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowManager, self).__init__()
        FontManager.install_fonts()
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_window = Home(self)
        self.init_ui()

        with open("assets/stylesheet.qss") as stylesheet_file:
            self.setStyleSheet(stylesheet_file.read())

    def init_ui(self):

        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('Psychomotriciel')

        self.stacked_widget.addWidget(self.home_window)

    def display(self):
        self.go_to_home()

    def go_to_home(self):
        self.stacked_widget.setCurrentWidget(self.home_window)

    def replaceWindow(self, widget):
        self.stacked_widget.addWidget(widget)
        self.stacked_widget.setCurrentWidget(widget)

    def replaceAndRemoveWindow(self, widget):
        former_widget = self.stacked_widget.currentWidget()
        self.replaceWindow(widget)
        self.removeWidget(former_widget)

    def removeWidget(self, widget):
        self.stacked_widget.removeWidget(widget)