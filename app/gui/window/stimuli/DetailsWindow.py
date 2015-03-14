# -*- coding: utf8 -*-
from app.model.stimuli import *
from app.gui.button import *
from app.gui.design.StylesheetHelper import *
from app.gui.base import *

class DetailsWindow(Window):
    def __init__(self, parent):
        super(DetailsWindow, self).__init__(parent)
        Window.init(self, parent, "Détails des tests")
