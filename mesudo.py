import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *


form_mesudo = uic.loadUiType("./res/dlg_mesudo.ui")[0]

class mesuDo(QDialog, form_mesudo):
    myInterBal = 0.0
    mSellQty = 0.0
    # 여기는 매수 매도 할때 물어 보는 다얄로그
    def __init__(self,msg, mInterbal):
        super().__init__() #속성및 메소드를 모두 가져옴
        self.setupUi(self)        
        self.checkBox.toggled.connect(self.checkBox_toggled)
        self.comboBox.activated[str].connect(self.onActivated)
        self.buttonBox.accepted.connect(self.acceptReturn)
        self.buttonBox.rejected.connect(self.rejectReturn)
        self.label.setText(msg)
        self.myInterBal = mInterbal
        self.onActivated(self.comboBox.currentText())
        return
    def onActivated(self, text):        
        nVal = int(text.split(' ')[0])
        # print(text, nVal)

        if self.checkBox.isChecked() :
            self.lineEdit.setText(str(self.myInterBal))
        else:            
            self.lineEdit.setText(str(self.myInterBal * nVal / 100))

    def checkBox_toggled(self):
        if self.checkBox.isChecked() :
            self.lineEdit.setText(str(self.myInterBal))
            
        else :            
            self.lineEdit.setText('0')
        return
    def acceptReturn(self):   
        global mSellQty     
        mSellQty = float(self.lineEdit.text())
        return True
    def rejectReturn(self):        
        global mSellQty
        mSellQty = 0.0
        return False

    @staticmethod
    def launch(msg,myInterBal):
        dlg = mesuDo(msg,myInterBal)
        r = dlg.exec()
        if r : 
            return mSellQty
        return None
    def showModal(self):
            return super().exec_()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = mesuDo('매도 할 수량을 입력하세요')
    dlg.show()
    app.exec_()