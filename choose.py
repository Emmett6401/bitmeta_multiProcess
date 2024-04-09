import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyupbit


form_choose = uic.loadUiType("./res/dlg_choose.ui")[0]

class chooseMyInterestCoin(QDialog, form_choose):
    newInter = []
    def __init__(self,parent):        
        super().__init__() #속성및 메소드를 모두 가져옴
        self.setupUi(self)        
        self.btnBox.accepted.connect(self.accept)
        self.btnBox.rejected.connect(self.reject)    
        # self.btnInter1.clicked.connect(self.btnInter1Clicked)
        # self.btnRelease.clicked.connect(self.fncRelease)
        self.listWidget_2.itemSelectionChanged.connect(self.btnInter1Clicked)

        self.setModel()
        return

    def btnInter1Clicked(self):
        global newInter
        items = self.listWidget_2.selectedItems()
        for item in items:
            newInter = item.text()
            print('QRY', newInter)
        return

    def fncQuary(self):
        global newInter
        items = self.listWidget_2.selectedItems()                
        for item in items:
            newInter = item.text()
            print('QRY', newInter)
        price_history = pyupbit.get_ohlcv(ticker=newInter)        
        self.create_table_widget(self.tableWidget, price_history)
        return

    def create_table_widget(self, widget, df):
        widget.setRowCount(len(df.index))
        widget.setColumnCount(len(df.columns))
        widget.setHorizontalHeaderLabels(df.columns)  
        # widget.setVerticalHeaderLabels(df.index)
        for row_index, row in enumerate(df.index):
            for col_index, column in enumerate(df.columns):
                value = df.loc[row][column]
                item = QTableWidgetItem(str(value))
                widget.setItem(row_index, col_index, item)
        # 위젯의 컬럼 조정 
        widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)     
        return

    def fncRelease(self):
        print('RLS')
        return
    def setModel(self):
        krwCoins = pyupbit.get_tickers("KRW")        
        for krwCoin in krwCoins:
            self.listWidget_2.addItem(krwCoin)
        self.listWidget_2.sortItems()
        return    
    @staticmethod
    def launch(parent):
        dlg = chooseMyInterestCoin(parent)
        r = dlg.exec()
        if r : 
            return newInter
        return None    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = chooseMyInterestCoin(None)
    dlg.show()
    app.exec_()