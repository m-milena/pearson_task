from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QAction, QDialog, QApplication
from NNinterface import NNinterface
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = NNinterface()
    dlg.show()
    app.exec()
