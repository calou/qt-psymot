# -*- coding: utf8 -*-
import sys

from app.gui.gui import *


def main():
    
    app = QtGui.QApplication(sys.argv)
    widget = ManagePatientWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()