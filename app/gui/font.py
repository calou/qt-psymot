import os
from PyQt4 import QtGui, QtCore


class FontManager():
    @staticmethod
    def install_fonts():
        font_files = os.listdir("assets/fonts")
        for font_file in font_files:
            file = "assets/fonts/" + font_file
            QtGui.QFontDatabase.addApplicationFont(file)

    @staticmethod
    def get_font(ttf, family, size):
        QtCore.qDebug("Ajout de la police %s" % ttf)
        QtGui.QFontDatabase.addApplicationFont(ttf)
        font_database = QtGui.QFontDatabase()
        return font_database.font(family, "normal", size)

    @staticmethod
    def get_title_font():
        return FontManager.get_font("assets/fonts/GeosansLight.ttf", "GeosansLight", 20)

    @staticmethod
    def get_sub_title_font():
        return FontManager.get_font("assets/fonts/GeosansLight.ttf", "GeosansLight", 16)