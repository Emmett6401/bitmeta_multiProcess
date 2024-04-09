from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

app = QApplication([])
app.setStyle('fusion')

# 전체 위젯의 배경색상과 텍스트 색상을 설정
palette = QPalette()
palette.setColor(QPalette.Window, QColor(30, 30, 30))
palette.setColor(QPalette.WindowText, QColor(200, 200, 200))
app.setPalette(palette)

# 위젯 추가
widget = QWidget()
label = QLabel('Hello, World!')
layout = QVBoxLayout()
layout.addWidget(label)
widget.setLayout(layout)

widget.show()
app.exec_()






