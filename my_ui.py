# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './res/window8.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 914)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(80.0)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pBar = QtWidgets.QProgressBar(self.centralwidget)
        self.pBar.setGeometry(QtCore.QRect(420, 1, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pBar.setFont(font)
        self.pBar.setProperty("value", 0)
        self.pBar.setTextVisible(False)
        self.pBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.pBar.setObjectName("pBar")
        self.lbl_matic_led = QtWidgets.QLabel(self.centralwidget)
        self.lbl_matic_led.setGeometry(QtCore.QRect(243, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_matic_led.setFont(font)
        self.lbl_matic_led.setText("")
        self.lbl_matic_led.setScaledContents(True)
        self.lbl_matic_led.setObjectName("lbl_matic_led")
        self.lineEdit_yTop = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_yTop.setEnabled(False)
        self.lineEdit_yTop.setGeometry(QtCore.QRect(290, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_yTop.setFont(font)
        self.lineEdit_yTop.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit_yTop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_yTop.setObjectName("lineEdit_yTop")
        self.lineEdit_yBottom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_yBottom.setEnabled(False)
        self.lineEdit_yBottom.setGeometry(QtCore.QRect(120, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_yBottom.setFont(font)
        self.lineEdit_yBottom.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_yBottom.setObjectName("lineEdit_yBottom")
        self.lineEdit_targetPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_targetPrice.setEnabled(False)
        self.lineEdit_targetPrice.setGeometry(QtCore.QRect(290, 130, 161, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_targetPrice.setFont(font)
        self.lineEdit_targetPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_targetPrice.setObjectName("lineEdit_targetPrice")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 274, 161, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:blue;")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_boyuMATIC = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_boyuMATIC.setEnabled(False)
        self.lineEdit_boyuMATIC.setGeometry(QtCore.QRect(120, 306, 161, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_boyuMATIC.setFont(font)
        self.lineEdit_boyuMATIC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_boyuMATIC.setObjectName("lineEdit_boyuMATIC")
        self.lineEdit_boyuKRW = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_boyuKRW.setEnabled(False)
        self.lineEdit_boyuKRW.setGeometry(QtCore.QRect(120, 210, 331, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_boyuKRW.setFont(font)
        self.lineEdit_boyuKRW.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_boyuKRW.setObjectName("lineEdit_boyuKRW")
        self.lineEdit_tujaYul = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tujaYul.setGeometry(QtCore.QRect(210, 240, 71, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_tujaYul.setFont(font)
        self.lineEdit_tujaYul.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_tujaYul.setObjectName("lineEdit_tujaYul")
        self.lineEdit_byunYul = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_byunYul.setGeometry(QtCore.QRect(120, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_byunYul.setFont(font)
        self.lineEdit_byunYul.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_byunYul.setObjectName("lineEdit_byunYul")
        self.lineEdit_upbitPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_upbitPrice.setEnabled(False)
        self.lineEdit_upbitPrice.setGeometry(QtCore.QRect(290, 100, 161, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_upbitPrice.setFont(font)
        self.lineEdit_upbitPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_upbitPrice.setObjectName("lineEdit_upbitPrice")
        self.lbl_upbitInterest = QtWidgets.QLabel(self.centralwidget)
        self.lbl_upbitInterest.setGeometry(QtCore.QRect(10, 37, 101, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_upbitInterest.setFont(font)
        self.lbl_upbitInterest.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_upbitInterest.setObjectName("lbl_upbitInterest")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(450, 73, 51, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(30, 73, 81, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(133, 136, 151, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:red;")
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(-40, 215, 151, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:red;")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(10, 134, 101, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:blue;")
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 247, 161, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:blue;")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.lineEdit_gaingYul = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gaingYul.setGeometry(QtCore.QRect(210, 270, 71, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_gaingYul.setFont(font)
        self.lineEdit_gaingYul.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_gaingYul.setObjectName("lineEdit_gaingYul")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(203, 108, 81, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:red;")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.lineEdit_avgMesu = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_avgMesu.setEnabled(False)
        self.lineEdit_avgMesu.setGeometry(QtCore.QRect(120, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_avgMesu.setFont(font)
        self.lineEdit_avgMesu.setText("")
        self.lineEdit_avgMesu.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_avgMesu.setObjectName("lineEdit_avgMesu")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(-40, 186, 151, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.lineEdit_lastMesu = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lastMesu.setEnabled(False)
        self.lineEdit_lastMesu.setGeometry(QtCore.QRect(290, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_lastMesu.setFont(font)
        self.lineEdit_lastMesu.setText("")
        self.lineEdit_lastMesu.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_lastMesu.setObjectName("lineEdit_lastMesu")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(453, 184, 81, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.lineEdit_tujaKum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tujaKum.setEnabled(False)
        self.lineEdit_tujaKum.setGeometry(QtCore.QRect(290, 240, 161, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_tujaKum.setFont(font)
        self.lineEdit_tujaKum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_tujaKum.setObjectName("lineEdit_tujaKum")
        self.lineEdit_gaingKum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gaingKum.setEnabled(False)
        self.lineEdit_gaingKum.setGeometry(QtCore.QRect(290, 270, 161, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_gaingKum.setFont(font)
        self.lineEdit_gaingKum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_gaingKum.setObjectName("lineEdit_gaingKum")
        self.lineEdit_idInfo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_idInfo.setEnabled(False)
        self.lineEdit_idInfo.setGeometry(QtCore.QRect(0, 0, 221, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_idInfo.setFont(font)
        self.lineEdit_idInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_idInfo.setObjectName("lineEdit_idInfo")
        self.lineEdit_boyuMATIC_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_boyuMATIC_2.setEnabled(False)
        self.lineEdit_boyuMATIC_2.setGeometry(QtCore.QRect(290, 306, 161, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.lineEdit_boyuMATIC_2.setFont(font)
        self.lineEdit_boyuMATIC_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_boyuMATIC_2.setObjectName("lineEdit_boyuMATIC_2")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(232, 3, 101, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:blue;")
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.comboBox_jugi = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_jugi.setGeometry(QtCore.QRect(340, 0, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_jugi.sizePolicy().hasHeightForWidth())
        self.comboBox_jugi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.comboBox_jugi.setFont(font)
        self.comboBox_jugi.setObjectName("comboBox_jugi")
        self.comboBox_jugi.addItem("")
        self.comboBox_jugi.addItem("")
        self.comboBox_jugi.addItem("")
        self.comboBox_jugi.addItem("")
        self.comboBox_jugi.addItem("")
        self.comboBox_jugi.addItem("")
        self.comboBox_jugi.addItem("")
        self.comboBox_jugi.addItem("")
        self.comboBox_jugi.addItem("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 360, 521, 248))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cBox_immediatery_trade = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.cBox_immediatery_trade.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/juksi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cBox_immediatery_trade.setIcon(icon1)
        self.cBox_immediatery_trade.setIconSize(QtCore.QSize(32, 32))
        self.cBox_immediatery_trade.setObjectName("cBox_immediatery_trade")
        self.verticalLayout.addWidget(self.cBox_immediatery_trade)
        self.cBox_banbok_trade = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.cBox_banbok_trade.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/banbok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cBox_banbok_trade.setIcon(icon2)
        self.cBox_banbok_trade.setIconSize(QtCore.QSize(32, 32))
        self.cBox_banbok_trade.setObjectName("cBox_banbok_trade")
        self.verticalLayout.addWidget(self.cBox_banbok_trade)
        self.cBox_zonbu_mesuNot = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.cBox_zonbu_mesuNot.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/jonbu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cBox_zonbu_mesuNot.setIcon(icon3)
        self.cBox_zonbu_mesuNot.setIconSize(QtCore.QSize(32, 32))
        self.cBox_zonbu_mesuNot.setObjectName("cBox_zonbu_mesuNot")
        self.verticalLayout.addWidget(self.cBox_zonbu_mesuNot)
        self.cBox_trade_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.cBox_trade_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.cBox_trade_2.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/0859.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cBox_trade_2.setIcon(icon4)
        self.cBox_trade_2.setIconSize(QtCore.QSize(32, 32))
        self.cBox_trade_2.setChecked(True)
        self.cBox_trade_2.setObjectName("cBox_trade_2")
        self.verticalLayout.addWidget(self.cBox_trade_2)
        self.btn_mesu = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.btn_mesu.setFont(font)
        self.btn_mesu.setObjectName("btn_mesu")
        self.verticalLayout.addWidget(self.btn_mesu)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cBox_trade = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.cBox_trade.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/byundong.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cBox_trade.setIcon(icon5)
        self.cBox_trade.setIconSize(QtCore.QSize(32, 32))
        self.cBox_trade.setObjectName("cBox_trade")
        self.verticalLayout_2.addWidget(self.cBox_trade)
        self.cBox_trade_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.cBox_trade_4.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.cBox_trade_4.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/idong.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cBox_trade_4.setIcon(icon6)
        self.cBox_trade_4.setIconSize(QtCore.QSize(32, 32))
        self.cBox_trade_4.setObjectName("cBox_trade_4")
        self.verticalLayout_2.addWidget(self.cBox_trade_4)
        self.cBox_trade_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.cBox_trade_3.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.cBox_trade_3.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/sunmedo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cBox_trade_3.setIcon(icon7)
        self.cBox_trade_3.setIconSize(QtCore.QSize(32, 32))
        self.cBox_trade_3.setObjectName("cBox_trade_3")
        self.verticalLayout_2.addWidget(self.cBox_trade_3)
        self.cBox_zonbu = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.cBox_zonbu.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/medonot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cBox_zonbu.setIcon(icon8)
        self.cBox_zonbu.setIconSize(QtCore.QSize(32, 32))
        self.cBox_zonbu.setObjectName("cBox_zonbu")
        self.verticalLayout_2.addWidget(self.cBox_zonbu)
        self.btn_medo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.btn_medo.setFont(font)
        self.btn_medo.setObjectName("btn_medo")
        self.verticalLayout_2.addWidget(self.btn_medo)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 610, 521, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_botSend = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(7)
        self.textEdit_botSend.setFont(font)
        self.textEdit_botSend.setObjectName("textEdit_botSend")
        self.verticalLayout_3.addWidget(self.textEdit_botSend)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(450, 310, 61, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(460, 240, 51, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(460, 270, 51, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(460, 212, 51, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(0, 310, 111, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menuVinance = QtWidgets.QMenu(self.menubar)
        self.menuVinance.setEnabled(False)
        self.menuVinance.setObjectName("menuVinance")
        self.menuKOSPI = QtWidgets.QMenu(self.menubar)
        self.menuKOSPI.setEnabled(False)
        self.menuKOSPI.setObjectName("menuKOSPI")
        self.menuNasDaq = QtWidgets.QMenu(self.menubar)
        self.menuNasDaq.setEnabled(False)
        self.menuNasDaq.setObjectName("menuNasDaq")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setEnabled(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/gLed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogin.setIcon(icon9)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.actionLogin.setFont(font)
        self.actionLogin.setObjectName("actionLogin")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setEnabled(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/rLed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon10)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.actionStop.setFont(font)
        self.actionStop.setObjectName("actionStop")
        self.actionInquiry = QtWidgets.QAction(MainWindow)
        self.actionInquiry.setEnabled(False)
        self.actionInquiry.setObjectName("actionInquiry")
        self.actionRegister = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRegister.setIcon(icon11)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.actionRegister.setFont(font)
        self.actionRegister.setObjectName("actionRegister")
        self.actionqusehdtjdehfvk = QtWidgets.QAction(MainWindow)
        self.actionqusehdtjdehfvk.setCheckable(True)
        self.actionqusehdtjdehfvk.setChecked(True)
        self.actionqusehdtjdehfvk.setObjectName("actionqusehdtjdehfvk")
        self.actionBTasking = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBTasking.setIcon(icon12)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.actionBTasking.setFont(font)
        self.actionBTasking.setObjectName("actionBTasking")
        self.actioncheksxkaoao = QtWidgets.QAction(MainWindow)
        self.actioncheksxkaoao.setCheckable(True)
        self.actioncheksxkaoao.setChecked(True)
        self.actioncheksxkaoao.setObjectName("actioncheksxkaoao")
        self.actionaBot = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("C:/Users/Na_neem/.designer/backup/bitmetaSmall3.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionaBot.setIcon(icon13)
        self.actionaBot.setObjectName("actionaBot")
        self.menu_2.addAction(self.actionLogin)
        self.menu_2.addAction(self.actionStop)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionBTasking)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionRegister)
        self.menu.addAction(self.actionqusehdtjdehfvk)
        self.menu.addAction(self.actioncheksxkaoao)
        self.menuAbout.addAction(self.actionaBot)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuVinance.menuAction())
        self.menubar.addAction(self.menuKOSPI.menuAction())
        self.menubar.addAction(self.menuNasDaq.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "24시간 잠들지 않는 bitMeta23.10.27"))
        self.label_10.setText(_translate("MainWindow", "초단타수익(%)(원)"))
        self.lineEdit_tujaYul.setToolTip(_translate("MainWindow", "내가 가진 현금중 얼마를 투자 할 것인가를 결정 합니다."))
        self.lineEdit_tujaYul.setText(_translate("MainWindow", "99.0"))
        self.lineEdit_byunYul.setToolTip(_translate("MainWindow", "적용 변동률이 낮을 수록 공격적인 투자를 하게 됩니다. 50%를 권장합니다."))
        self.lineEdit_byunYul.setText(_translate("MainWindow", "50.0"))
        self.lbl_upbitInterest.setText(_translate("MainWindow", "거래종목"))
        self.label_16.setText(_translate("MainWindow", "최고가"))
        self.label_17.setText(_translate("MainWindow", "전일최저가"))
        self.label_18.setText(_translate("MainWindow", "매수Target가"))
        self.label_19.setText(_translate("MainWindow", "보유 KRW"))
        self.label_22.setText(_translate("MainWindow", "적용변동률(%)"))
        self.label_11.setText(_translate("MainWindow", "KRW투자비율(%)"))
        self.lineEdit_gaingYul.setToolTip(_translate("MainWindow", "무엇보다 우선적으로 적용되는 옵션으로 평균 매수가의 해당 %보다 높을때 단타 매매를 합니다."))
        self.lineEdit_gaingYul.setText(_translate("MainWindow", "3.0"))
        self.label_20.setText(_translate("MainWindow", "현재가"))
        self.label_12.setText(_translate("MainWindow", "평균매수가"))
        self.label_13.setText(_translate("MainWindow", "직전매수가"))
        self.lineEdit_idInfo.setText(_translate("MainWindow", "미접속"))
        self.label_23.setText(_translate("MainWindow", "정산주기(캔들)"))
        self.comboBox_jugi.setToolTip(_translate("MainWindow", "정산 주기를 조절 할 수 있습니다."))
        self.comboBox_jugi.setItemText(0, _translate("MainWindow", "day"))
        self.comboBox_jugi.setItemText(1, _translate("MainWindow", "minute1"))
        self.comboBox_jugi.setItemText(2, _translate("MainWindow", "minute3"))
        self.comboBox_jugi.setItemText(3, _translate("MainWindow", "minute5"))
        self.comboBox_jugi.setItemText(4, _translate("MainWindow", "minute10"))
        self.comboBox_jugi.setItemText(5, _translate("MainWindow", "minute15"))
        self.comboBox_jugi.setItemText(6, _translate("MainWindow", "munite30"))
        self.comboBox_jugi.setItemText(7, _translate("MainWindow", "minute60"))
        self.comboBox_jugi.setItemText(8, _translate("MainWindow", "minute240"))
        self.cBox_immediatery_trade.setToolTip(_translate("MainWindow", "즉시 적용이란 변동성 돌파 자동 거래를 허가 했을때 이미 매수 타갯 가격에 도달 한 경우에  즉시 매수가 이루어 집니다. "))
        self.cBox_immediatery_trade.setText(_translate("MainWindow", "즉시 매입 적용"))
        self.cBox_banbok_trade.setToolTip(_translate("MainWindow", "반복매입이란 1회 최초 타겟가격에 매입을 한후 가격이 하락후 재 상승하여 타겟가에 도달 했을때 추가 매입을 시도 하는 옵션입니다."))
        self.cBox_banbok_trade.setText(_translate("MainWindow", "반복 매입 적용"))
        self.cBox_zonbu_mesuNot.setToolTip(_translate("MainWindow", "존버 매입 금지는 변동성 돌파 매입을 금지 합니다."))
        self.cBox_zonbu_mesuNot.setText(_translate("MainWindow", "존버 자동 매입 금지"))
        self.cBox_trade_2.setToolTip(_translate("MainWindow", "08:59에 피크 함정을 돌파 합니다.  거래가 중지 됩니다. "))
        self.cBox_trade_2.setText(_translate("MainWindow", "08:59 피크 함정 매입금지"))
        self.btn_mesu.setText(_translate("MainWindow", "강제매수"))
        self.cBox_trade.setToolTip(_translate("MainWindow", "변동성 돌파 자동 거래를 허가 하는것이 거래의 시작입니다."))
        self.cBox_trade.setText(_translate("MainWindow", "변동성돌파자동거래"))
        self.cBox_trade_4.setToolTip(_translate("MainWindow", "변동성 돌파 자동 거래를 허가 하는것이 거래의 시작입니다."))
        self.cBox_trade_4.setText(_translate("MainWindow", "이동 평균 차익 거래"))
        self.cBox_trade_3.setToolTip(_translate("MainWindow", "변동성 돌파 자동 거래를 허가 하는것이 거래의 시작입니다."))
        self.cBox_trade_3.setText(_translate("MainWindow", "08:59 피크 선매도"))
        self.cBox_zonbu.setToolTip(_translate("MainWindow", "초단타 수익률이 실현 될 때까지 버티기"))
        self.cBox_zonbu.setText(_translate("MainWindow", "존버 자동 매도 금지"))
        self.btn_medo.setText(_translate("MainWindow", "강제매도"))
        self.label_21.setText(_translate("MainWindow", "원"))
        self.label_24.setText(_translate("MainWindow", "원"))
        self.label_25.setText(_translate("MainWindow", "원"))
        self.label_26.setText(_translate("MainWindow", "원"))
        self.label_14.setText(_translate("MainWindow", "보유코인"))
        self.menu_2.setTitle(_translate("MainWindow", "업비트"))
        self.menuVinance.setTitle(_translate("MainWindow", "Vinance"))
        self.menuKOSPI.setTitle(_translate("MainWindow", "KOSPI"))
        self.menuNasDaq.setTitle(_translate("MainWindow", "NasDaq"))
        self.menu.setTitle(_translate("MainWindow", "알고리즘선택"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionLogin.setText(_translate("MainWindow", "로그인"))
        self.actionStop.setText(_translate("MainWindow", "로그아웃"))
        self.actionInquiry.setText(_translate("MainWindow", "Inquiry"))
        self.actionRegister.setText(_translate("MainWindow", "회원등록"))
        self.actionqusehdtjdehfvk.setText(_translate("MainWindow", "변동성돌파 "))
        self.actionBTasking.setText(_translate("MainWindow", "코인변경"))
        self.actioncheksxkaoao.setText(_translate("MainWindow", "분봉초단타매매"))
        self.actionaBot.setText(_translate("MainWindow", "aBot"))
