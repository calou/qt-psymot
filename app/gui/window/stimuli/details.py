# -*- coding: utf8 -*-
from PyQt4 import QtGui, Qt
from model.stimuli import *
from gui.button import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from gui.base import *
from db.StimuliRepositories import SessionRepository, StimuliRepository
import time


class DetailsWindow(Window):
    def __init__(self, parent):
        super(DetailsWindow, self).__init__(parent)

        self.search_input = QtGui.QLineEdit(self)
        self.list_widget = QtGui.QListWidget(self)
        self.repository = SessionRepository()

        self.stimuli_repository = StimuliRepository()

        self.sessions = []
        self.search_patients()
        self.init_ui()
        Window.init(self, parent, "Détails des tests")

    def init_ui(self):
        self.summary_tab = SummaryTab()
        self.stimuli_list_tab = StimuliListTab()
        self.histogram_tab = HistogramTab()
        self.tab_widget = QtGui.QTabWidget(self)
        self.tab_widget.addTab(self.summary_tab, u"Résumé")
        self.tab_widget.addTab(self.stimuli_list_tab, u"Liste des stimuli")
        self.tab_widget.addTab(self.histogram_tab, u"Histogramme")

        self.search_input.setPlaceholderText(u"Rechercher")

        self.search_input.textChanged.connect(self.search_patients)
        self.list_widget.itemClicked.connect(self.update_tabs)


    def update_tabs(self):
        session = self.sessions[self.list_widget.currentIndex().row()]
        session.stimuli = self.stimuli_repository.get_by_session_id(session.id)
        self.summary_tab.update_tab(session)
        self.stimuli_list_tab.update_tab(session)
        self.histogram_tab.update_tab(session)

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

    def resizeEvent(self, ev):
        Window.on_resize(self)
        qrect = Window.get_central_geometry(self)
        self.tab_widget.setGeometry(qrect.x() + 310, qrect.y(), qrect.width() - 310, qrect.height())
        self.list_widget.setGeometry(qrect.x(), qrect.y() + 40, 300, qrect.height() - 40)
        self.search_input.setGeometry(qrect.x(), qrect.y(), 300, 32)


class SummaryTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SummaryTab, self).__init__(parent)

        self.date = QtGui.QLabel(self)
        self.date.setGeometry(10, 50, 200, 40)

        self.configuration_name = QtGui.QLabel(self)
        self.configuration_name.setGeometry(10, 10, 200, 40)

        self.percentage = QtGui.QLabel(self)
        self.percentage.setGeometry(10, 90, 200, 40)


    def update_tab(self, session):
        self.date.setText(session.start_date.strftime("%d/%m/%Y - %H:%M"))
        self.configuration_name.setText(session.configuration_name)
        self.percentage.setText("%d%%" % (session.get_correct_responses_percentage()))


class StimuliListTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(StimuliListTab, self).__init__(parent)
        self.table = QtGui.QTableWidget(self)
        self.table.setGeometry(0, 0, 530, 460)
        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

    def create_table_widget_item(self, row, column, value, background_brush, foreground_brush, alignment=1):
        table_widget_item = QtGui.QTableWidgetItem(value)
        if background_brush:
            table_widget_item.setBackground(background_brush)
        if foreground_brush:
            table_widget_item.setForeground(foreground_brush)
        table_widget_item.setTextAlignment(alignment)
        self.table.setItem(row, column, table_widget_item)


    def update_tab(self, session):
        self.table.clear()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([u"Temps", u"Valeur", u"Réaction", u"Actions"])
        self.table.setRowCount(len(session.stimuli))
        self.table.setShowGrid(False)
        session_start_time = time.mktime(session.start_date.timetuple())
        index = 0
        green_bg_brush = QtGui.QBrush(QtGui.QColor("#80E680"))
        red_bg_brush = QtGui.QBrush(QtGui.QColor("#FF9999"))
        green_fg_brush = QtGui.QBrush(QtGui.QColor("#142D21"))
        red_fg_brush = QtGui.QBrush(QtGui.QColor("#4C0000"))
        for stimulus in session.stimuli:
            bg_brush = red_bg_brush
            fg_brush = red_fg_brush
            if stimulus.correct:
                bg_brush = green_bg_brush
                fg_brush = green_fg_brush
            self.table.setItem(index, 0, QtGui.QTableWidgetItem(stimulus.valid))
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

    def resizeEvent(self, ev):
        self.table.setGeometry(0, 0, self.width(), self.height())

class HistogramTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(HistogramTab, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def update_tab(self, session):
        reaction_times = [1000 * (stimulus.action_time - stimulus.effective_time) for stimulus in session.stimuli if
                          stimulus.action_time]
        ax = self.figure.add_subplot(111)
        ax.hist(reaction_times)
        self.canvas.draw()
