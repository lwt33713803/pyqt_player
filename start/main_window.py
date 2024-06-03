from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton
from start.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
