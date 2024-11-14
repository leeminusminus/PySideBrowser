#!/usr/bin/python3

from PySide6.QtWidgets import QApplication
from pybrowser6 import MainWindow
import sys

app = QApplication()

win = MainWindow()
win.new_tab()
win.show()

app.exec()
