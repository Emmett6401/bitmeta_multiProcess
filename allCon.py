import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStyleFactory, QSizePolicy, QWidget, QHBoxLayout, QFrame
from PyQt5.QtGui import QColor
import win32gui
import win32api
import win32con


# 핸들러 가져오기
hwnd = win32gui.GetForegroundWindow()

# 윈도우 스타일 가져오기
style = win32api.GetWindowLong(hwnd, win32con.GWL_STYLE)

# 윈도우 스타일 설정하기
style &= ~win32con.WS_CAPTION
style &= ~win32con.WS_THICKFRAME
style &= ~win32con.WS_MINIMIZEBOX
style &= ~win32con.WS_MAXIMIZEBOX
style &= ~win32con.WS_SYSMENU
win32api.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

# 레이어드 윈도우로 설정
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

# 투명도 설정
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 255, win32con.LWA_COLORKEY)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # central widget 설정
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 버튼 추가
        self.button = QPushButton("Click me!", self)
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 버튼을 넣을 수 있는 레이아웃 추가
        self.layout = QHBoxLayout(self.central_widget)
        self.layout.addWidget(self.button)

        self.setStyleSheet('''
            /* QMainWindow */
            QMainWindow {
                background-color: #404040;
                color: #F0F0F0;
            }
            /* QHeaderView */
            QHeaderView {
                background-color: #404040;
                color: #F0F0F0;
                border: none;
                border-radius: 0px;
            }
            QHeaderView::section {
                background-color: #404040;
                color: #F0F0F0;
                border: none;
                border-radius: 0px;
                padding: 4px;
            }
            QHeaderView::section:hover {
                background-color: #505050;
            }
            /* QMenuBar */
            QMenuBar {
                background-color: #303030;
                color: #F0F0F0;
            }
            QMenuBar::item:selected {
                background-color: #7B7B7B;
            }
            /* QToolBar */
            QToolBar {
                background-color: #404040;
                border: none;
            }
            /* QFrame */
            QFrame {
                border: none;
                background-color: #404040;
            }
            /* QStatusBar */
            QStatusBar {
                background-color: #303030;
            }
            /* QPushButton */
            QPushButton {
                background-color: #606060;
                border: none;
                border-radius: 5px;
                color: #F0F0F0;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #7B7B7B;
            }
            QPushButton:pressed {
                background-color: #505050;
            }
            /* QComboBox */
            QComboBox {
                background-color: #606060;
                color: #F0F0F0;
                border: none;
                border-radius: 5px;
            }
            QComboBox:hover {
                background-color: #7B7B7B;
            }
            /* QLineEdit */
            QLineEdit {
                background-color: #606060;
                color: #F0F0F0;
                border: none;
                border-radius: 5px;
            }
            /* QScrollBar */
            QScrollBar {
                background-color: #606060;
                border-radius: 5px;
                width: 10px;
            }
            QScrollBar::handle {
                background-color: #7B7B7B;
                border-radius: 5px;
            }
            QScrollBar::add-page, QScrollBar::sub-page {
                background-color: #606060;
                border-radius: 5px;
            }
            /* QCheckBox */
            QCheckBox {
                color: #F0F0F0;
            }
            QCheckBox::indicator {
                background-color: #606060;
                border: none;
                width: 15px;
                height: 15px;
            }
            QCheckBox::indicator:checked {
                background-color: #7B7B7B;
            }
            ''')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())