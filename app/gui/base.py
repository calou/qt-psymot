from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FontManager():
    @staticmethod
    def get_font(ttf, family):
        print("Ajout de la police %s" % ttf)
        QFontDatabase.addApplicationFont(ttf)
        font_database = QFontDatabase()
        font = font_database.font(family, "normal", 20)
        return font

    @staticmethod
    def get_title_font():
        return FontManager.get_font("assets/fonts/GeosansLight.ttf", "GeosansLight")

class Window(QWidget):
    def setTitle(self, patients_):
        title = QLabel(patients_)
        font = FontManager.get_title_font()
        title.setFont(font)
        font.setPointSize(20)
        title.setContentsMargins(0, 0, 0, 10)
        return title
