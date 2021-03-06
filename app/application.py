# -*- coding: utf8 -*-
import sys
from PyQt4 import QtGui
from db import repository
from gui.WindowManager import *



def main():
    app = QtGui.QApplication(sys.argv)

    """
    Migration de base de données
    """
    database_manager = repository.DatabaseManager()
    database_manager.migrate()
    widget = WindowManager()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()