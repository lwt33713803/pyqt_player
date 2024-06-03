import sys
from PyQt6.QtWidgets import QApplication, QPushButton
from start.main_window import MainWindow as StartMainWindow
from player.main_window import MainWindow as PlayerMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = StartMainWindow()
    player = PlayerMainWindow()
    start.show()
    start.openUrlWidget.clicked.connect(player.show)
    start.openUrlWidget.clicked.connect(start.hide)
    sys.exit(app.exec())

