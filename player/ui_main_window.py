from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from utils.helpers import load_stylesheet
from PyQt6.QtMultimedia import QMediaPlayer, QMediaFormat, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget

class Ui_MainWindow(object):
    _startPos = None
    _endPos = None
    _isTracking = False

    def __init__(self):
        super().__init__()
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self.videoContainerWidget = QVideoWidget()
        self.setCentralWidget(self.videoContainerWidget)
        self._player.setVideoOutput(self.videoContainerWidget)

    def play(self):
        fp = '/Users/john/Desktop/video_res/1.mp4'
        self._player.setSource(QUrl.fromLocalFile(fp))
        self._player.play()

    def setupUi(self, MainWindow):
        # qss
        qss_file = "player/assets/styles/style.qss"
        stylesheet = load_stylesheet(qss_file)
        MainWindow.setStyleSheet(stylesheet)
        MainWindow.setFixedSize(1200, 800)
        MainWindow.setObjectName("player_window")

        currentWindows = QWidget(parent=MainWindow)
        currentWindows.setObjectName("player_widget")

        mainLayout = QVBoxLayout(currentWindows)
        mainLayout.setObjectName("main_layout")
        mainLayout.setContentsMargins(0, 0, 0, 0)


        self.videoConterWidget = QtWidgets.QWidget(currentWindows)
        self.videoConterWidget.setStyleSheet("background:#ff00ff")
        mainLayout.addWidget(self.videoContainerWidget)
        mainLayout.addWidget(self.videoConterWidget)
        mainLayout.setStretch(0,9)
        mainLayout.setStretch(1, 1)
        mainLayout.setSpacing(0)


        MainWindow.setCentralWidget(currentWindows)
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.setUpButtons(MainWindow)


    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()


    def setUpButtons(self, MainWindow):

        ####### 菜单按钮
        close_button = QPushButton(parent=MainWindow)
        close_button.clicked.connect(MainWindow.close)
        close_button.setObjectName("close_btn")
        close_button.setProperty("class", "button_circle")
        close_button.setGeometry(10, 10, 12, 12)

        # 添加最小化按钮
        minimize_button = QPushButton(parent=MainWindow)
        minimize_button.clicked.connect(MainWindow.showMinimized)
        minimize_button.setObjectName("mini_btn")
        minimize_button.setProperty("class", "button_circle")
        minimize_button.setGeometry(30, 10, 12, 12)

        # 添加全屏按钮
        fullscreen_button = QPushButton(parent=MainWindow)
        fullscreen_button.setProperty("class", "button_circle")
        fullscreen_button.setGeometry(50, 10, 12, 12)
        minimize_button.clicked.connect(MainWindow.toggle_fullscreen)


    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.MouseButton.LeftButton:
            self._isTracking = True
            self._startPos = e.pos()

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.MouseButton.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
