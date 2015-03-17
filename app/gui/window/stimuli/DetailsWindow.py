# -*- coding: utf8 -*-
from PyQt5 import QtWidgets
from model.stimuli import *
from gui.button import *
from gui.base import *
from db.StimuliRepositories import SessionRepository

class DetailsWindow(Window):
    def __init__(self, parent):
        super(DetailsWindow, self).__init__(parent)

        self.search_input = QtWidgets.QLineEdit(self)
        self.list_widget = QtWidgets.QListWidget(self)
        self.repository = SessionRepository()
        self.sessions = []
        self.search_patients()
        self.init_ui()
        Window.init(self, parent, "Détails des tests")

    def init_ui(self):
        self.search_input.setPlaceholderText(u"Rechercher")
        self.search_input.setGeometry(30, 90, 200, 32)
        self.search_input.textChanged.connect(self.search_patients)
        self.list_widget.setGeometry(30, 130, 300, 420)

        self.summary_tab = SummaryTab()
        self.stimuli_list_tab = StimuliListTab()
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setGeometry(340, 90, 530, 460)
        self.tab_widget.addTab(self.summary_tab, u"Résumé")
        self.tab_widget.addTab(self.stimuli_list_tab, u"Liste des stimuli")


    def search_patients(self):
        search_value = self.search_input.text()
        if(search_value == ''):
            self.sessions = self.repository.list()
        else:
            self.sessions = self.repository.search_by_person(search_value)
        self.redraw_list()

    def redraw_list(self):
        self.list_widget.clear()
        for s in self.sessions:
            date_str = s.start_date.strftime("%d/%m/%Y - %H:%M")
            self.list_widget.addItem('%s - %s, %s' % (date_str, s.person.last_name, s.person.first_name))

class SummaryTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SummaryTab, self).__init__(parent)

class StimuliListTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(StimuliListTab, self).__init__(parent)