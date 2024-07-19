from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal
from database import save_login, get_last_login
from datetime import datetime
class LoginWindow(QWidget):
    login_successful = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.usernameLabel = QLabel('用户名')
        self.usernameInput = QLineEdit()
        self.passwordLabel = QLabel('密码')
        self.passwordInput = QLineEdit()
        self.usernameInput.setEchoMode(QLineEdit.Normal)
        self.passwordInput.setEchoMode(QLineEdit.Normal)
        self.loginButton = QPushButton('登录')
        layout.addWidget(self.usernameInput)
        layout.addWidget(self.usernameLabel)
        layout.addWidget(self.passwordInput)
        layout.addWidget(self.passwordLabel)
        layout.addWidget(self.loginButton)
        
        
        # self.loginButton.clicked.connect(self.getClicked)
        self.loginButton.clicked.connect(self.loginCheck)

        self.setLayout(layout)
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('登录')

    def loginCheck(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        login_time = datetime.now()
        
        # print(username,password)
        # Simple authentication (replace with proper authentication later)
        if username == 'admin' and password == 'password':
            QMessageBox.information(self, '提示', '登陆成功')
            save_login()
            self.login_successful.emit()
            self.close()
        elif(username == '' or password == ''):
            QMessageBox.warning(self, '提示', '请输入用户名和密码')
        else:
            QMessageBox.warning(self, '提示', '用户名或密码错误')
    
    def getClicked(self):
        QMessageBox.information(self, 'Message', '按钮被点击了！')
        # print("clicked")