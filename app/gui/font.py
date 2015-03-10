import os
from PyQt5.QtGui import QFontDatabase


class FontManager():
    @staticmethod
    def install_fonts():
        font_files = os.listdir("assets/fonts")
        for font_file in font_files:
            file = "assets/fonts/" + font_file
            QFontDatabase.addApplicationFont(file)

    @staticmethod
    def get_font(ttf, family, size):
        print("Ajout de la police %s" % ttf)
        QFontDatabase.addApplicationFont(ttf)
        font_database = QFontDatabase()
        return font_database.font(family, "normal", size)

    @staticmethod
    def get_title_font():
        return FontManager.get_font("assets/fonts/GeosansLight.ttf", "GeosansLight", 20)

    @staticmethod
    def get_sub_title_font():
        return FontManager.get_font("assets/fonts/GeosansLight.ttf", "GeosansLight", 16)