import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from login_ok import Ui_Tela1
import configparser
import os
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon

config = configparser.ConfigParser()

if os.path.exists("config.ini"):
    class TelaLogin(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Tela1()
            self.ui.setupUi(self)

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        login = TelaLogin()
        login.showMaximized()
        sys.exit(app.exec())
       
else:
    print("erro")
    exit()

