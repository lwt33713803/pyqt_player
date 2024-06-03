import os

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt, QSize, QEvent
from PyQt6.QtGui import QMouseEvent, QIcon, QPixmap, QImage, QColor
from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QToolButton, QLabel, QHBoxLayout, QSizePolicy
from my_app.utils.helpers import load_stylesheet


class HoverableHBoxLayout(QHBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.Enter:
            obj.setStyleSheet("background-color: lightblue;")
        elif event.type() == QEvent.Type.Leave:
            obj.setStyleSheet("background-color: none;")
        return super().eventFilter(obj, event)

class Ui_MainWindow(object):
    _startPos = None
    _endPos = None
    _isTracking = False

    def setupUi(self, MainWindow):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # qss
        qss_file = "my_app/assets/styles/style.qss"
        stylesheet = load_stylesheet(qss_file)
        MainWindow.setStyleSheet(stylesheet)
        MainWindow.setFixedSize(640, 400)
        MainWindow.setObjectName("main_window")

        mainWindowWeight = QWidget(parent=MainWindow)
        mainWindowWeight.setObjectName("main_widget")

        hLayout = QHBoxLayout(mainWindowWeight)
        hLayout.setObjectName("main_layout")
        hLayout.setContentsMargins(0, 0, 0, 0)

        # 创建左侧部件
        left_widget = QWidget(parent=mainWindowWeight)
        left_layout = QVBoxLayout(left_widget)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        left_layout.setContentsMargins(20, 20, 20, 20)

        left_widget.setObjectName("left_panel")
        left_layout.setObjectName("left_layout")

        # 创建右侧部件
        right_widget = QWidget(parent=mainWindowWeight)
        right_layout = QVBoxLayout(right_widget)
        right_widget.setObjectName("right_panel")
        right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        right_layout.setContentsMargins(20, 20, 20, 20)
        right_layout.setObjectName("right_layout")

        # 将左右部件添加到主布局中
        hLayout.addWidget(left_widget)
        hLayout.addWidget(right_widget)
        hLayout.setStretch(0, 1)
        hLayout.setStretch(1, 2)

        ### 左侧布局组件
        logo = QLabel(parent=mainWindowWeight)
        logo.setObjectName("label")
        image_path = os.path.join(current_dir, "assets/images/logo.jpg")
        pixmap = QPixmap(image_path)
        width, height = 100, 100
        scaled_pixmap = pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setPixmap(scaled_pixmap)
        logo.setFixedHeight(150)
        logo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        title = QLabel(parent=mainWindowWeight)
        title.setObjectName("title")
        title.setText("引力播放器")
        title.setStyleSheet("font-size:16px;font-weight:bold;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        version = QLabel(parent=mainWindowWeight)
        version.setObjectName("version")
        version.setText("1.3.4")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        left_layout.addWidget(logo)
        left_layout.addWidget(title)
        left_layout.addWidget(version)

        ### 右侧布局组件
        openWidget = QWidget(parent=mainWindowWeight)
        openLayout = QHBoxLayout(openWidget)
        openWidget.setContentsMargins(0, 0, 0, 0)
        openUrlWidget = QWidget(parent=mainWindowWeight)
        openUrlLayout = QHBoxLayout(openUrlWidget)
        right_layout.setSpacing(0)
        openHistoryWidget = QWidget(parent=mainWindowWeight)
        openHistoryLayout = HoverableHBoxLayout(openHistoryWidget)

        right_layout.addWidget(openWidget)
        right_layout.addWidget(openUrlWidget)
        right_layout.addWidget(openHistoryWidget)

        openText = QLabel(parent=mainWindowWeight)
        openText.setObjectName("title_open_local")
        openText.setText("打开...")
        openText.setStyleSheet("font-size:12px;font-weight:normal;")
        openText.setAlignment(Qt.AlignmentFlag.AlignLeft)

        openTextHotkey = QLabel(parent=mainWindowWeight)
        openTextHotkey.setObjectName("title_open_local_hotkey")
        openTextHotkey.setText("COMMAND + O")
        openTextHotkey.setStyleSheet("font-size:12px;font-weight:normal;")
        openTextHotkey.setAlignment(Qt.AlignmentFlag.AlignRight)

        openLayout.setAlignment(Qt.AlignmentFlag.AlignBaseline)
        openLayout.addWidget(openText)
        openLayout.addWidget(openTextHotkey)

        openUrlText = QLabel(parent=mainWindowWeight)
        openUrlText.setObjectName("title_open_url")
        openUrlText.setText("打开 URL...")
        openUrlText.setStyleSheet("font-size:12px;font-weight:normal;")
        openUrlText.setAlignment(Qt.AlignmentFlag.AlignLeft)

        openUrlTextHotkey = QLabel(parent=mainWindowWeight)
        openUrlTextHotkey.setObjectName("title_open_local_hotkey")
        openUrlTextHotkey.setText("SHIFT + CTRL + O")
        openUrlTextHotkey.setStyleSheet("font-size:12px;font-weight:normal;")
        openUrlTextHotkey.setAlignment(Qt.AlignmentFlag.AlignRight)

        openUrlLayout.addWidget(openUrlText)
        openUrlLayout.addWidget(openUrlTextHotkey)
        openUrlLayout.setAlignment(Qt.AlignmentFlag.AlignBaseline)

        openItemIcon = QLabel(parent=mainWindowWeight)
        openItemIcon.setObjectName("open_item_icon")
        open_item_icon_path = os.path.join(current_dir, "assets/icons/files.png")
        open_item_pixmap = QPixmap(open_item_icon_path)
        open_item_scaled_pixmap = open_item_pixmap.scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)

        openItemIcon.setPixmap(open_item_scaled_pixmap)
        openItemIcon.setFixedHeight(20)
        openItemIcon.setFixedWidth(20)
        openItemIcon.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        openItemWidget = QLabel(parent=mainWindowWeight)
        openItemWidget.setObjectName("title_open_history_item")
        openItemWidget.setText("Download")
        openItemWidget.setStyleSheet("font-size:12px;font-weight:normal;")

        openHistoryLayout.addWidget(openItemIcon)
        openHistoryLayout.addWidget(openItemWidget)
        openHistoryLayout.setObjectName("open_history_item")

        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        MainWindow.setCentralWidget(mainWindowWeight)
        MainWindow.setWindowOpacity(0.96)
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        ####### 菜单按钮
        # 添加关闭按钮
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


    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

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

    def focusInEvent(self, event):
        pass

    def focusOutEvent(self, event):
        # 当窗口失去焦点时恢复默认样式
        self.mainWindowWeight.setStyleSheet()

    def isFullScreen(self):
        pass

    def showNormal(self):
        pass

    def showFullScreen(self):
        pass

    def pos(self):
        pass

    def width(self):
        pass
