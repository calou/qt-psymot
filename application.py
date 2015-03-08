# -*- coding: utf8 -*-
import sys
from app.gui.ManagePatientsWindow import *


def main():
    
    app = QtWidgets.QApplication(sys.argv)
    widget = ManagePatientWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()