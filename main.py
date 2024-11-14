from PySide2.QtWidgets import QApplication
from pybrowser import MainWindow
import sys

app = QApplication()

win = MainWindow()
win.add_web_tab()
win.show()

app.exec_()
