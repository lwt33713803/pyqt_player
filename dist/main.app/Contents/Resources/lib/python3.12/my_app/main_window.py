from PyQt6.QtWidgets import QMainWindow
from my_app.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.initUI()

    # def initUI(self):