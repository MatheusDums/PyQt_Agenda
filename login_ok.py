from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QApplication, QTableWidget, QTableWidgetItem, QWidget
from PyQt6.QtCore import QDate, QTimer
from datetime import datetime
from errados.python.teste_id import Ui_MainWindow
import requests
import json

class Ui_Tela1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: white;")
        MainWindow.setWindowIcon(QIcon("assets/images/image.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        layout_principal = QtWidgets.QVBoxLayout(self.centralwidget)
        layout_principal.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_login = QtWidgets.QLabel("Login")
        font_login = QtGui.QFont("Segoe Print", 18)
        font_login.setItalic(True)
        self.label_login.setFont(font_login)
        self.label_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(self.label_login)
        frame = QtWidgets.QFrame()
        frame_layout = QtWidgets.QVBoxLayout(frame)
        frame_layout.setSpacing(20)
        frame.setContentsMargins(0, 0, 0, 0)
        frame.setMaximumWidth(400)
        frame.setStyleSheet("""
            QLineEdit {
border: none;border-bottom: 1px solid #000; padding: 10px;font-size: 14pt;} """)
        self.linha_user = QtWidgets.QLineEdit()
        self.linha_user.setPlaceholderText("Email")
        frame_layout.addWidget(self.linha_user)
        self.linha_pass = QtWidgets.QLineEdit()
        self.linha_pass.setPlaceholderText("Senha")
        self.linha_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        frame_layout.addWidget(self.linha_pass)
        self.login_btn = QtWidgets.QPushButton("Entrar")
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_btn.setStyleSheet("""
            QPushButton {background-color: black;color: white;border-radius: 5px;padding: 12px;font-size: 12pt;}
QPushButton:hover {background-color: #333;}""")
        frame_layout.addWidget(self.login_btn)
        layout_principal.addWidget(frame)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
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
            dados_rec = resposta_json['data']['dados_rec']
            print('dados:' , dados_rec)
            statuscode = resposta.status_code
            if resposta_json['status'] == 200:
                
                from testando import Ui_MainWindow
                self.window_principal = QtWidgets.QMainWindow()
                self.ui_principal = Ui_MainWindow()
                self.ui_principal.setupUi(self.window_principal)
                self.ui_principal.listar()
                self.window_principal.showMaximized()
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
    MainWindow.showMaximized()
    sys.exit(app.exec())
