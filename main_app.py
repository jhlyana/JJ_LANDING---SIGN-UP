import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QMessageBox  
from ui_classes import Ui_JJ_LANDING
from ui_classes import Ui_OwnrLOGIN
from ui_classes import Ui_OwnrSIGNUP
from ui_classes import Ui_OWNER_DASHBOARD
from ui_classes import Ui_CashrLOGIN
from ui_classes import Ui_CASHIER_DASHBOARD

class LandingPage(QMainWindow): # J & J ELEVATE LANDING PAGE
    def __init__(self):
        super().__init__()
        self.ui = Ui_JJ_LANDING()
        self.ui.setupUi(self)

        # Continue as OWNER button click
        self.ui.pushButton_contOwner.clicked.connect(self.open_owner_login)
        
        # Continue as CASHIER button click
        self.ui.pushButton_contCashier.clicked.connect(self.open_cashier_login)

    def open_owner_login(self):
        self.owner_login_window = OwnerLoginPage()
        self.owner_login_window.show()
        self.close()

    def open_cashier_login(self):
        self.cashier_login_window = CashierLoginPage()
        self.cashier_login_window.show()
        self.close()

class OwnerLoginPage(QMainWindow): # ENTER OWNER LOG IN INFO.
    def __init__(self):
        super().__init__()
        self.ui = Ui_OwnrLOGIN()
        self.ui.setupUi(self)

        # Click Sign-Up button in Log in
        self.ui.pushButton_signup.clicked.connect(self.open_signup_page)       

        # Open Owner Dashboard after clicking Log in
        self.ui.pushButton_LOGIN.clicked.connect(self.open_owner_dashboard)

    def open_signup_page(self):
        self.signup_window = OwnerSignupPage()
        self.signup_window.show()
        self.close()

    def open_owner_dashboard(self):
        self.owner_dashboard = OwnerDashboard()
        self.owner_dashboard.show()
        self.close()

class OwnerSignupPage(QMainWindow): # FOR OWNER TO CREATE THEIR ACCOUNT 
    def __init__(self):
        super().__init__()
        self.ui = Ui_OwnrSIGNUP()
        self.ui.setupUi(self)

        # Successful account creation after clicking sign up button
        self.ui.pushButton_signup.clicked.connect(self.create_account)

        # Go back to Login page
        self.ui.pushButton_backtologin.clicked.connect(self.go_to_login)

    def create_account(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText("Your account has been created!")
        msg.exec_()

    def go_to_login(self):
        self.login_window = OwnerLoginPage()
        self.login_window.show()
        self.close()
        
class OwnerDashboard(QMainWindow): # VIEW OWNER DASHBOARD
    def __init__(self):
        super().__init__()
        self.ui = Ui_OWNER_DASHBOARD()
        self.ui.setupUi(self)

class CashierLoginPage(QMainWindow): # ENTER CASHIER LOG IN INFO.
    def __init__(self):
        super().__init__()
        self.ui = Ui_CashrLOGIN()
        self.ui.setupUi(self)      

        # Open Cashier Dashboard (JUST DELETE START FROM THIS)
        self.ui.pushButton_CASHIERLOGIN.clicked.connect(self.open_cashier_dashboard)

    def open_cashier_dashboard(self):
        self.cashier_dashboard = CashierDashboard()
        self.cashier_dashboard.show()
        self.close()
        
class CashierDashboard(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.ui = Ui_CASHIER_DASHBOARD()
        self.ui.setupUi(self)   # Open Cashier Dashboard (END DELETION HERE)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LandingPage()
    window.show()

    sys.exit(app.exec_())
