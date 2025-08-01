from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QApplication, QTableWidget, QTableWidgetItem, QWidget
from PyQt6.QtCore import QDate, QTimer
from datetime import datetime
from teste_id import Ui_MainWindow
import requests
import json

class Ui_Tela1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 541)
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 160, 751, 381))
        self.frame.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.linha_user = QtWidgets.QLineEdit(parent=self.frame)
        self.linha_user.setGeometry(QtCore.QRect(210, 70, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.linha_user.setFont(font)
        self.linha_user.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.linha_user.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.linha_user.setObjectName("linha_user")
        self.login_btn = QtWidgets.QPushButton(parent=self.frame)
        self.login_btn.setGeometry(QtCore.QRect(210, 210, 331, 51))
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_btn.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.login_btn.setObjectName("login_btn")
        self.linha_pass = QtWidgets.QLineEdit(parent=self.frame)
        self.linha_pass.setGeometry(QtCore.QRect(210, 140, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.linha_pass.setFont(font)
        self.linha_pass.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.linha_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.linha_pass.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.linha_pass.setObjectName("linha_pass")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 100, 751, 61))
        self.label_2.setStyleSheet("font: 75 16pt \"Segoe Print\";\n"
"font: 20pt \"Segoe Print\";")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.MainWindow = MainWindow 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login - BudContatos"))
        MainWindow.setWindowIcon(QIcon('assets/images/image.png'))
        self.linha_user.setPlaceholderText(_translate("MainWindow", "Email"))
        self.login_btn.setText(_translate("MainWindow", "Entrar"))
        self.linha_pass.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.label_2.setText(_translate("MainWindow", "BudContatos - Login"))
        
        """ desenvolvimento """
        self.login_btn.clicked.connect(self.entrar)
        
    def entrar(self):
        texto_user = self.linha_user.text()
        texto_password = self.linha_pass.text()
        
        if not texto_user or not texto_password :
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('assets/images/image.png'))
            reply.setText("Preencha todos os campos!")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            x = reply.exec()
        else:
            dados = {
                'user' : texto_user,
                'password' : texto_password
            }
            
            url = 'http://localhost/pyqt_agenda/php/api/login.php'
            resposta = requests.post(url, json=dados)
            resposta_json = json.loads(resposta.text)
            statuscode = resposta.status_code
            if resposta_json['status'] == 200:
                """ reply = QMessageBox()
                reply.setWindowTitle("Agenda de Contatos")
                reply.setWindowIcon(QIcon('assets/images/image.png'))
                reply.setText("Login realizado com sucesso!")
                reply.setStandardButtons(QMessageBox.StandardButton.Yes)
                x = reply.exec() """
                
                from main import Ui_MainWindow
                self.window_principal = QtWidgets.QMainWindow()
                self.ui_principal = Ui_MainWindow()
                self.ui_principal.setupUi(self.window_principal)
                self.window_principal.show()
                
                self.MainWindow.close()
                
            elif resposta_json['status'] == 400:
                reply = QMessageBox()
                reply.setWindowTitle("Agenda de Contatos")
                reply.setWindowIcon(QIcon('assets/images/image.png'))
                reply.setText("Credenciais incorretas!")
                reply.setStandardButtons(QMessageBox.StandardButton.Yes)
                x = reply.exec()
                
            else:
                reply = QMessageBox()
                reply.setWindowTitle("Agenda de Contatos")
                reply.setWindowIcon(QIcon('assets/images/image.png'))
                reply.setText("Erro ao conectar com o servidor!")
                reply.setStandardButtons(QMessageBox.StandardButton.Yes)
                x = reply.exec()

            self.padrao()

    def padrao(self) :
        self.linha_user.setText('')
        self.linha_pass.setText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Tela1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
