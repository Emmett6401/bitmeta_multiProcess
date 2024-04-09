import sys,os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyupbit
import time
import datetime
from mysql import *
from choose import *
from mesudo import *
from register import *
from login import *
import threading


# import # pprint 
# from time import sleep
# import logging
# import psutil #process 찾아서 kill 하기 위함.
import webbrowser 
from version import __version__
from customLineedit import CustomLineEdit  

# pyinstaller -F -w --icon=./res/2.ico bitmeta.py
# https://slays.tistory.com/42 파이 인스톨 관련 

'''
23.01.25 작업 내용
dBot에서 작업 중 임
pyinstaller -F -w --icon=./res/2.ico gbot.py
1. 반복 매입을 적용 : 툴팁에 써 놓았음.
2. 즉시 적용을 적용 : 툴팁에 써 놓았음.
3. 정산 주기를 적용하였음 1분 3분 5분 등~~~ 240분까지 초단타 모드임
아이고 정신 없어 적어라 적어 으~~~~~~

23.01.26 
1. 속도 개선을 위해 dlg를 모두 독립 클래스로 옮김
2. 안정성을 위해 dlg 클래스와 메인 윈도간의 데이터 교환 login, mesudo는 전혀 다른 방식임. 
3. 스레드는 안됨. 고생만 했음. 언젠간 되겠지.
4. 작업폴더는 ebot임 

다음 작업은 
1. 오토업뎃
2. 멀티 코인을 1개 프로그램에서 (3개까지) - 
   프로램램이 멀티로 돌때 업비트에 쿼리가 동시에 이루어 질경우 프로그램중 1개가 다운되는것으로 보이기 때문
3. 쓰레드 구현으로 랙을 더 최소화 할 수 잇는지 보겠음.  

'''

"""

학교 - 102호
A = 7zP2nTa5XfTBW8Nr7AFvChMN6O0w4Fv8Obd38zD0
S = cXHPms611PX2RMpLQx1qIs5X6iIxWctxnw2uKk8G
IP = 1.221.32.156
"""

mBool_login = False
mBool_teleService = False
mBool_DangilMesu = False
mBool_autoWarning = False

nTimerEvent = 500 # 100 millisecond
mMinBuyAmount = 5000
mMilliSecond = 0
mSecond = 0
mMinute = 0
mJugiMinute = 0

mByunYul = 50.000000
mTujaYul = 0.0
mMesudoQty = 0.0
myInterestBalance = 0.0
myInterest = ''
pmyInterest = ''

mKrwBalance = 0.0
mKrwBalance4Buy = 0

mTargetPrice = 0.0
mLastInterPrice = 0.0
mCurrentInterPrice = 0.0

mCurNoTrade = 0
mPreNoTrade = -1
mMesuPrice = 0.0
mYesterMax = 0.0
mYesterMin = 0.0
mYesterRange = 0.0
mAvgMesuPrice = 0.0
mTotJasan = 0.0
mCalcTargetJugi = 2 #7days 1d 1hour
mTitleVersion = '24시간 bit & Meta 2023.02.19 서버이전' 
mTitleVersion = '24시간 bit & Meta 2023.05.25 DB복구' 
mTitleVersion = '24시간 bit & Meta 2023.10.27 월루서버' 
mTitleVersion = '24시간 bit & Meta 2023.12.30 아리시골' 
mTitleVersion = '24시간 bit & Meta ' + __version__ + ' #아리 반올림' 

# myThread =[]
myDB = mySqlDB()

prevNow = datetime.datetime.now() 
form_mainWin = uic.loadUiType("./res/window8.ui")[0]
class WorkerThread(QThread):
    finished = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.stopped = False
    def run(self):
        while not self.stopped:
            # 스레드에서 수행할 작업을 여기에 작성합니다.
            try:
                # startTime = time.time()
                global mCurrentInterPrice, mAvgMesuPrice, mTotJasan
                global myInterestBalance,mKrwBalance, mKrwBalance4Buy, mBool_login                                
                mCurrentInterPrice =  pyupbit.get_current_price(myInterest)
                time.sleep(0.007)
                myInterestBalance = myUpbit.get_balance(myInterest) #matic 잔고 가져오기 모두
                time.sleep(0.007)
                mKrwBalance = round(myUpbit.get_balance("KRW"),4) #원화 잔고 가져오기   
                time.sleep(0.007)                
                mAvgMesuPrice = myUpbit.get_avg_buy_price(myInterest)                
                # print(f'Debugging mAvgMesuPrice{mAvgMesuPrice} mKrwBalanceP{mKrwBalance} myInterestBalance{myInterestBalance} mCurrentInterPrice{mCurrentInterPrice}')
                # endTime=time.time()
                # 실행 시간 계산
                # executionTime = endTime - startTime
                # print(f"Debugging 실행 시간: {executionTime} 초")

            except Exception as e:
                print(e)                
            # time.sleep(0.2)            

    def stop(self):
        self.stopped = True
    def restart(self):
        self.stopped = False
        self.start()
