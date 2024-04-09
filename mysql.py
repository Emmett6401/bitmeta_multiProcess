import sys
import pymysql.cursors
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class ConnectionInputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("이 다이얼로그가 보일때는 서버에 이상이 생겼음")  # 다이얼로그 제목 설정

        self.host_input = QLineEdit()
        self.user_input = QLineEdit()
        self.passwd_input = QLineEdit()
        self.db_input = QLineEdit()
        self.port_input = QLineEdit()

        self.host_input.setPlaceholderText("bitnmeta2.synology.me")  # 디폴트 값 대신 placeholder 텍스트 사용
        self.user_input.setPlaceholderText("iyrc")
        self.passwd_input.setPlaceholderText("Dodan1004!")
        self.db_input.setPlaceholderText("mydb")
        self.port_input.setPlaceholderText("3306")

        layout = QFormLayout()
        layout.addRow("Host:", self.host_input)
        layout.addRow("User:", self.user_input)
        layout.addRow("Password:", self.passwd_input)
        layout.addRow("Database:", self.db_input)
        layout.addRow("Port:", self.port_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)
        self.setLayout(layout)

    def accept(self):
        # 각 입력값을 검증하고 비어 있으면 디폴트 값을 설정
        if not self.host_input.text():
            self.host_input.setText("localhost")
        if not self.user_input.text():
            self.user_input.setText("username")
        if not self.passwd_input.text():
            self.passwd_input.setText("password")
        if not self.db_input.text():
            self.db_input.setText("abot")
        if not self.port_input.text():
            self.port_input.setText("3307")      
        super().accept()

class mySqlDB():    
    def __init__(self):
        pymysql.version_info = (1, 4, 2, "final", 0)
        pymysql.install_as_MySQLdb()        
        super().__init__()
        try:
            self.connection = pymysql.connect(
                host='bitnmeta2.synology.me',
                user='iyrc', 
                passwd='Dodan1004!',              
                db='abot',
                charset='utf8',    
                port = 3307,
                cursorclass=pymysql.cursors.DictCursor)        
        except Exception as e :
            print(f"An error occurred: {e}")
            self.show_dialog()

    def show_dialog(self):
        app = QApplication(sys.argv)
        dialog = ConnectionInputDialog()
        if dialog.exec_():
            host = dialog.host_input.text()
            user = dialog.user_input.text()
            passwd = dialog.passwd_input.text()
            db = dialog.db_input.text()
            port = int(dialog.port_input.text())

            self.connection = pymysql.connect(
                host=host,
                user=user,
                passwd=passwd,
                db=db,
                charset='utf8',
                port=port,
                cursorclass=pymysql.cursors.DictCursor)

            print("Connection successful")
        else:
            print("User canceled")       

    def insert2(self, id,password):
        
        with self.connection:
            with self.connection.cursor() as cursor:                
                sql = "INSERT INTO user2 (id, pw) VALUES (%s, %s)"
                cursor.execute(sql, (id,password))
                self.connection.commit()                

    def insert(self,id,password,username,phone,level,signdate,upbit_ip,upbit_api,upbit_secret,\
        coinone_api,coinone_secret, teleAPInum, teleAPIkey,myinterest1,myinterest2,myinterest3):
        
        with self.connection:
            with self.connection.cursor() as cursor:
                
                sql = "INSERT INTO user (id, password, username, phone,level,\
                     signdate, upbitip, upbitapi,upbitsecret,coinoneapi,coinonesecret,\
                        teleapinum,teleapikey,myinterest1,myinterest2,myinterest3) \
                            VALUES (%s, %s, %s, %s,  %s, %s, %s, %s,  %s, %s, %s,%s,  %s, %s, %s, %s)"
                cursor.execute(sql, (id,password,username,phone,level,signdate,\
                    upbit_ip,upbit_api,upbit_secret,coinone_api,coinone_secret,\
                    teleAPInum, teleAPIkey,myinterest1,myinterest2,myinterest3))
                self.connection.commit()                   

    def update(self,id,sel1):
        
        try:
            with self.connection:
                with self.connection.cursor() as cursor:                
                    sql = "UPDATE user SET myinterest1 = %s WHERE id = %s" 
                    cursor.execute(sql, (sel1,id))
                    self.connection.commit()
        except Exception as e:
            print(e)        
            
        
    def search(self,key):
        
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM user WHERE id LIKE %s OR phone LIKE %s OR email LIKE %s"
            key = '%'+key+'%'
            cursor.execute(sql, (key,key,key))
            result = cursor.fetchone()
            return result
    def chkLogin(self,id,pw):
        
        with self.connection.cursor() as cursor:            
            try:
                sql = "SELECT * FROM `user` WHERE `id` = %s AND `password` = %s"
                cursor.execute(sql, (id,pw))
                result = cursor.fetchone()                                
            except Exception as e:                         
                print(e)
                return None
            return result
    def chkID(self,id):
        
        with self.connection.cursor() as cursor:            
            sql = "SELECT * FROM `user` WHERE `id` = %s"
            cursor.execute(sql, (id))
            result = cursor.fetchone()
            return result
    def delete(self,key):
        
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "DELETE FROM `user` WHERE `id` = %s"
            cursor.execute(sql,key)
            self.connection.commit()
            

            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = mySqlDB()       
    app.exec_()
    