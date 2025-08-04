from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QApplication, QTableWidget, QTableWidgetItem, QWidget
from PyQt6.QtCore import QDate, QTimer
from datetime import datetime
import requests
import json
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()  # JANELA MAXIMIZADA
        MainWindow.setStyleSheet("background-color: #ffffff;")
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(50, 30, 50, 30)  # Margens laterais e superior/inferior
        self.layout.setSpacing(15)

        # TÍTULO
        self.title_label = QtWidgets.QLabel("Agenda de Contatos")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font: 20pt 'Segoe Print';")
        self.layout.addWidget(self.title_label)

        # FORMULÁRIO
        self.form_layout = QtWidgets.QGridLayout()
        self.form_layout.setHorizontalSpacing(20)
        self.form_layout.setVerticalSpacing(10)

        self.label_nome = QtWidgets.QLabel("Nome")
        self.linha_nome = QtWidgets.QLineEdit()

        self.label_telefone = QtWidgets.QLabel("Telefone")
        self.linha_telefone = QtWidgets.QLineEdit()

        self.label_email = QtWidgets.QLabel("Email")
        self.linha_email = QtWidgets.QLineEdit()

        self.label_obs = QtWidgets.QLabel("Observações")
        self.linha_obs = QtWidgets.QLineEdit()

        self.label_nascimento = QtWidgets.QLabel("Data de Nascimento")
        self.data_nasc = QtWidgets.QDateEdit()
        self.data_nasc.setCalendarPopup(True)
        self.data_nasc.setDate(QDate(2000, 1, 1))

        self.form_layout.addWidget(self.label_nome, 0, 0)
        self.form_layout.addWidget(self.linha_nome, 1, 0)

        self.form_layout.addWidget(self.label_telefone, 0, 1)
        self.form_layout.addWidget(self.linha_telefone, 1, 1)

        self.form_layout.addWidget(self.label_email, 2, 0)
        self.form_layout.addWidget(self.linha_email, 3, 0)

        self.form_layout.addWidget(self.label_obs, 2, 1)
        self.form_layout.addWidget(self.linha_obs, 3, 1)

        self.form_layout.addWidget(self.label_nascimento, 4, 0)
        self.form_layout.addWidget(self.data_nasc, 5, 0)

        self.layout.addLayout(self.form_layout)

        # BOTÕES
        self.botoes_layout = QtWidgets.QHBoxLayout()
        self.salvar_btn = QtWidgets.QPushButton("Salvar")
        self.salvar_btn.setStyleSheet("background-color: #00ff00; font-weight: bold;")
        self.cancelar_btn = QtWidgets.QPushButton("Cancelar")
        self.cancelar_btn.setStyleSheet("background-color: #ff0000; color: #000; font-weight: bold;")

        self.botoes_layout.addWidget(self.salvar_btn)
        self.botoes_layout.addWidget(self.cancelar_btn)
        self.layout.addLayout(self.botoes_layout)

        # TABELA
        self.tabela = QtWidgets.QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(["Nome", "ID", "Telefone", "Email", "Nascimento", "Observações"])
        self.tabela.setColumnHidden(1, True)  # Oculta a coluna ID
        self.tabela.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        self.tabela.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.layout.addWidget(self.tabela)

        MainWindow.setCentralWidget(self.centralwidget)

        # Ocultar ID se ainda existir
        self.tabela.setColumnHidden(1, True)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.sair_btn_2.setText(_translate("MainWindow", "Sair"))
        """ desenvolvimento """
        self.editar_btn.hide()
        self.excluir_btn.hide()
        self.tabela.itemSelectionChanged.connect(self.verifica_selecao)
        
        self.salvar_btn.clicked.connect(self.envia)
        self.cancelar_btn.clicked.connect(self.padrao)
        self.excluir_btn.clicked.connect(self.excluir)
        self.editar_btn.clicked.connect(self.editar)
        self.sair_btn_2.clicked.connect(self.sair)
        
        

    def padrao(self) :
        self.linha_nome.setText("")
        self.linha_telefone.setText("")
        self.linha_email.setText("")
        self.data_nasc.setDate(QDate(2000, 1, 1))
        self.linha_obs.setText("")
        self.salvar_btn.setText("Salvar")
        self.editar_btn.hide()
        self.excluir_btn.hide()

        
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
            """ reply.setWindowIcon(QIcon('assets/images/image.png')) """
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
                    """ reply.setWindowIcon(QIcon('assets/images/image.png')) """
                    reply.setText("Contato adicionado com sucesso")
                    reply.setStandardButtons(QMessageBox.StandardButton.Yes)
                    x = reply.exec()
                else:
                    reply = QMessageBox()
                    reply.setWindowTitle("Agenda de Contatos")
                    """ reply.setWindowIcon(QIcon('assets/images/image.png')) """
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
            """ reply.setWindowIcon(QIcon('assets/images/image.png')) """
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
            
    def verifica_selecao(self):
        selecionados = self.tabela.selectedItems()
        if selecionados:
            self.editar_btn.show()
            self.excluir_btn.show()
        else:
            self.editar_btn.hide()
            self.excluir_btn.hide()
        
        
    def sair(self) :
        self.close()
""" não mexer """    



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())
