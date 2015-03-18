# -*- coding: utf8 -*-
from PyQt5 import QtWidgets, QtGui, Qt
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
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.repository = StimuliRepository()

    def create_table_widget_item(self, row, column, value, background_brush, foreground_brush, alignment=1):
        table_widget_item = QtWidgets.QTableWidgetItem(value)
        if background_brush:
            table_widget_item.setBackground(background_brush)
        if foreground_brush:
            table_widget_item.setForeground(foreground_brush)
        table_widget_item.setTextAlignment(alignment)
        self.table.setItem(row, column, table_widget_item)


    def update_tab(self, session):
        stimuli = self.repository.get_by_session_id(session.id)
        self.table.clear()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([u"Temps", u"Valeur", u"Réaction", u"Actions"])
        self.table.setRowCount(len(stimuli))
        self.table.setShowGrid(False)
        session_start_time = time.mktime(session.start_date.timetuple())
        index = 0
        green_bg_brush = QtGui.QBrush(QtGui.QColor("#80E680"))
        red_bg_brush = QtGui.QBrush(QtGui.QColor("#FF9999"))
        green_fg_brush = QtGui.QBrush(QtGui.QColor("#142D21"))
        red_fg_brush = QtGui.QBrush(QtGui.QColor("#4C0000"))
        for stimulus in stimuli:
            bg_brush = red_bg_brush
            fg_brush = red_fg_brush
            if stimulus.correct:
                bg_brush = green_bg_brush
                fg_brush = green_fg_brush
            self.table.setItem(index, 0, QtWidgets.QTableWidgetItem(stimulus.valid))
            relative_time = 0
            if stimulus.effective_time:
                relative_time = 1000 * (stimulus.effective_time - session_start_time)
            reaction_str = ""
            if stimulus.action_time:
                reaction = 1000 * (stimulus.action_time - stimulus.effective_time)
                reaction_str = "%d ms" % reaction
            self.create_table_widget_item(index, 0, "%d ms" % relative_time, bg_brush, fg_brush, 0x82)
            self.create_table_widget_item(index, 1, stimulus.string_value, bg_brush, fg_brush, 0x84)
            self.create_table_widget_item(index, 2, reaction_str, bg_brush, fg_brush, 0x82)
            self.create_table_widget_item(index, 3, "%d" % stimulus.action_count, bg_brush, fg_brush, 0x84)
            index += 1
