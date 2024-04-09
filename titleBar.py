import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStyleFactory, QSizePolicy, QWidget, QHBoxLayout, QFrame
from PyQt5.QtGui import QColor
import ctypes

# # Windows 10의 Dark mode를 활성화
# if hasattr(ctypes.windll, "uxtheme"):
#     # Windows API에서 사용할 라이브러리를 로드합니다.
#     ctypes.windll.uxtheme.SetPreferredAppMode(1)
#     ctypes.windll.uxtheme.SetThemeAppProperties(
#         ctypes.c_ulong(0x00000008))
    
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

        # 모든 위젯들을 white 테마로 바꾸는 스타일시트 설정
        self.setStyleSheet('''
            /* QMainWindow */
            QMainWindow {
                background-color: #F0F0F0;
                color: #404040;
            }
            /* QMenuBar */
            QMenuBar {
                background-color: #F0F0F0;
                color: #404040;
            }
            QMenuBar::item:selected {
                background-color: #D0D0D0;
            }
            /* QToolBar */
            QToolBar {
                background-color: #F0F0F0;
                border: none;
            }
            /* QFrame */
            QFrame {
                border: none;
                background-color: #F0F0F0;
            }
            /* QStatusBar */
            QStatusBar {
                background-color: #D0D0D0;
            }
            /* QPushButton */
            QPushButton {
                background-color: #E0E0E0;
                border: none;
                border-radius: 5px;
                color: #404040;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #D0D0D0;
            }
            QPushButton:pressed {
                background-color: #E0E0E0;
            }
            /* QComboBox */
            QComboBox {
                background-color: #E0E0E0;
                color: #404040;
                border: none;
                border-radius: 5px;
            }
            QComboBox:hover {
                background-color: #D0D0D0;
            }
            /* QLineEdit */
            QLineEdit {
                background-color: #E0E0E0;
                color: #404040;
                border: none;
                border-radius: 5px;
            }
            /* QScrollBar */
            QScrollBar {
                background-color: #E0E0E0;
                border-radius: 5px;
                width: 10px;
            }
            QScrollBar::handle {
                background-color: #D0D0D0;
                border-radius: 5px;
            }
            QScrollBar::add-page, QScrollBar::sub-page {
                background-color: #E0E0E0;
                border-radius: 5px;
            }
            /* QCheckBox */
            QCheckBox {
                color: #404040;
            }
            QCheckBox::indicator {
                background-color: #E0E0E0;
                border: none;
                width: 15px;
                height: 15px;
            }
            QCheckBox::indicator:checked {
                background-color: #D0D0D0;
            }
            ''')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