class MyWindow(QMainWindow, form_mainWin):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        qPixmapVar = QPixmap()
        #  초기값 설정
        self.setWindowTitle(mTitleVersion)
        self.pBarValue = 0
        self.pBarPlus = 23
        self.pBar.setValue(self.pBarValue)

        #버튼 박스 연결 하기
        self.btn_mesu.clicked.connect(self.btn_Mesu_clicked)
        self.btn_medo.clicked.connect(self.btn_Medo_clicked)        
        self.cBox_trade.toggled.connect(self.cBox_trade_toggled)
        self.cBox_zonbu.toggled.connect(self.cBox_zonbu_toggled)

        self.cBox_zonbu_mesuNot.toggled.connect(self.cBox_zonbu_mesuNot_toggled)
        self.cBox_banbok_trade.toggled.connect(self.cBox_banbok_trade_toggled)
        self.cBox_immediatery_trade.toggled.connect(self.cBox_immediatery_trade_toggled)
        
        #logo를 파일에서 읽기 
        # qPixmapVar.load("./res/bitmetaSmall2.png")        
        # self.lbl_bgImage.setPixmap(qPixmapVar)        
        self.round2 = 2
        self.round4 = 4

        #초기값
        self.lineEdit_tujaYul.setText('99.950000')
        self.lineEdit_gaingYul.setText('3.000000')

        
        self.comboBox_jugi.activated[str].connect(self.jugiActivated)
        
                
        #함수                
        self.lineEdit_tujaYul.returnPressed.connect(self.tujaYulChanged)        
        self.lineEdit_byunYul.returnPressed.connect(self.byunYulChanged)
        self.lineEdit_gaingYul.returnPressed.connect(self.gaingYulChanged)

        
        #메뉴연결
        self.actionRegister.triggered.connect(self.actionRegisterFunc)
        self.actionLogin.triggered.connect(self.loginDlg) 
        self.actionStop.triggered.connect(self.logoutFunction)
        self.actionBTasking.triggered.connect(self.actionCoinSelect)
        self.actionaBot.triggered.connect(self.actionaBotTasking)

        #타이머 셋팅
        self.timer = QTimer(self)        
        self.timer.timeout.connect(self.timerEvent)

        # WorkerThread 인스턴스 생성
        self.worker_thread = WorkerThread()


        self.botSendmsg('+++++++++++++++++++++++++++++++++++++')
        self.botSendmsg('+ 현재시각 '+str(datetime.datetime.now())+' +')
        self.botSendmsg('+    bitMeta 로봇이 실행 되었습니다.    +')
        self.botSendmsg('+++++++++++++++++++++++++++++++++++++')
        self.botSendmsg('+info+' + '메뉴-업비트-로그인 하세요')        
        return
    def closeEvent(self, event):
        # 프로그램이 종료될 때 WorkerThread 종료
        self.worker_thread.stop()
        event.accept()

    def jugiActivated(self,text):    
        global mJugiMinute                   
        self.botSendmsg('현재 정산 주기는 ' + text + '입니다.')
        self.reflesh()
        jugi = self.comboBox_jugi.currentText()
        if jugi == 'day':
            mJugiMinute = 0    
        else:        
            mJugiMinute = int(jugi.split('te')[1])
        return

    def tujaYulChanged(self):
        global mTujaYul, mBool_autoWarning
        pVal = mTujaYul
        try:
            mTujaYul = float(self.lineEdit_tujaYul.text())                
            if mTujaYul >= 100 :
                self.botSendmsg('수수료를 남겨 두어야 합니다')
                self.lineEdit_tujaYul.setText('99.9500')
                mTujaYul = float(self.lineEdit_tujaYul.text())            
            elif mTujaYul <= 0 :
                self.lineEdit_tujaYul.setText('10')
                mTujaYul = float(self.lineEdit_tujaYul.text())
        except:
            mTujaYul = pVal
        self.botSendmsg('보유 현금의 투자 비율이 변경 되었습니다.')
        self.reflesh()
        mBool_autoWarning  = False
        return

    def byunYulChanged(self): #변동률을 바꿨어 
        global mByunYul,mTargetPrice

        if self.lineEdit_byunYul.text() == '' or mByunYul <= 0 or mByunYul >= 100 :
            self.lineEdit_byunYul.setText('50.000000')            
        
        mByunYul = float(self.lineEdit_byunYul.text())

        formatted_number = "{:,.6f}".format(float(self.lineEdit_byunYul.text()) )            
        self.lineEdit_byunYul.setText(str(formatted_number ) )
        
        self.botSendmsg('적용변동률이 변경 되었습니다.')
        self.reflesh()
        return

    def gaingYulChanged(self):                
        self.botSendmsg('초단타 매매 수익률이 변경 되었습니다.')        
        self.reflesh()
        return

    def actionaBotTasking(self):
        webbrowser.open("https://www.bitmeta.kr")
        return

    def actionRegisterFunc(self):                
        ok = userInfo.launch(None)        
        if ok:        
            self.botSendmsg('가입 되었습니다.로그인 하세요.')
            self.loginDlg()
        else:
            QMessageBox.information(self,'회원가입','이미 가입 하였으면 로그인 하세요')
            self.loginDlg()
        return    

    def actionCoinSelect(self):
        global myInterest, myDB
        if self.chkLoginFirst() == False :
            return
        newInter = chooseMyInterestCoin.launch(None)                    
        if newInter :        
            if myInterest == newInter :
                return 
            else:
                # update myInterest
                myDB.update(session['id'],newInter)
                myInterest = newInter
                self.reflesh()
                self.botSendmsg('거래 종목이 변경 되었습니다.'+myInterest)                
                time.sleep(1)
                return                
        
    def chkLoginFirst(self):
        global mBool_login
        if mBool_login == False :            
            self.botSendmsg('먼저 로그인 해주세요.')
            return False
        return True   
    
    def loginDlg(self):
        global mBool_login,session,myInterest        
        session = bitmetaLogin.launch(None)        
        try:
            if session['myinterest1'] == '':
                session['myinterest1'] = 'KRW-BTC'
                self.botSendmsg('지정된 Ticker 가 없습니다. 지정하세요')
            if session:            
                if self.makeInstance()==True:
                    mBool_login = True                
                    self.botSendmsg(f"{session['id']}가 종목 {session['myinterest1']} : 로그인 되었습니다.")
                    self.lineEdit_idInfo.setText(f"{session['id']} - {session['username']}")                
                    # WorkerThread 실행
                    # self.worker_thread.start()
                    self.worker_thread.restart()
                    # TimerStart
                    self.timer.start(nTimerEvent)
                    return mBool_login
                else:
                    QMessageBox.warning(self,'로그인 정보 확인','접속 장소가 다르거나 로그인 정보를 확인해주세요.')
                    self.botSendmsg('접속 장소가 다르거나 로그인 정보를 확인해주세요.')
                    mBool_login = False
                    self.loginDlg()    
                    return False
            else:
                self.btn_Exit_clicked()
        except:
            session['myinterest1'] = 'KRW-BTC'
            self.botSendmsg('지정된 Ticker 가 없습니다. 지정하세요')
            return False
    
    def logoutFunction(self):
        global mBool_login
        global session
        if self.chkLoginFirst() == False :
            return
        
        # Thread & Timer Stop 
        self.worker_thread.stop()
        self.timer.stop()

        mBool_login = False
        session[0] = ''        
        session[1] = ''
        self.lineEdit_upbitPrice.setText('')
        self.lineEdit_yBottom.setText('')
        self.lineEdit_yTop.setText('')
        self.lineEdit_targetPrice.setText('')
        self.lineEdit_boyuMATIC.setText('')
        self.lineEdit_boyuKRW.setText('')
        self.lineEdit_idInfo.setText('미접속')
        if self.cBox_trade.isChecked():
            self.cBox_trade.toggle()                        
        self.botSendmsg('안전하게 로그아웃 되었습니다.')
        return

    def showDlgConfirm(self):
        text, ok = QInputDialog.getText(self,'Confirm',"'예'라고 입력하고 OK를 누르세요")
        if ok:
            self.lblAfterConfirm.setText("OK Confirmed")            
        else:
            self.lblAfterConfirm.setText("NOT Confirmed")
        return ok
                    

    def botSendmsg(self,msg):        
        global botTelegram,botMc
        global mBool_teleService        
        dt_now = datetime.datetime.now()
        
        msg = dt_now.strftime('%Y-%m-%d %H:%M:%S : ') + msg
        if mBool_teleService == False :
            self.textEdit_botSend.append(msg)            
            print(msg)
        else:
            try:            
                botTelegram.sendMessage(botMc,msg)
                
            except Exception as e:
                print(e)
        return
                  
    def btn_Mesu_clicked(self):
        # 강제매수 
        global mMesuPrice, mMinBuyAmount
        if self.chkLoginFirst() == False :
            return        
        if mKrwBalance4Buy < mMinBuyAmount:
            self.botSendmsg('매수 금액이 최저 금액 보다 커야 합니다.')
            # for i in range(1,10):
            #     self.lineEdit_tujaYul.setEnabled(False) 
            #     sleep(0.10)
            #     self.lineEdit_tujaYul.setEnabled(True) 
            #     sleep(0.10)
            
            
            return 

        btnReply = QMessageBox.question(self, "수동 매수", '매수금액 = ' + str(format(mKrwBalance4Buy,',')) + '원',\
                                        QMessageBox.Yes,QMessageBox.No)
        
        if btnReply == QMessageBox.No:            
            return        
        resp = myUpbit.buy_market_order (myInterest, int(mKrwBalance4Buy) )                    
        if resp == None:            
            self.botSendmsg('매수 거래 최소 금액 5천원을 확인해 주세요')
            
        else:            
            mMesuPrice = mCurrentInterPrice            
            self.mesuSendMsg(resp,' 강제 매수가 진행 되었습니다.')             
        
        time.sleep(1) # 매수후 잔고 회복 시간을 줌     
        self.reflesh()            
        return

    def btn_Medo_clicked(self):
        # 강제매도 버튼을 누름
        # 은 초당 8회, 분당 200회 / 주문 외 요청은 초당 30회, 분당 900회 사용 가능합니다.
        global mMesudoQty
        if self.chkLoginFirst() == False or myInterestBalance <= 0:
            return        
        
        mMesudoQty = mesuDo.launch('매도 할 수량을 입력하세요',myInterestBalance)
        if mMesudoQty == 0 : 
            return                
        resp = myUpbit.sell_market_order(myInterest,mMesudoQty) #mMesudoQty는 Float으로 리턴됨        
        # print ('Debugging 강제 매도 하였는데 어쩔? ',resp)        
        try:        
            self.medoSendMsg (resp,' 강제 매도가 진행 되었습니다.')                       
        except:
            self.botSendmsg('거래가 이루어 지지 않았습니다.')
            self.botSendmsg(resp['error']['message'])                    
        
        time.sleep(1) # 매도후 잔고 회복 시간을 줌 
        self.reflesh()
        return

    def timerEvent(self):   
        if self.chkLoginFirst() == False :
            return
        self.dspStatus() # 화면을 갱신 Status + pBar + updown        
        self.dspCurrent() # 데이터 읽고 화면에 표시 시간이 오래 걸림
        self.gwaingYulMedoCheck() # 가서 0이면 리턴 함
        self.autoTrading() # 자동매매가서 오토 아니면 리턴함를 채크 한다.

        return
    def chk_autoTrade(self):
        if self.cBox_zonbu_mesuNot.isChecked() == True and self.cBox_zonbu.isChecked() == True :
            self.cBox_trade.setStyleSheet("color:  rgb(207, 207, 207)")
            self.cBox_trade.setEnabled (False)
        else :
            self.cBox_trade.setStyleSheet("color: black")
            self.cBox_trade.setEnabled (True)
        
    def cBox_zonbu_toggled(self):
        self.chk_autoTrade()
    def cBox_zonbu_mesuNot_toggled(self):
        if self.cBox_zonbu_mesuNot.isChecked() == True :
            self.cBox_immediatery_trade.setStyleSheet("color:  rgb(207, 207, 207)")
            self.cBox_banbok_trade.setStyleSheet("color:  rgb(207, 207, 207)")
            self.cBox_immediatery_trade.setEnabled (False)
            self.cBox_banbok_trade.setEnabled (False)            
        else:
            self.cBox_immediatery_trade.setStyleSheet("color: black")
            self.cBox_banbok_trade.setStyleSheet("color: black")
            self.cBox_immediatery_trade.setEnabled (True)
            self.cBox_banbok_trade.setEnabled (True)
        self.chk_autoTrade()

    def cBox_immediatery_trade_toggled(self):
        global mBool_DangilMesu
        if self.chkLoginFirst() == False :
            return
        if self.cBox_immediatery_trade.isChecked():
            self.botSendmsg('변동성 돌파 자동 거래 허가시 매입 조건을 즉시 적용합니다.')
            mBool_DangilMesu = False
        else:
            self.botSendmsg('매입 조건을 다음 정산 주기 부터 적용 합니다.')
            mBool_DangilMesu = True        

    def cBox_banbok_trade_toggled(self):        
        if self.chkLoginFirst() == False :
            return
        if self.cBox_banbok_trade.isChecked():
            self.botSendmsg('반복 매입이 가능합니다.')
        else:
            self.botSendmsg('반복 매입 차단!')

    def cBox_trade_toggled(self):                
        if self.chkLoginFirst() == False :
            return
        if self.cBox_trade.isChecked():            
            self.botSendmsg("자동 거래가 허가 되었습니다.")
        else :
            self.botSendmsg("자동 거래가 중지 되었습니다.")
        return
        

    def btn_Exit_clicked(self):        
        buttonReply = QMessageBox.question(self,'프로젝트 종료','프로젝트를 종료 할까요?')
        
        if buttonReply == QMessageBox.Yes:             
            exit(1)
        
    
    def dspStatus(self):   
        
        global mLastInterPrice    
        global mBool_login
        
        if mBool_login == False:
            return
        self.pBarValue += self.pBarPlus

        if self.pBarValue >= 100:
            self.pBarPlus = -10
            self.pBarValue = 100
        elif self.pBarValue <= 0:
            self.pBarPlus = 10
            self.pBarValue = 0
        self.pBar.setValue(self.pBarValue)
        

        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")        
        self.statusBar().showMessage(str_time)
        
        # #파일에서 그림 읽고 올라감 내려감 표시 하기  
        if mLastInterPrice > mCurrentInterPrice : #블루            
            self.lineEdit_upbitPrice.setStyleSheet("color:  blue")
        elif mLastInterPrice < mCurrentInterPrice : #레드            
            self.lineEdit_upbitPrice.setStyleSheet("color:  red")        
        else :
            self.lineEdit_upbitPrice.setStyleSheet("color:  black")                        

        # qPic = QPixmap()     

        # if mLastInterPrice > mCurrentInterPrice : #블루            
        #     qPic.load("./res/downArrow.png")
            
        # elif mLastInterPrice < mCurrentInterPrice : #레드            
        #     qPic.load("./res/upArrow.png")        
        # else :
        #     qPic.load("./res/equal.png")                        
        # qPic = qPic.scaledToWidth(51)
        # qPic = qPic.scaledToHeight(31)
        # self.lbl_matic_led.setPixmap(qPic)
        mLastInterPrice = mCurrentInterPrice

        return

        
    def cal_target(self):
        global mYesterMax,mYesterMin,mYesterRange,mTargetPrice,myInterest, mAvgMesuPrice
        global mBool_login, mKrwBalance4Buy
        
        jugi = self.comboBox_jugi.currentText()     
        try : 
            df = pyupbit.get_ohlcv(ticker = myInterest, interval = jugi, count = 3)  
            mAvgMesuPrice = myUpbit.get_avg_buy_price(myInterest)
            
            yesterday = df.iloc[-2]
            today = df.iloc[-1]
            yesterday_range = yesterday['high']-yesterday['low']
            target = today['open'] + yesterday_range * (mByunYul/100)
            
            mYesterMax = yesterday['high']            
            mYesterMin = yesterday['low']            
            mYesterRange = yesterday_range            
            mTargetPrice = target
            mKrwBalance4Buy =  round(mKrwBalance * (mTujaYul/100),6)
            
            
        except Exception as e:
            print(e)
            self.botSendmsg(f"cal_target 애러 발생 {e}")
            self.logoutFunction()        
        return
            
    def makeInstance(self):
        global myUpbit,myInterest,mKrwBalance
        global botTelegram,botMc
        global mBool_teleService
        global session        

        """Upbit API KEY """        
        try :            
            myInterest = session['myinterest1']        
            myUpbit = pyupbit.Upbit(session['upbitapi'], session['upbitsecret'])
            mKrwBalance = round(myUpbit.get_balance("KRW"),self.round2)            
            self.cal_target()
            
        except Exception as e:            
            print(e)
            print("Debugging make instance error ")
            return False
        return True
    
    def dspCurrent(self): 
        try:               
            self.lbl_upbitInterest.setText(myInterest) #나으 거래 코인            
            
            formatted_number = "{:,.6f}".format(mYesterMax)  # 쉼표 추가
            self.lineEdit_yTop.setText( str(formatted_number ) )
            
            formatted_number = "{:,.6f}".format(mYesterMin)  # 쉼표 추가
            self.lineEdit_yBottom.setText( str(formatted_number ) )
            
            # 타겟프라이스 
            formatted_number = "{:,.6f}".format(mTargetPrice)  # 쉼표 추가
            self.lineEdit_targetPrice.setText(str(formatted_number))
            
            formatted_number = "{:,.6f}".format(mCurrentInterPrice)
            self.lineEdit_upbitPrice.setText(str(formatted_number))

            formatted_number = "{:,.6f}".format(myInterestBalance)
            self.lineEdit_boyuMATIC.setText (str(formatted_number) )

            formatted_number = "{:,.6f}".format(mKrwBalance)
            self.lineEdit_boyuKRW.setText (str(formatted_number ) )
            if mKrwBalance4Buy < mMinBuyAmount:
                self.lineEdit_tujaKum.setStyleSheet('color:red')
            else:
                self.lineEdit_tujaKum.setStyleSheet('color:black')
                    
            formatted_number = "{:,.6f}".format(mKrwBalance4Buy)    
            self.lineEdit_tujaKum.setText (str(formatted_number ) )
            # print('Debugging ',self.lineEdit_tujaKum.text(),mKrwBalance4Buy )
                        
            if self.lineEdit_tujaYul.text() == '' :
                self.lineEdit_tujaYul.setText('99.950000')
            else:
                formatted_number = "{:,.6f}".format(float(self.lineEdit_tujaYul.text()) )    
                self.lineEdit_tujaYul.setText(str(formatted_number ) )

            if self.lineEdit_gaingYul.text() == '' :
                self.lineEdit_gaingYul.setText('0.000001')
            else:
                formatted_number = "{:,.6f}".format(float(self.lineEdit_gaingYul.text()) )    
                self.lineEdit_gaingYul.setText(str(formatted_number ) )

            gaingKum = mAvgMesuPrice + (mAvgMesuPrice * (float(self.lineEdit_gaingYul.text())/100 ))               
            formatted_number = "{:,.6f}".format(gaingKum)    
            self.lineEdit_gaingKum.setText(str(formatted_number ) )
            
            formatted_number = "{:,.6f}".format(mAvgMesuPrice)    
            self.lineEdit_avgMesu.setText(str(formatted_number ) )



            self.lineEdit_idInfo.setText(f"{session['id']} - {session['username']}")
            boyukum = round(myInterestBalance*mCurrentInterPrice,self.round2)
            formatted_number = "{:,.6f}".format(boyukum)    

            self.lineEdit_boyuMATIC_2.setText(str(formatted_number))        

            mTotJasan = boyukum + mKrwBalance
            formatted_number = "{:,.6f}".format(mTotJasan)
            self.lineEdit_boyuMATIC_3.setText (str(formatted_number) )
        except :
            print("Debugging 어딘가 0이다")

    def autoMedo(self):        
        try:
            if self.cBox_zonbu.isChecked() == True :
                self.botSendmsg('존버 중입니다.')
            else:    
                resp = myUpbit.sell_market_order(myInterest,myInterestBalance)                                                  
                self.medoSendMsg(resp,' 가격에 자동 매도가 진행 되었습니다.')
        except Exception as e:
            print(e)        
        
        time.sleep(1) # 매도후 잔고 회복 시간을 줌 
        self.reflesh()
        return
    
    def autoMesu(self):
        global mMesuPrice

        now = datetime.datetime.now()
        # print (f"Debugging  정산 주기가 {jugi} 이며 now={now} 입니다.")        
        if self.chkLoginFirst() == False :
            return
        try:            
            if self.cBox_zonbu_mesuNot.isChecked() == True :
                self.botSendmsg('존버 자동 매입 금지 중입니다.')
            elif self.cBox_trade_2.isChecked() == True and now.hour == 8 and now.minute == 59 and (0 <= now.second <= 59):
                self.botSendmsg('08:59 피크 함정 매입 금지 중입니다.')    
            else:
                resp = myUpbit.buy_market_order (myInterest, mKrwBalance4Buy)                            
                
                self.mesuSendMsg(resp,' 가격에 자동 매수가 진행 되었습니다.')
                mMesuPrice = mCurrentInterPrice 
        except Exception as e:
            print(e)     
        
        time.sleep(1) # 매수도후 잔고 회복 시간을 줌 
        self.reflesh()
        return
    def gwaingYulMedoCheck(self):
        # 목표 도달 했으면 강제 매도 하자                 
        if myInterestBalance <= 0 or mAvgMesuPrice > mCurrentInterPrice :
            return          
        # 현재 가격이 평균매수가격 + (평균매수가격  * 단타매도율)  
        if mCurrentInterPrice >= mAvgMesuPrice + (mAvgMesuPrice * (float(self.lineEdit_gaingYul.text())/100 )):
            try:
                resp = myUpbit.sell_market_order(myInterest,myInterestBalance)
                
                self.botSendmsg(f"평균 매입가 {mAvgMesuPrice } 보다 현재 가격 {mCurrentInterPrice }이 \
                    { self.lineEdit_gaingYul.text() }% 높아 오늘은1대박입니다.")
                self.botSendmsg(f"Ticker: { resp['market'] }")
                self.botSendmsg(f"총매도수량: 체결{ resp['volume']}/시도{ resp['remaining_volume'] } 수수료: { resp['remaining_fee'] }")
            except Exception as e:
                print(e)
        
        time.sleep(1) # 매수도후 잔고 회복 시간을 줌         
        self.reflesh()
        return

    def medoSendMsg(self,resp,msg):
        try:
            self.botSendmsg('거래가 ' + str(format(mCurrentInterPrice, ',')) + '에' + msg)
            self.botSendmsg(f"Ticker: { resp['market'] } 거래일시: { resp['created_at'] }")            
            self.botSendmsg(f"총매도수량: 체결{ resp['volume']}/시도{ resp['remaining_volume'] } 수수료: { resp['remaining_fee'] }")
        except Exception as e:
            print(e)
            print("Debugging def mesu_SendMsg 에러 발생")
            self.botSendmsg('매도가 진행 되지 못했습니다.')
            time.sleep(0.2)
        return
    
    def mesuSendMsg(self,resp,msg):
        try:
            self.botSendmsg('거래가 ' + str(format(mCurrentInterPrice, ',')) + '에 ' + msg)
            self.botSendmsg(f"Ticker: { resp['market'] } 거래일시: { resp['created_at'] }")            
            self.botSendmsg(f"총매입금액: { resp['price'] } 수수료: { resp['reserved_fee'] }")            
        except Exception as e:
            print(e)
            print("Debugging def mesu_SendMsg 에러 발생")
            self.botSendmsg('매수가 진행 되지 못했습니다. / 잔액 혹은 투자비율을 확인 하세요')
            time.sleep(0.2)
        return
    def dayJungsan(self, jugi):        
        global mBool_DangilMesu
        now = datetime.datetime.now()
        # print (f"Debugging 정산 주기가 {jugi} 이며 now={now} 입니다.")
        try:
            # 매도 기능 / 매일 아침 8시 59분 50초 ~ 09시 00분 00초 사이에 무조건 매도        
            if now.hour == 8 and now.minute == 59 and (1 <= now.second <= 19):                
                if myInterestBalance > 0:
                    self.autoMedo()
                time.sleep(5)                                        
                time.sleep(1) # 매수도후 잔고 회복 시간을 줌 
                mBool_DangilMesu = False
            # 09시 00분 20초~30초 사이에 금일의 매수 타겟 가격을 구해 온다. 
            if now.hour == 9 and now.minute == 0 and (20<= now.second <= 30): #09:00이 되어야 목표가 갱신이 된다.                 
                time.sleep(10) #10초간 슬립                            
                time.sleep(1) # 매수도후 잔고 회복 시간을 줌 
                self.reflesh()
                self.botSendmsg('일봉 정산 실행 후 타겟 재 계산')
        except Exception as e:
            print(e)
            print("Debugging autoTrading 에러 발생")
        
        return
    
    def minJungsan(self, jugi):        
        global mBool_DangilMesu, prevNow, mJugiMinute ,myInterestBalance
        if mJugiMinute == 0 :
            return
        now = datetime.datetime.now()        
        nextJungsan = prevNow + datetime.timedelta(minutes=mJugiMinute)        
        if now >= nextJungsan:            
            # print (f"Debugging 정산 주기가 {jugi} 이며 now={now} prevNow ={prevNow} nextJungsan={nextJungsan}")
            if myInterestBalance > 0:                                
                self.autoMedo()
                time.sleep(10) #10초간 슬립                
                time.sleep(1) # 매수도후 잔고 회복 시간을 줌 
            mBool_DangilMesu = False
            prevNow = now            
            self.reflesh()            
            self.botSendmsg('분봉 정산 실행 후 타겟 재 계산')
        return    

    def autoTrading(self):
        global mBool_DangilMesu, mMinBuyAmount, mBool_autoWarning, mCurNoTrade, mCurNoTrade, mPreNoTrade
        try:
            if self.chkLoginFirst() == False :
                mCurNoTrade = 1
                if mCurNoTrade != mPreNoTrade :
                    self.botSendmsg(f"현재가격 {mCurrentInterPrice } 타겟가격 {mTargetPrice } 로그인 안되어 있음")
                    mPreNoTrade = mCurNoTrade
                return            
            # 매도 싯점은 정산 주기에 의존 함. 무조건 거래라는 뜻            
            if self.comboBox_jugi.currentText() == 'day':
                self.dayJungsan(self.comboBox_jugi.currentText())
            else :
                self.minJungsan(self.comboBox_jugi.currentText())
            if mKrwBalance4Buy < mMinBuyAmount and mBool_autoWarning == False:
                mCurNoTrade = 2
                if mCurNoTrade != mPreNoTrade :
                    self.botSendmsg(f"매수 예정 금액= [{format(mKrwBalance4Buy,',')}] 이 최소 [{format(mMinBuyAmount,',')}]보다 작음.")
                    mPreNoTrade = mCurNoTrade
                    self.tujaYulChanged()
                self.reflesh()
                mBool_autoWarning = True
                return
            if mKrwBalance4Buy < mMinBuyAmount :
                mCurNoTrade = 2
                if mCurNoTrade != mPreNoTrade :
                    self.botSendmsg(f"현재가격 {mCurrentInterPrice } 타겟가격 {mTargetPrice } 최소거래 금액이 없음")
                    mPreNoTrade = mCurNoTrade                
                    self.tujaYulChanged()
                return

            # 매수는 공통 사항임 아래 조건에 부합 할때            
            if self.cBox_trade.isChecked() is False: #자동매매 아니면 
                mCurNoTrade = 4
                if mCurNoTrade != mPreNoTrade :
                    self.botSendmsg(f"현재가격 {mCurrentInterPrice } 타겟가격 {mTargetPrice } 자동매매 상태 아님")
                    mPreNoTrade = mCurNoTrade                
                return            
            if mCurrentInterPrice < mTargetPrice: # 타겟가격보다 낮으면
                mCurNoTrade = 5
                if mCurNoTrade != mPreNoTrade :
                    self.botSendmsg(f"현재가격 {mCurrentInterPrice } 타겟가격 {mTargetPrice } 타겟가격낮음")
                    mPreNoTrade = mCurNoTrade                
                return            
            if self.cBox_banbok_trade.isChecked() is False and mBool_DangilMesu == True: # 당일매수한적 있는데 반복 불가이면
                mCurNoTrade = 6
                if mCurNoTrade != mPreNoTrade :
                    self.botSendmsg(f"현재가격 {mCurrentInterPrice } 타겟가격 {mTargetPrice } 당일매수 있고 반복 불가")
                    mPreNoTrade = mCurNoTrade
                return            
            if self.cBox_banbok_trade.isChecked() is True or mBool_DangilMesu == False: #반복매수허가 이거나 오늘 매수가 없을때                             
                mCurNoTrade = 8
                if mCurNoTrade != mPreNoTrade :
                    self.botSendmsg(f"Auto 매수 시도 금액=[{format(mKrwBalance4Buy,',')}] 코인 { myInterest } 매입가 [{format(mCurrentInterPrice,',')}]")
                    mPreNoTrade = mCurNoTrade                
                self.autoMesu()
                mBool_DangilMesu = True
                time.sleep(5)                
        except Exception as e:
            self.botSendmsg(e)
            self.botSendmsg("autoTrading 에러 발생")            
        return
    def reflesh(self):
        if self.chkLoginFirst() == False :
            return  
        self.cal_target()
        self.dspCurrent()
    
# 이 코드는 Python에서 실행 중인 스크립트가 컴파일된 환경에서 실행되는지 또는 스크립트 파일로 실행되는지를 
# 확인하는 것입니다. 컴파일된 환경에서 실행되는 경우 해당 실행 파일이 있는 디렉토리를 얻고, 
# 그렇지 않은 경우 스크립트 파일이 있는 디렉토리를 얻습니다.
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

# # 로그 생성
# logger = logging.getLogger()
# # 로그의 출력 기준 설정
# logger.setLevel(logging.INFO)
# # log 출력 형식
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # log 출력
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
# logger.addHandler(stream_handler)

# # log를 파일에 출력
# file_handler = logging.FileHandler(f'{application_path}/my.log')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
# myThread = threading.Thread(target=everyTime, args=(1,))
app = QApplication(sys.argv)
app.setStyle('fusion')

# 전체 위젯의 배경색상과 텍스트 색상을 설정
# palette = QPalette()
# palette.setColor(QPalette.Window, QColor(30, 30, 30))
# palette.setColor(QPalette.WindowText, QColor(200, 200, 200))
# app.setPalette(palette)

window = MyWindow()

# myThread.start()
window.show()
app.exec_()