from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QTextCharFormat, QColor, QBrush

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def setFormattedNumber(self, number):
        formatted_number = "{:,.4f}".format(number)
        self.setText(str(formatted_number))

    def setFormattedNumberWithColor(self, number, min_value):
        formatted_number = "{:,.4f}".format(number)
        self.setText(str(formatted_number))
        if number < min_value:
            self.setStyleSheet('color:red')
        else:
            self.setStyleSheet('color:black')
