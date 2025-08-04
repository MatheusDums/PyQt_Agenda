import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from login_ok import Ui_Tela1

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