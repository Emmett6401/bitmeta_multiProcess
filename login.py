import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from mysql import *
from PyQt5 import uic
from PyQt5.QtCore import QSettings
import base64  # 이 모듈은 간단한 암호화에 사용됩니다.

form_login = uic.loadUiType("./res/win_login.ui")[0]
class bitmetaLogin(QDialog, form_login):  
    result = []
    def __init__(self,parent):        
        super().__init__() #속성및 메소드를 모두 가져옴                
        self.setupUi(self)
        self.btn_login.clicked.connect(self.btn_login_clicked)            

         # 시작 시 자동 로그인 시도 및 체크박스 상태 복원
        self.restore_settings()
  
           
    def btn_login_clicked(self):
        global result        
        myDB = mySqlDB()          
        result = myDB.chkLogin(self.line_username.text(), self.line_password.text())
        
        if result == None:                        
            QMessageBox.warning(self,'회원정보','ID와 비번을 확인하세요')            
        elif result['id'] == self.line_username.text() and \
             result['password'] == self.line_password.text() :            
            self.save_settings()
            self.accept()
        else:
            self.reject()
    def restore_settings(self):
        settings = QSettings("bitnmeta", "Login")
        autologin = settings.value("autologin", False, type=bool)
        
        if autologin:
            username = base64.b64decode(settings.value("username", "").encode()).decode()
            password = base64.b64decode(settings.value("password", "").encode()).decode()
            
            if username and password:
                self.line_username.setText(username)
                self.line_password.setText(password)
                self.chk_autologin.setChecked(True)
                self.btn_login_clicked()  # 저장된 정보로 로그인 시도
        else:
            username = base64.b64decode(settings.value("username", "").encode()).decode()
            if username:
                self.line_username.setText(username)

                        
    def save_settings(self):
        settings = QSettings("bitnmeta", "Login")
        # 간단한 암호화를 사용하여 정보 저장
        settings.setValue("username", base64.b64encode(self.line_username.text().encode()).decode())
        settings.setValue("password", base64.b64encode(self.line_password.text().encode()).decode())
        settings.setValue("autologin", self.chk_autologin.isChecked())




    @staticmethod
    def launch(parent):
        dlg = bitmetaLogin(parent)
        r = dlg.exec()
        if r : 
            return result
        return None
    def showModalQ(self):
            return super().exec_()
if __name__ == "__main__":    
    app = QApplication(sys.argv)
    dlg = bitmetaLogin(None)      
    dlg.show()
    app.exec_()