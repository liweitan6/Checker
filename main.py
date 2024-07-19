import sys
from PyQt5.QtWidgets import QApplication
from login import LoginWindow
from main_window import MainWindow
from database import create_all_tables, get_last_login
class CodeDuplicationChecker:
    def __init__(self):
        self.app = QApplication(sys.argv)
        create_all_tables()
        self.init_login()

    def init_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.login_window.login_successful.connect(self.show_main_window)

    def show_main_window(self):
        self.main_window = MainWindow()
        last_login = get_last_login()
        self.main_window.setWindowTitle(f'Code Duplication Checker - 上次登陆时间: {last_login}')
        self.main_window.show()

    def run(self):
        return self.app.exec_()

if __name__ == '__main__':
    checker = CodeDuplicationChecker()
    sys.exit(checker.run())