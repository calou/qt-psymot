# -*- coding: utf8 -*-
import sys
from PyQt5 import QtWidgets
from db import Repository
from gui.WindowManager import *



def main():
    app = QtWidgets.QApplication(sys.argv)
    database_manager = Repository.DatabaseManager()
    database_manager.migrate()
    widget = WindowManager()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()