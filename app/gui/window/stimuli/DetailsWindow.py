# -*- coding: utf8 -*-
from PyQt5 import QtWidgets, QtGui
from model.stimuli import *
from gui.button import *
from gui.base import *
from db.StimuliRepositories import SessionRepository, StimuliRepository
import time


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

        # self.update_tabs()


    def update_tabs(self):
        session = self.sessions[self.list_widget.currentIndex().row()]
        self.summary_tab.update_tab(session)
        self.stimuli_list_tab.update_tab(session)


    def search_patients(self):
        search_value = self.search_input.text()
        if '' == search_value:
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
        self.configuration_name.setGeometry(10, 10, 200, 40)

        self.percentage = QtWidgets.QLabel(self)
        self.percentage.setGeometry(10, 90, 200, 40)


    def update_tab(self, session):
        self.date.setText(session.start_date.strftime("%d/%m/%Y - %H:%M"))
        self.configuration_name.setText(session.configuration_name)
        self.percentage.setText("%d%%" % (session.get_correct_responses_percentage()))


class StimuliListTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(StimuliListTab, self).__init__(parent)
        self.table = QtWidgets.QTableWidget(self)
        self.table.setGeometry(0, 0, 530, 460)
        self.table.setAlternatingRowColors(True)
        self.table.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.repository = StimuliRepository()

    def update_tab(self, session):
        stimuli = self.repository.get_by_session_id(session.id)
        self.table.clear()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([u"Temps", u"Valeur", u"Réaction", u"Actions"])

        self.table.setRowCount(len(stimuli))
        session_start_time = time.mktime(session.start_date.timetuple())
        index = 0
        green_color = QtGui.QColor("#00CC66")
        red_color = QtGui.QColor("#FF4D4D")
        green_brush = QtGui.QBrush(green_color)
        red_brush = QtGui.QBrush(red_color)
        for stimulus in stimuli:
            brush = red_brush
            if stimulus.correct:
                brush = green_brush
            self.table.setItem(index, 0, QtWidgets.QTableWidgetItem(stimulus.valid))
            relative_time = 0

            if stimulus.effective_time:
                relative_time = 1000 * (stimulus.effective_time - session_start_time)
            value_ti = QtWidgets.QTableWidgetItem(stimulus.string_value)
            value_ti.setBackground(brush)
            time_ti = QtWidgets.QTableWidgetItem("%d ms" % relative_time)
            time_ti.setBackground(brush)
            self.table.setItem(index, 0, time_ti)
            self.table.setItem(index, 1, value_ti)

            reaction_str = ""
            if stimulus.action_time:
                reaction = 1000 * (stimulus.action_time - stimulus.effective_time)
                reaction_str = "%d ms" % reaction
            reaction_ti = QtWidgets.QTableWidgetItem(reaction_str)
            reaction_ti.setBackground(brush)
            self.table.setItem(index, 2, reaction_ti)
            count_ti = QtWidgets.QTableWidgetItem("%d" % stimulus.action_count)
            count_ti.setBackground(brush)
            self.table.setItem(index, 3, count_ti)

            self.table.row
            index += 1
