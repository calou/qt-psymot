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
        self.summary_tab = SummaryTab()
        self.stimuli_list_tab = StimuliListTab()
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setGeometry(340, 90, 530, 460)
        self.tab_widget.addTab(self.summary_tab, u"Résumé")
        self.tab_widget.addTab(self.stimuli_list_tab, u"Liste des stimuli")

        self.search_input.setPlaceholderText(u"Rechercher")
        self.search_input.setGeometry(30, 90, 200, 32)
        self.search_input.textChanged.connect(self.search_patients)
        self.list_widget.setGeometry(30, 130, 300, 420)
        self.list_widget.itemClicked.connect(self.update_tabs)

        self.update_tabs()


    def update_tabs(self):
        session = self.sessions[self.list_widget.currentIndex().row()]
        self.summary_tab.update_tab(session)
        self.stimuli_list_tab.update_tab(session)


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

        self.date = QtWidgets.QLabel(self)
        self.date.setGeometry(10, 50, 200, 40)

        self.configuration_name = QtWidgets.QLabel(self)
        self.configuration_name.setGeometry(10,10, 200, 40)

        self.percentage = QtWidgets.QLabel(self)
        self.percentage.setGeometry(10,90, 200, 40)


    def update_tab(self, session):
        self.date.setText(session.start_date.strftime("%d/%m/%Y - %H:%M"))
        self.configuration_name.setText(session.configuration_name)
        self.percentage.setText("%d%%" % (session.get_correct_responses_percentage()))


class StimuliListTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(StimuliListTab, self).__init__(parent)

    def update_tab(self, session):
        self.stimuli = session.stimuli