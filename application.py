# -*- coding: utf8 -*-
import sys
from gui import *

def main():
    
    app = QtGui.QApplication(sys.argv)
    widget = ManagePatientWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()