from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QApplication, QTableWidget, QTableWidgetItem, QWidget
from PyQt6.QtCore import QDate, QTimer
from datetime import datetime
import requests
import json


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 524)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(0, -8, 751, 51))
        self.title_label.setStyleSheet("font: 75 14pt \"Segoe Print\";")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.tabela = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tabela.setGeometry(QtCore.QRect(0, 280, 621, 241))
        self.tabela.setAutoFillBackground(False)
        self.tabela.setStyleSheet("")
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(6)
        self.tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tabela.setHorizontalHeaderItem(1, item)  
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tabela.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tabela.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tabela.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tabela.setHorizontalHeaderItem(5, item)
        self.tabela.horizontalHeader().setDefaultSectionSize(101)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 40, 751, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.linha_email = QtWidgets.QLineEdit(parent=self.frame)
        self.linha_email.setObjectName("linha_email")
        self.gridLayout.addWidget(self.linha_email, 3, 0, 1, 1)
        self.label_nascimento = QtWidgets.QLabel(parent=self.frame)
        self.label_nascimento.setObjectName("label_nascimento")
        self.gridLayout.addWidget(self.label_nascimento, 4, 0, 1, 1)
        self.label_nome = QtWidgets.QLabel(parent=self.frame)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.label_telefone = QtWidgets.QLabel(parent=self.frame)
        self.label_telefone.setObjectName("label_telefone")
        self.gridLayout.addWidget(self.label_telefone, 0, 2, 1, 1)
        self.label_obs = QtWidgets.QLabel(parent=self.frame)
        self.label_obs.setObjectName("label_obs")
        self.gridLayout.addWidget(self.label_obs, 2, 2, 1, 1)
        self.linha_nome = QtWidgets.QLineEdit(parent=self.frame)
        self.linha_nome.setObjectName("linha_nome")
        self.gridLayout.addWidget(self.linha_nome, 1, 0, 1, 1)
        self.label_email = QtWidgets.QLabel(parent=self.frame)
        self.label_email.setObjectName("label_email")
        self.gridLayout.addWidget(self.label_email, 2, 0, 1, 1)
        self.linha_telefone = QtWidgets.QLineEdit(parent=self.frame)
        self.linha_telefone.setAutoFillBackground(False)
        self.linha_telefone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linha_telefone.setObjectName("linha_telefone")
        self.gridLayout.addWidget(self.linha_telefone, 1, 2, 1, 1)
        self.salvar_btn = QtWidgets.QPushButton(parent=self.frame)
        self.salvar_btn.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/images/save-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.salvar_btn.setIcon(icon)
        self.salvar_btn.setObjectName("salvar_btn")
        self.gridLayout.addWidget(self.salvar_btn, 7, 0, 1, 2)
        self.linha_obs = QtWidgets.QLineEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linha_obs.sizePolicy().hasHeightForWidth())
        self.linha_obs.setSizePolicy(sizePolicy)
        self.linha_obs.setObjectName("linha_obs")
        self.gridLayout.addWidget(self.linha_obs, 3, 2, 3, 1)
        self.cancelar_btn = QtWidgets.QPushButton(parent=self.frame)
        self.cancelar_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/images/cancel-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cancelar_btn.setIcon(icon1)
        self.cancelar_btn.setObjectName("cancelar_btn")
        self.gridLayout.addWidget(self.cancelar_btn, 7, 2, 1, 1)
        self.data_nasc = QtWidgets.QDateEdit(parent=self.frame)
        self.data_nasc.setObjectName("data_nasc")
        self.gridLayout.addWidget(self.data_nasc, 5, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(620, 280, 121, 241))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.editar_btn = QtWidgets.QPushButton(parent=self.frame_2)
        self.editar_btn.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.editar_btn.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(0, 0, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/images/edit-3-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.editar_btn.setIcon(icon2)
        self.editar_btn.setObjectName("editar_btn")
        self.excluir_btn = QtWidgets.QPushButton(parent=self.frame_2)
        self.excluir_btn.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.excluir_btn.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 0, 0);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/images/delete-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.excluir_btn.setIcon(icon3)
        self.excluir_btn.setObjectName("excluir_btn")
        self.tabela.setColumnWidth(1, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.listar()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agenda de Contatos"))
        MainWindow.setWindowIcon(QIcon('assets/images/image.png'))
        self.title_label.setText(_translate("MainWindow", "Agenda de Contatos"))
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tabela.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Telefone"))
        item = self.tabela.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tabela.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nascimento"))
        item = self.tabela.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Observações"))
        self.label_nascimento.setText(_translate("MainWindow", "Data de Nascimento"))
        self.label_nome.setText(_translate("MainWindow", "Nome"))
        self.label_telefone.setText(_translate("MainWindow", "Telefone"))
        self.label_obs.setText(_translate("MainWindow", "Observações"))
        self.label_email.setText(_translate("MainWindow", "Email"))
        self.salvar_btn.setText(_translate("MainWindow", "Salvar"))
        self.cancelar_btn.setText(_translate("MainWindow", "Cancelar"))
        self.editar_btn.setText(_translate("MainWindow", "Editar"))
        self.excluir_btn.setText(_translate("MainWindow", "Excluir"))
        """ desenvolvimento """
        self.salvar_btn.clicked.connect(self.envia)
        self.cancelar_btn.clicked.connect(self.padrao)
        self.excluir_btn.clicked.connect(self.excluir)
        self.editar_btn.clicked.connect(self.editar)
        
        

    def padrao(self) :
        self.linha_nome.setText("")
        self.linha_telefone.setText("")
        self.linha_email.setText("")
        self.data_nasc.setDate(QDate(2000, 1, 1))
        self.linha_obs.setText("")
        self.salvar_btn.setText("Salvar")
        
    def listar(self) :
        url = 'http://localhost/pyqt_agenda/php/api/listar.php'
        response = requests.get(url)
        dados = response.json()
        
        self.tabela.setRowCount(0)  
        
        for i in range(len(dados)):  
            id = dados[i]['pyt_id']
            nome = dados[i]['pyt_nome']
            telefone = dados[i]['pyt_telefone']
            email = dados[i]['pyt_email']
            nascimento = dados[i]['pyt_nascimento']
            observacoes = dados[i]['pyt_observacoes']
            linha = self.tabela.rowCount()
            self.tabela.insertRow(linha)
            nome_tb = QtWidgets.QTableWidgetItem(nome)
            self.tabela.setItem(linha, 0, nome_tb)
            id_tb = QtWidgets.QTableWidgetItem(str(id))
            self.tabela.setItem(linha, 1, id_tb)
            telefone_tb = QtWidgets.QTableWidgetItem(telefone)
            self.tabela.setItem(linha, 2, telefone_tb)
            email_tb = QtWidgets.QTableWidgetItem(email)
            self.tabela.setItem(linha, 3, email_tb)
            nasc_tb = QtWidgets.QTableWidgetItem(nascimento)
            self.tabela.setItem(linha, 4, nasc_tb)
            obs_tb = QtWidgets.QTableWidgetItem(observacoes)
            self.tabela.setItem(linha, 5, obs_tb)
            self.padrao()
        
    def envia(self, i) :
        data = {
            'nome' : self.linha_nome.text(),
            'telefone' : self.linha_telefone.text(),
            'email' : self.linha_email.text(),
            'nascimento': self.data_nasc.date().toString('dd-MM-yyyy'),
            'observacoes' : self.linha_obs.text()    
        }
        url = 'http://localhost/pyqt_agenda/php/api/insere.php'
        texto_nome = self.linha_nome.text()
        texto_telefone = self.linha_telefone.text()
        texto_email = self.linha_email.text()
        texto_observacoes = self.linha_obs.text()
        
        if not texto_nome or not texto_email or not texto_telefone or not texto_observacoes:
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('assets/images/image.png'))
            reply.setText("Preencha todos os campos!")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            x = reply.exec()
        else:
            if self.salvar_btn.text() == "Salvar" :
                resposta = requests.post(url, json=data)
                print(resposta.text)
                self.padrao()
                status_code = resposta.status_code
                if status_code == 200 :
                    reply = QMessageBox()
                    reply.setWindowTitle("Agenda de Contatos")
                    reply.setWindowIcon(QIcon('assets/images/image.png'))
                    reply.setText("Contato adicionado com sucesso")
                    reply.setStandardButtons(QMessageBox.StandardButton.Yes)
                    x = reply.exec()
                else:
                    reply = QMessageBox()
                    reply.setWindowTitle("Agenda de Contatos")
                    reply.setWindowIcon(QIcon('assets/images/image.png'))
                    reply.setText("Erro ao adicionar contato")
                    reply.setStandardButtons(QMessageBox.StandardButton.Yes)
                    x = reply.exec()


                """ agora tem que puxar os dados do banco, e apresentar na tabela """
                self.listar()
        
    def excluir(self) :
        url_delete = 'http://localhost/pyqt_agenda/php/api/delete.php'
        linha = self.tabela.currentRow()
        if linha >= 0 :
            item = self.tabela.item(linha, 1)
            item_id = item.text()
        data = {
            'id' : item_id 
        }
        
        if linha >= 0:
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('assets/images/image.png'))
            reply.setText("Deseja apagar o contato?")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes | 
                     QMessageBox.StandardButton.No)
            x = reply.exec()
            
            if x == QMessageBox.StandardButton.Yes:
                self.tabela.removeRow(linha)
                response = requests.delete(url_delete,  json=data)
        else:
            print("Nenhuma linha selecionada.")
            
    def editar(self) :  
        linha = self.tabela.currentRow()
        self.salvar_btn.setText("Atualizar")
        
        if linha >= 0 :
            item_id = self.tabela.item(linha, 1)
            item_nome = self.tabela.item(linha, 0)
            item_telefone = self.tabela.item(linha, 2)
            item_email = self.tabela.item(linha, 3)
            item_nasc = self.tabela.item(linha, 4)
            item_obs = self.tabela.item(linha, 5)
            text_nome = item_nome.text()
            text_telefone = item_telefone.text()
            text_email = item_email.text()
            text_nasc = item_nasc.text()
            text_observacoes = item_obs.text()           
        self.linha_nome.setText(text_nome)
        self.linha_telefone.setText(text_telefone)
        self.linha_email.setText(text_email)
        
        qdate = QDate.fromString(text_nasc, "dd-MM-yyyy")
        if not qdate.isValid():
            qdate = QDate.fromString(text_nasc, "dd-MM-yyyy")
            self.data_nasc.setDate(qdate)
        
        self.linha_obs.setText(text_observacoes)
         
        dados_atualiza = {
            'id' : item_id.text(),
            'nome' : self.linha_nome.text(),
            'telefone' : self.linha_telefone.text(),
            'email' : self.linha_email.text(),
            'nascimento': self.data_nasc.date().toString('dd-MM-yyyy'),
            'observacoes' : self.linha_obs.text() 
        }
        self.salvar_btn.clicked.connect(self.atualiza)
        
    def atualiza(self) :
        linha = self.tabela.currentRow()
        if self.salvar_btn.text() == "Atualizar" :
            item_id = self.tabela.item(linha, 1)
            dados_ok = {
                'id' : item_id.text(),
                'nome' : self.linha_nome.text(),
                'telefone' : self.linha_telefone.text(),
                'email' : self.linha_email.text(),
                'nascimento': self.data_nasc.date().toString('dd-MM-yyyy'),
                'observacoes' : self.linha_obs.text() 
            }
            
            self.cancelar_btn.clicked.connect(self.padrao)
            
            url = 'http://localhost/pyqt_agenda/php/api/edita.php'
            resposta = requests.post(url, json=dados_ok)
            self.salvar_btn.setText("Salvar")
            print(resposta.text)
            self.padrao()
        
""" não mexer """    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
