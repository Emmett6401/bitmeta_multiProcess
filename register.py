import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyupbit
import datetime
import webbrowser
from mysql import *

boolEchoMode = True
boolIDCheck = False
myDB = mySqlDB()

form_userinfo = uic.loadUiType("./res/dlg_userinfo.ui")[0]

class userInfo(QDialog, form_userinfo):
    def __init__(self,parent):
        super().__init__() #속성및 메소드를 모두 가져옴
        self.setupUi(self)        

        self.btnSummit.clicked.connect(self.summit)
        self.btnPWView.clicked.connect(self.btnPWViewToggle)

        self.listWidget_2.itemSelectionChanged.connect(self.btnGetInterClick_1)     
        
        self.btnIDCheck.clicked.connect(self.btnIDCheckClicked)        
        self.btnTeleHelp.clicked.connect(self.btnTeleHelpClicked)
        self.btnAPIHelp.clicked.connect(self.btnAPIHelpClicked)
        self.setModel()
        self.setMyVisable(False)

    def setMyVisable(self,flag):
        self.leCoinoneAPIKey.setVisible(flag)
        self.leCoinoneSkey.setVisible(flag)
        self.label_9.setVisible(flag)
        self.label_10.setVisible(flag)
        self.label_16.setVisible(flag)
        self.label_17.setVisible(flag)

        self.btnTeleHelp.setVisible(flag)
        self.leTeleAPINum.setVisible(flag)
        self.leTeleAPIKey.setVisible(flag)
        
    def btnTeleHelpClicked(self):
        webbrowser.open("https://www.welovedoctor.com/?p=9329")
        return 

    def btnAPIHelpClicked(self):
        webbrowser.open("https://upbit.com/service_center/open_api_guide")
        return 

    def btnIDCheckClicked(self):
        global boolIDCheck
        result = myDB.chkID(self.leID.text())    
        if result==None:
            QMessageBox.information(self,'ID생성','사용할 수 있는 ID 입니다.')
            boolIDCheck = True
        else :
            btnReply = QMessageBox.question(self, "ID생성","중복된 아이디 입니다. 다른 아이디를 입력 하시겠습니까?",\
                                        QMessageBox.Yes,QMessageBox.No)
            if btnReply == QMessageBox.No:
                QMessageBox.information(self,'ID생성','사용할 수 없는 ID 입니다.')                
                return

    def btnGetInterClick_1(self):
        items = self.listWidget_2.selectedItems()                        
        for item in items:
            self.leInter1.setText(item.text())
    # def btnGetInterClick_2(self):
    #     items = self.listWidget_2.selectedItems()
    #     for item in items:
    #         self.leInter2.setText(item.text())
    # def btnGetInterClick_3(self):
    #     items = self.listWidget_2.selectedItems()
    #     for item in items:
    #         self.leInter3.setText(item.text())        
    def btnPWViewToggle(self):
        global boolEchoMode
        if boolEchoMode == True:
            self.lePW.setEchoMode(QLineEdit.Normal)
            self.lePWC.setEchoMode(QLineEdit.Normal)
            boolEchoMode = False
        else:
            self.lePW.setEchoMode(QLineEdit.Password)
            self.lePWC.setEchoMode(QLineEdit.Password)
            boolEchoMode = True

    def summit(self):
        global boolIDCheck,myDB
        if boolIDCheck == False:
            QMessageBox.information(self,'ID중복확인','ID 중복확인을 먼저 실행 하세요')
            return
        if self.lePW.text() != self.lePWC.text():
            QMessageBox.information(self,'Password','패스워드를 확인해 주세요요')
            return
        now = datetime.datetime.now() 
        nowDate = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
        # myDB.insert2(self.leID.text(),self.lePW.text())
        myDB.insert(self.leID.text(),self.lePW.text(),self.leName.text(),self.lePhone.text(),'1',nowDate, \
            self.leUpbitIP.text(),self.leUpbitAPIKey.text(),self.leUpbitSkey.text(),\
            self.leCoinoneAPIKey.text(),self.leCoinoneSkey.text(), self.leTeleAPINum.text(), self.leTeleAPIKey.text(),\
            self.leInter1.text(),self.leInter1.text(),self.leInter1.text())
        QMessageBox.information(self,'ID생성','정상적으로 처리 되었습니다.')
        self.accept()
    def fncQuary(self):
        global myInterest
        items = self.listWidget_2.selectedItems()                
        for item in items:
            myInterest = item.text()
            print('QRY', myInterest)
        price_history = pyupbit.get_ohlcv(ticker=myInterest)
        # pprint.pprint(type(price_history))
        # pprint.pprint(price_history.columns)
        # pprint.pprint(price_history)        
        self.create_table_widget(self.tableWidget, price_history)

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

    def fncRelease(self):
        print('RLS')
    def setModel(self):
        krwCoins = pyupbit.get_tickers("KRW")        
        for krwCoin in krwCoins:
            self.listWidget_2.addItem(krwCoin)
        self.listWidget_2.sortItems()
    @staticmethod
    def launch(parent):
        dlg = userInfo(parent)
        r = dlg.exec()
        if r : 
            return True
        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = userInfo(None)
    ex.show()
    sys.exit(app.exec_())