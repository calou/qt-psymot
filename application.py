# -*- coding: utf8 -*-
import sys
from app.gui.WindowManager import *


def main():
    
    app = QtWidgets.QApplication(sys.argv)
    widget = WindowManager()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()