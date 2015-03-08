from PyQt5 import QtWidgets

__author__ = 'calou'


class HomeWindow(QtWidgets.QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.drawHome()

    def drawHome(self):
        self.homeLayout = QtWidgets.QHBoxLayout()
        leftBox = QtWidgets.QGridLayout()
        startTestButton = QtWidgets.QPushButton(u"Démarrer un test")
        managePatientsButton = QtWidgets.QPushButton(u"Gérer les patients")
        managePatientsButton.clicked.connect(self.managePatientsButtonClicked)

        leftBox.addWidget(startTestButton, 0, 0)
        leftBox.addWidget(managePatientsButton, 1, 0)

        self.homeLayout.addLayout(leftBox)
        personFormLayout = QtWidgets.QFormLayout()
        self.firstNameWidget = QtWidgets.QLineEdit()
        self.lastNameWidget = QtWidgets.QLineEdit()
        self.birthDateWidget = QtWidgets.QDateEdit()
        personFormLayout.addRow(u"Prénom", self.firstNameWidget)
        personFormLayout.addRow(u"Nom", self.lastNameWidget)
        personFormLayout.addRow(u"Date de naissance", self.birthDateWidget)

        self.homeLayout.addLayout(personFormLayout)

        self.setLayout(self.homeLayout)

        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('Psychomotriciel')
        self.show()