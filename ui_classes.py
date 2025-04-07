from PyQt5 import QtCore, QtGui, QtWidgets

# LANDING PAGE-------------------------------------------------------------------------------------------------------
class Ui_JJ_LANDING(object):  # THIS PART CORRESPONDS TO class LandingPage(QMainWindow) in main_app.py
    def setupUi(self, JJ_LANDING):
        JJ_LANDING.setObjectName("JJ_LANDING")
        JJ_LANDING.resize(1280, 849)
        self.centralwidget = QtWidgets.QWidget(JJ_LANDING)
        self.centralwidget.setObjectName("centralwidget")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(0, 0, 1281, 831))
        self.BG.setText("")
        self.BG.setPixmap(QtGui.QPixmap(":/images/BACKGROUND.png"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")
        self.LOGO = QtWidgets.QLabel(self.centralwidget)
        self.LOGO.setGeometry(QtCore.QRect(500, 100, 341, 231))
        self.LOGO.setText("")
        self.LOGO.setPixmap(QtGui.QPixmap(":/images/JJLOGO.png"))
        self.LOGO.setScaledContents(True)
        self.LOGO.setObjectName("LOGO")
        self.JJ = QtWidgets.QLabel(self.centralwidget)
        self.JJ.setGeometry(QtCore.QRect(280, 360, 921, 81))
        font = QtGui.QFont()
        font.setFamily("Rubik Mono One")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.JJ.setFont(font)
        self.JJ.setStyleSheet("color: #ebe0cc;\n"
"font-size: 100px;\n"
"font-family: \"Rubik Mono One\", sans-serif;\n"
"background: transparent;")
        self.JJ.setScaledContents(True)
        self.JJ.setObjectName("JJ")
        self.ELEVATE = QtWidgets.QLabel(self.centralwidget)
        self.ELEVATE.setGeometry(QtCore.QRect(580, 350, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ELEVATE.setFont(font)
        self.ELEVATE.setStyleSheet("color: #d75413;\n"
"font-size: 100px;\n"
"font-family: \"Arial Black\", Arial, sans-serif; \n"
"background: transparent;")
        self.ELEVATE.setScaledContents(True)
        self.ELEVATE.setObjectName("ELEVATE")
        self.elv_ur_space = QtWidgets.QLabel(self.centralwidget)
        self.elv_ur_space.setGeometry(QtCore.QRect(280, 440, 711, 71))
        font = QtGui.QFont()
        font.setFamily("Sora Semibold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.elv_ur_space.setFont(font)
        self.elv_ur_space.setStyleSheet("color: #f6f3ee;\n"
"font-size: 35px;\n"
"font-family: \"Sora Semibold\", sans-serif; \n"
"background: transparent;")
        self.elv_ur_space.setScaledContents(True)
        self.elv_ur_space.setObjectName("elv_ur_space")
        self.Supply_Inst_Rep = QtWidgets.QLabel(self.centralwidget)
        self.Supply_Inst_Rep.setGeometry(QtCore.QRect(390, 550, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Extrabold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.Supply_Inst_Rep.setFont(font)
        self.Supply_Inst_Rep.setStyleSheet("color: #ebe0cc;\n"
"font-size: 20px;\n"
"font-family: \"Poppins Extrabold\", sans-serif;\n"
"background: transparent;")
        self.Supply_Inst_Rep.setScaledContents(True)
        self.Supply_Inst_Rep.setObjectName("Supply_Inst_Rep")
        self.pushButton_contOwner = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_contOwner.setGeometry(QtCore.QRect(70, 650, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.pushButton_contOwner.setFont(font)
        self.pushButton_contOwner.setStyleSheet("background-color: #f6f3ee;\n"
"border-radius: 15px; \n"
"padding: 4px;\n"
"border: none;\n"
"color: #374550;\n"
"font-size: 18px;\n"
"font-family: \"MS Shell Dlg 2\", sans-serif;")
        self.pushButton_contOwner.setObjectName("pushButton_contOwner")
        self.pushButton_contCashier = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_contCashier.setGeometry(QtCore.QRect(70, 700, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.pushButton_contCashier.setFont(font)
        self.pushButton_contCashier.setStyleSheet("background-color: #f6f3ee;\n"
"border-radius: 15px; \n"
"padding: 4px;\n"
"border: none;\n"
"color: #374550;\n"
"font-size: 18px;\n"
"font-family: \"MS Shell Dlg 2\", sans-serif;")
        self.pushButton_contCashier.setObjectName("pushButton_contCashier")
        JJ_LANDING.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JJ_LANDING)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        JJ_LANDING.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JJ_LANDING)
        self.statusbar.setObjectName("statusbar")
        JJ_LANDING.setStatusBar(self.statusbar)

        self.retranslateUi(JJ_LANDING)
        QtCore.QMetaObject.connectSlotsByName(JJ_LANDING)

    def retranslateUi(self, JJ_LANDING):
        _translate = QtCore.QCoreApplication.translate
        JJ_LANDING.setWindowTitle(_translate("JJ_LANDING", "MainWindow"))
        self.JJ.setText(_translate("JJ_LANDING", "J&J\n"
""))
        self.ELEVATE.setText(_translate("JJ_LANDING", "Elevate\n"
""))
        self.elv_ur_space.setText(_translate("JJ_LANDING", "Elevate Your Space, One Roof at a Time"))
        self.Supply_Inst_Rep.setText(_translate("JJ_LANDING", "Supply                               Install                               Repair    "))
        self.pushButton_contOwner.setText(_translate("JJ_LANDING", "Continue as Owner"))
        self.pushButton_contCashier.setText(_translate("JJ_LANDING", "Continue as Cashier"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JJ_LANDING = QtWidgets.QMainWindow()
    ui = Ui_JJ_LANDING()
    ui.setupUi(JJ_LANDING)
    JJ_LANDING.show()
    sys.exit(app.exec_())

# OWNER LOGIN--------------------------------------------------------------------------------------------------------
class Ui_OwnrLOGIN(object):  # THIS PART CORRESPONDS TO class OwnerLoginPage(QMainWindow) in main_app.py
    def setupUi(self, OwnrLOGIN):
        OwnrLOGIN.setObjectName("OwnrLOGIN")
        OwnrLOGIN.resize(1280, 849)
        self.centralwidget = QtWidgets.QWidget(OwnrLOGIN)
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")
        self.PIC = QtWidgets.QLabel(self.centralwidget)
        self.PIC.setGeometry(QtCore.QRect(0, 0, 1291, 791))
        self.PIC.setMinimumSize(QtCore.QSize(100, 40))
        self.PIC.setText("")
        self.PIC.setPixmap(QtGui.QPixmap(":/images/PIC_log_sign_in.png"))
        self.PIC.setScaledContents(True)
        self.PIC.setObjectName("PIC")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 120, 411, 251))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/JJLOGO.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(880, 70, 181, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #022162;\n"
"font-size: 58px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 200, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #022162;\n"
"font-size: 24px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 340, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #022162;\n"
"font-size: 24px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(860, 610, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #022162;")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.ownr_login_usrname = QtWidgets.QLineEdit(self.centralwidget)
        self.ownr_login_usrname.setGeometry(QtCore.QRect(710, 250, 521, 51))
        self.ownr_login_usrname.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.ownr_login_usrname.setFont(font)
        self.ownr_login_usrname.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.ownr_login_usrname.setObjectName("ownr_login_usrname")
        self.ownr_login_password = QtWidgets.QLineEdit(self.centralwidget)
        self.ownr_login_password.setGeometry(QtCore.QRect(710, 400, 521, 51))
        self.ownr_login_password.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.ownr_login_password.setFont(font)
        self.ownr_login_password.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.ownr_login_password.setObjectName("ownr_login_password")
        self.checkBox_rememberme = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rememberme.setGeometry(QtCore.QRect(730, 470, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.checkBox_rememberme.setFont(font)
        self.checkBox_rememberme.setStyleSheet("color: #022162;\n"
"font-size: 17px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.checkBox_rememberme.setObjectName("checkBox_rememberme")
        self.pushButton_LOGIN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LOGIN.setGeometry(QtCore.QRect(700, 550, 531, 51))
        self.pushButton_LOGIN.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_LOGIN.setFont(font)
        self.pushButton_LOGIN.setStyleSheet("border: 2px solid #374550; \n"
"border-radius: 25px; \n"
"padding: 5px; \n"
"font-size: 22px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_LOGIN.setObjectName("pushButton_LOGIN")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 390, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #ffffff;\n"
"font-size: 27px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;\n"
"")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 440, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #ffffff;\n"
"font-size: 23px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;\n"
"")
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 540, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #fff2bd; \n"
"font-size: 20px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent; \n"
"")
        self.label_8.setObjectName("label_8")
        self.pushButton_signup = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_signup.setGeometry(QtCore.QRect(910, 650, 101, 41))
        self.pushButton_signup.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_signup.setFont(font)
        self.pushButton_signup.setStyleSheet("border-radius: 25px; \n"
"padding: 5px; \n"
"font-size: 15px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: transparent; \n"
"color: #022162;")
        self.pushButton_signup.setObjectName("pushButton_signup")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1129, 20, 51, 31))
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 10))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius: 13px; \n"
"padding: 1px; \n"
"font-size: 22px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1189, 20, 51, 31))
        self.pushButton_4.setMinimumSize(QtCore.QSize(40, 10))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius: 13px; \n"
"padding: 1px; \n"
"font-size: 15px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_4.setObjectName("pushButton_4")
        OwnrLOGIN.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OwnrLOGIN)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        OwnrLOGIN.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OwnrLOGIN)
        self.statusbar.setObjectName("statusbar")
        OwnrLOGIN.setStatusBar(self.statusbar)

        self.retranslateUi(OwnrLOGIN)
        QtCore.QMetaObject.connectSlotsByName(OwnrLOGIN)

    def retranslateUi(self, OwnrLOGIN):
        _translate = QtCore.QCoreApplication.translate
        OwnrLOGIN.setWindowTitle(_translate("OwnrLOGIN", "MainWindow"))
        self.label_2.setText(_translate("OwnrLOGIN", "Login"))
        self.label_3.setText(_translate("OwnrLOGIN", "Username"))
        self.label_4.setText(_translate("OwnrLOGIN", "Password"))
        self.label_6.setText(_translate("OwnrLOGIN", "Don\'t have an account?"))
        self.ownr_login_usrname.setPlaceholderText(_translate("OwnrLOGIN", "Enter your username"))
        self.ownr_login_password.setPlaceholderText(_translate("OwnrLOGIN", "Enter your password"))
        self.checkBox_rememberme.setText(_translate("OwnrLOGIN", "Remember me"))
        self.pushButton_LOGIN.setText(_translate("OwnrLOGIN", "Login"))
        self.label_5.setText(_translate("OwnrLOGIN", "J & J Roofsteel and Gutter Supply"))
        self.label_7.setText(_translate("OwnrLOGIN", "Moalboal Branch"))
        self.label_8.setText(_translate("OwnrLOGIN", "Supply       |         Install       |         Repair    "))
        self.pushButton_signup.setText(_translate("OwnrLOGIN", "Sign Up"))
        self.pushButton_3.setText(_translate("OwnrLOGIN", "-"))
        self.pushButton_4.setText(_translate("OwnrLOGIN", "x"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OwnrLOGIN = QtWidgets.QMainWindow()
    ui = Ui_OwnrLOGIN()
    ui.setupUi(OwnrLOGIN)
    OwnrLOGIN.show()
    sys.exit(app.exec_())

# OWNER SIGNUP-------------------------------------------------------------------------------------------------------
class Ui_OwnrSIGNUP(object):  # THIS PART CORRESPONDS TO class OwnerSignupPage(QMainWindow) in main_app.py
    def setupUi(self, OwnrSIGNUP):
        OwnrSIGNUP.setObjectName("OwnrSIGNUP")
        OwnrSIGNUP.resize(1280, 849)
        self.centralwidget = QtWidgets.QWidget(OwnrSIGNUP)
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")
        self.PIC = QtWidgets.QLabel(self.centralwidget)
        self.PIC.setGeometry(QtCore.QRect(0, 0, 1291, 791))
        self.PIC.setMinimumSize(QtCore.QSize(100, 40))
        self.PIC.setText("")
        self.PIC.setPixmap(QtGui.QPixmap(":/images/PIC_log_sign_in.png"))
        self.PIC.setScaledContents(True)
        self.PIC.setObjectName("PIC")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 120, 411, 251))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/JJLOGO.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(760, 20, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #022162;\n"
"font-size: 40px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 110, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #022162;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 210, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #022162;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(870, 670, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #022162;")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.owner_enterfullname = QtWidgets.QLineEdit(self.centralwidget)
        self.owner_enterfullname.setGeometry(QtCore.QRect(710, 160, 521, 51))
        self.owner_enterfullname.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.owner_enterfullname.setFont(font)
        self.owner_enterfullname.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.owner_enterfullname.setObjectName("owner_enterfullname")
        self.owner_enterusername = QtWidgets.QLineEdit(self.centralwidget)
        self.owner_enterusername.setGeometry(QtCore.QRect(710, 270, 521, 51))
        self.owner_enterusername.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.owner_enterusername.setFont(font)
        self.owner_enterusername.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.owner_enterusername.setObjectName("owner_enterusername")
        self.pushButton_signup = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_signup.setGeometry(QtCore.QRect(710, 610, 531, 51))
        self.pushButton_signup.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_signup.setFont(font)
        self.pushButton_signup.setStyleSheet("border: 2px solid #374550; \n"
"border-radius: 25px; \n"
"padding: 5px; \n"
"font-size: 22px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_signup.setObjectName("pushButton_signup")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 390, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #ffffff;\n"
"font-size: 27px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;\n"
"")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 440, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #ffffff;\n"
"font-size: 23px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;\n"
"")
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 540, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #fff2bd; \n"
"font-size: 20px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent; \n"
"")
        self.label_8.setObjectName("label_8")
        self.pushButton_backtologin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_backtologin.setGeometry(QtCore.QRect(920, 700, 101, 41))
        self.pushButton_backtologin.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_backtologin.setFont(font)
        self.pushButton_backtologin.setStyleSheet("border-radius: 25px; \n"
"padding: 5px; \n"
"font-size: 15px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: transparent; \n"
"color: #022162;")
        self.pushButton_backtologin.setObjectName("pushButton_backtologin")
        self.owner_enterpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.owner_enterpassword.setGeometry(QtCore.QRect(710, 380, 521, 51))
        self.owner_enterpassword.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.owner_enterpassword.setFont(font)
        self.owner_enterpassword.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.owner_enterpassword.setObjectName("owner_enterpassword")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(730, 320, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #022162;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.owner_confirmpass = QtWidgets.QLineEdit(self.centralwidget)
        self.owner_confirmpass.setGeometry(QtCore.QRect(710, 490, 521, 51))
        self.owner_confirmpass.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.owner_confirmpass.setFont(font)
        self.owner_confirmpass.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.owner_confirmpass.setObjectName("owner_confirmpass")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(730, 430, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #022162;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        OwnrSIGNUP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OwnrSIGNUP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        OwnrSIGNUP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OwnrSIGNUP)
        self.statusbar.setObjectName("statusbar")
        OwnrSIGNUP.setStatusBar(self.statusbar)

        self.retranslateUi(OwnrSIGNUP)
        QtCore.QMetaObject.connectSlotsByName(OwnrSIGNUP)

    def retranslateUi(self, OwnrSIGNUP):
        _translate = QtCore.QCoreApplication.translate
        OwnrSIGNUP.setWindowTitle(_translate("OwnrSIGNUP", "MainWindow"))
        self.label_2.setText(_translate("OwnrSIGNUP", "Create an Account"))
        self.label_3.setText(_translate("OwnrSIGNUP", "Full Name"))
        self.label_4.setText(_translate("OwnrSIGNUP", "Username"))
        self.label_6.setText(_translate("OwnrSIGNUP", "Already have an account?"))
        self.owner_enterfullname.setPlaceholderText(_translate("OwnrSIGNUP", "Enter your full name"))
        self.owner_enterusername.setPlaceholderText(_translate("OwnrSIGNUP", "Enter your username"))
        self.pushButton_signup.setText(_translate("OwnrSIGNUP", "Sign up"))
        self.label_5.setText(_translate("OwnrSIGNUP", "J & J Roofsteel and Gutter Supply"))
        self.label_7.setText(_translate("OwnrSIGNUP", "Moalboal Branch"))
        self.label_8.setText(_translate("OwnrSIGNUP", "Supply       |         Install       |         Repair    "))
        self.pushButton_backtologin.setText(_translate("OwnrSIGNUP", "Login"))
        self.owner_enterpassword.setPlaceholderText(_translate("OwnrSIGNUP", "Enter your password"))
        self.label_9.setText(_translate("OwnrSIGNUP", "Password"))
        self.owner_confirmpass.setPlaceholderText(_translate("OwnrSIGNUP", "Confirm your password"))
        self.label_10.setText(_translate("OwnrSIGNUP", "Confirm Password"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OwnrSIGNUP = QtWidgets.QMainWindow()
    ui = Ui_OwnrSIGNUP()
    ui.setupUi(OwnrSIGNUP)
    OwnrSIGNUP.show()
    sys.exit(app.exec_())

# CASHIER LOGIN------------------------------------------------------------------------------------------------------
class Ui_CashrLOGIN(object):  # THIS PART CORRESPONDS TO class CashierLoginPage(QMainWindow) in main_app.py
    def setupUi(self, CashrLOGIN):
        CashrLOGIN.setObjectName("CashrLOGIN")
        CashrLOGIN.resize(1280, 849)
        self.centralwidget = QtWidgets.QWidget(CashrLOGIN)
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")
        self.PIC = QtWidgets.QLabel(self.centralwidget)
        self.PIC.setGeometry(QtCore.QRect(0, 0, 1291, 791))
        self.PIC.setMinimumSize(QtCore.QSize(100, 40))
        self.PIC.setText("")
        self.PIC.setPixmap(QtGui.QPixmap(":/images/PIC_log_sign_in.png"))
        self.PIC.setScaledContents(True)
        self.PIC.setObjectName("PIC")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 120, 411, 251))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/JJLOGO.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(880, 70, 181, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #022162;\n"
"font-size: 58px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 200, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #022162;\n"
"font-size: 24px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 340, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #022162;\n"
"font-size: 24px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.cashr_login_usrname = QtWidgets.QLineEdit(self.centralwidget)
        self.cashr_login_usrname.setGeometry(QtCore.QRect(710, 250, 521, 51))
        self.cashr_login_usrname.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.cashr_login_usrname.setFont(font)
        self.cashr_login_usrname.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.cashr_login_usrname.setObjectName("cashr_login_usrname")
        self.cashr_login_password = QtWidgets.QLineEdit(self.centralwidget)
        self.cashr_login_password.setGeometry(QtCore.QRect(710, 400, 521, 51))
        self.cashr_login_password.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.cashr_login_password.setFont(font)
        self.cashr_login_password.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-size: 18px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.cashr_login_password.setObjectName("cashr_login_password")
        self.checkBox_CASHIEREMEMBERME = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_CASHIEREMEMBERME.setGeometry(QtCore.QRect(730, 470, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.checkBox_CASHIEREMEMBERME.setFont(font)
        self.checkBox_CASHIEREMEMBERME.setStyleSheet("color: #022162;\n"
"font-size: 17px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.checkBox_CASHIEREMEMBERME.setObjectName("checkBox_CASHIEREMEMBERME")
        self.pushButton_CASHIERLOGIN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CASHIERLOGIN.setGeometry(QtCore.QRect(700, 550, 531, 51))
        self.pushButton_CASHIERLOGIN.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_CASHIERLOGIN.setFont(font)
        self.pushButton_CASHIERLOGIN.setStyleSheet("border: 2px solid #374550; \n"
"border-radius: 25px; \n"
"padding: 5px; \n"
"font-size: 22px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_CASHIERLOGIN.setObjectName("pushButton_CASHIERLOGIN")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 390, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #ffffff;\n"
"font-size: 27px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;\n"
"")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 440, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #ffffff;\n"
"font-size: 23px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;\n"
"")
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 540, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #fff2bd; \n"
"font-size: 20px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent; \n"
"")
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1129, 20, 51, 31))
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 10))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius: 13px; \n"
"padding: 1px; \n"
"font-size: 22px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1189, 20, 51, 31))
        self.pushButton_4.setMinimumSize(QtCore.QSize(40, 10))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius: 13px; \n"
"padding: 1px; \n"
"font-size: 15px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_4.setObjectName("pushButton_4")
        CashrLOGIN.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CashrLOGIN)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        CashrLOGIN.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CashrLOGIN)
        self.statusbar.setObjectName("statusbar")
        CashrLOGIN.setStatusBar(self.statusbar)

        self.retranslateUi(CashrLOGIN)
        QtCore.QMetaObject.connectSlotsByName(CashrLOGIN)

    def retranslateUi(self, CashrLOGIN):
        _translate = QtCore.QCoreApplication.translate
        CashrLOGIN.setWindowTitle(_translate("CashrLOGIN", "MainWindow"))
        self.label_2.setText(_translate("CashrLOGIN", "Login"))
        self.label_3.setText(_translate("CashrLOGIN", "Username"))
        self.label_4.setText(_translate("CashrLOGIN", "Password"))
        self.cashr_login_usrname.setPlaceholderText(_translate("CashrLOGIN", "Enter your username"))
        self.cashr_login_password.setPlaceholderText(_translate("CashrLOGIN", "Enter your password"))
        self.checkBox_CASHIEREMEMBERME.setText(_translate("CashrLOGIN", "Remember me"))
        self.pushButton_CASHIERLOGIN.setText(_translate("CashrLOGIN", "Login"))
        self.label_5.setText(_translate("CashrLOGIN", "J & J Roofsteel and Gutter Supply"))
        self.label_7.setText(_translate("CashrLOGIN", "Moalboal Branch"))
        self.label_8.setText(_translate("CashrLOGIN", "Supply       |         Install       |         Repair    "))
        self.pushButton_3.setText(_translate("CashrLOGIN", "-"))
        self.pushButton_4.setText(_translate("CashrLOGIN", "x"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CashrLOGIN = QtWidgets.QMainWindow()
    ui = Ui_CashrLOGIN()
    ui.setupUi(CashrLOGIN)
    CashrLOGIN.show()
    sys.exit(app.exec_())

# OWNER DASHBOARD----------------------------------------------------------------------------------------------------
class Ui_OWNER_DASHBOARD(object):  # THIS PART CORRESPONDS TO class OwnerDashboard(QMainWindow) in main_app.py
    def setupUi(self, OWNER_DASHBOARD):
        OWNER_DASHBOARD.setObjectName("OWNER_DASHBOARD")
        OWNER_DASHBOARD.resize(1280, 849)
        self.centralwidget = QtWidgets.QWidget(OWNER_DASHBOARD)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-1430, -150, 2721, 1361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/PIC_log_sign_in.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 1231, 511))
        self.label_2.setStyleSheet("color: #022162;\n"
"font-size: 58px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_2.setObjectName("label_2")
        self.pushButton_OwnrDASH = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OwnrDASH.setGeometry(QtCore.QRect(30, 100, 201, 71))
        self.pushButton_OwnrDASH.setObjectName("pushButton_OwnrDASH")
        OWNER_DASHBOARD.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OWNER_DASHBOARD)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        OWNER_DASHBOARD.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OWNER_DASHBOARD)
        self.statusbar.setObjectName("statusbar")
        OWNER_DASHBOARD.setStatusBar(self.statusbar)

        self.retranslateUi(OWNER_DASHBOARD)
        QtCore.QMetaObject.connectSlotsByName(OWNER_DASHBOARD)

    def retranslateUi(self, OWNER_DASHBOARD):
        _translate = QtCore.QCoreApplication.translate
        OWNER_DASHBOARD.setWindowTitle(_translate("OWNER_DASHBOARD", "MainWindow"))
        self.label_2.setText(_translate("OWNER_DASHBOARD", "OWNER DASHBOARD WALA PA HUHU"))
        self.pushButton_OwnrDASH.setText(_translate("OWNER_DASHBOARD", "DASHBOARD"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OWNER_DASHBOARD = QtWidgets.QMainWindow()
    ui = Ui_OWNER_DASHBOARD()
    ui.setupUi(OWNER_DASHBOARD)
    OWNER_DASHBOARD.show()
    sys.exit(app.exec_())

# CASHIER DASHBOARD --------------------------------------------------------------------------------------------------
class Ui_CASHIER_DASHBOARD(object):  # THIS PART CORRESPONDS TO class CashierDashboard(QMainWindow) in main_app.py
    def setupUi(self, CASHIER_DASHBOARD):
        CASHIER_DASHBOARD.setObjectName("CASHIER_DASHBOARD")
        CASHIER_DASHBOARD.resize(1280, 849)
        self.centralwidget = QtWidgets.QWidget(CASHIER_DASHBOARD)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-1430, -150, 2721, 1361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/PIC_log_sign_in.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 1231, 511))
        self.label_2.setStyleSheet("color: #022162;\n"
"font-size: 58px;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_2.setObjectName("label_2")
        self.pushButton_CashrDASH = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CashrDASH.setGeometry(QtCore.QRect(20, 90, 201, 71))
        self.pushButton_CashrDASH.setObjectName("pushButton_CashrDASH")
        CASHIER_DASHBOARD.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CASHIER_DASHBOARD)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        CASHIER_DASHBOARD.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CASHIER_DASHBOARD)
        self.statusbar.setObjectName("statusbar")
        CASHIER_DASHBOARD.setStatusBar(self.statusbar)

        self.retranslateUi(CASHIER_DASHBOARD)
        QtCore.QMetaObject.connectSlotsByName(CASHIER_DASHBOARD)

    def retranslateUi(self, CASHIER_DASHBOARD):
        _translate = QtCore.QCoreApplication.translate
        CASHIER_DASHBOARD.setWindowTitle(_translate("CASHIER_DASHBOARD", "MainWindow"))
        self.label_2.setText(_translate("CASHIER_DASHBOARD", "CASHIER DASHBOARD BY CLAUDIN"))
        self.pushButton_CashrDASH.setText(_translate("CASHIER_DASHBOARD", "DASHBOARD"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CASHIER_DASHBOARD = QtWidgets.QMainWindow()
    ui = Ui_CASHIER_DASHBOARD()
    ui.setupUi(CASHIER_DASHBOARD)
    CASHIER_DASHBOARD.show()
    sys.exit(app.exec_())

# --------------------------------------------------------------------------------------------------------------------
