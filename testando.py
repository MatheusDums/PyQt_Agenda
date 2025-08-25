from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon, QColor
from PyQt6.QtWidgets import QMessageBox, QAbstractItemView
from PyQt6.QtCore import QDate, Qt
import base64
import os
import requests
from datetime import datetime
import configparser
from configparser import ConfigParser
import time
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: #ffffff;")
        MainWindow.setWindowTitle("Agenda de contatos")
        MainWindow.setWindowIcon(QIcon("assets/images/image.png"))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(50, 30, 50, 30)
        self.layout.setSpacing(15)
        self.title_label = QtWidgets.QLabel("Agenda de Contatos")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font: 40px 'Dubai';")
        self.layout.addWidget(self.title_label)
        self.form_layout = QtWidgets.QGridLayout()
        self.form_layout.setHorizontalSpacing(20)
        self.form_layout.setVerticalSpacing(10)
        self.label_nome = QtWidgets.QLabel("Nome")
        self.label_nome.setFont(QtGui.QFont("Dubai", 17))
        self.linha_nome = QtWidgets.QLineEdit()
        self.linha_nome.setFont(QtGui.QFont("Dubai", 15))
        self.label_telefone = QtWidgets.QLabel("Telefone")
        self.label_telefone.setFont(QtGui.QFont("Dubai", 17))
        self.linha_telefone = QtWidgets.QLineEdit()
        self.linha_telefone.setFont(QtGui.QFont("Dubai", 15))
        self.label_email = QtWidgets.QLabel("Email")
        self.label_email.setFont(QtGui.QFont("Dubai", 17))
        self.linha_email = QtWidgets.QLineEdit()
        self.linha_email.setFont(QtGui.QFont("Dubai", 15))
        self.label_obs = QtWidgets.QLabel("Observações")
        self.label_obs.setFont(QtGui.QFont("Dubai", 17))
        self.linha_obs = QtWidgets.QLineEdit()
        self.linha_obs.setFont(QtGui.QFont("Dubai", 15))
        self.label_nascimento = QtWidgets.QLabel("Data de Nascimento")
        self.label_nascimento.setFont(QtGui.QFont("Dubai", 17))
        self.data_nasc = QtWidgets.QDateEdit()
        self.data_nasc.setFont(QtGui.QFont("Dubai", 15))
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
        self.botoes_layout = QtWidgets.QHBoxLayout()
        self.salvar_btn = QtWidgets.QPushButton("Salvar")
        self.salvar_btn.setStyleSheet("""QPushButton {font-size:17px;background-color: #009417;font-weight: bold;padding: 10px;border: none;}""")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/images/save-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.salvar_btn.setIcon(icon)
        self.cancelar_btn = QtWidgets.QPushButton("Cancelar")
        self.cancelar_btn.setStyleSheet("""QPushButton {font-size:17px;background-color: #ff7f05;color: black;font-weight: bold;padding: 10px;border: none;}""")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/images/cancel-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cancelar_btn.setIcon(icon1)
        self.excluir_btn = QtWidgets.QPushButton("Excluir")
        self.excluir_btn.setStyleSheet("""QPushButton {font-size:17px;background-color: #ff0000;font-weight: bold;padding: 10px;border: none;}""")
        """ self.excluir_btn.setFixedWidth(120) """
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/images/delete-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.excluir_btn.setIcon(icon3)
        self.botoes_layout.addWidget(self.salvar_btn)
        self.botoes_layout.addWidget(self.cancelar_btn)
        self.botoes_layout.addWidget(self.excluir_btn)
        self.layout.addLayout(self.botoes_layout)
        self.horizontal_main_layout = QtWidgets.QHBoxLayout()
        self.tabela = QtWidgets.QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(["Nome", "ID", "Telefone", "Email", "Nascimento", "Observações"])
        self.tabela.setColumnHidden(1, True)
        self.tabela.setStyleSheet("""font-size:15px;""")
        self.tabela.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        self.tabela.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.horizontal_main_layout.addWidget(self.tabela)
        self.side_button_layout = QtWidgets.QVBoxLayout()
        self.side_button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.editar_btn = QtWidgets.QPushButton("Editar")
        self.editar_btn.setStyleSheet("""QPushButton {font-size:15px;background-color: #0000ff;font-weight: bold;padding: 10px;border: none;}""")
        self.editar_btn.setFixedWidth(120)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/images/edit-3-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.editar_btn.setIcon(icon2)
        
        self.print_btn = QtWidgets.QPushButton("")
        self.print_btn.setStyleSheet("""QPushButton {icon-size: 30px;font-size:15px;background-color: #d3d3d3;font-weight: bold;padding: 10px;border: none;}""")
        self.print_btn.setFixedWidth(70)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/images/print-svgrepo-com"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.print_btn.setIcon(icon5)
        self.side_button_layout.addWidget(self.editar_btn)
        self.side_button_layout.addStretch()
        self.side_button_layout.addWidget(self.print_btn)
        
        
        self.sair_btn_2 = QtWidgets.QPushButton("")
        self.sair_btn_2.setStyleSheet("""QPushButton {icon-size: 30px;background-color: #d3d3d3;font-weight: bold;padding: 10px;border: none;}""")
        self.sair_btn_2.setFixedWidth(70)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/images/exit-to-app-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.sair_btn_2.setIcon(icon4)
        self.side_button_layout.addWidget(self.editar_btn)
        self.side_button_layout.addWidget(self.sair_btn_2)
        self.horizontal_main_layout.addLayout(self.side_button_layout)
        self.layout.addLayout(self.horizontal_main_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.editar_btn.hide()
        self.excluir_btn.hide()
                
        """ desenvolvimento """
        self.salvar_btn.clicked.connect(lambda: self.execucao_segura(self.envia))
        self.excluir_btn.clicked.connect(lambda: self.execucao_segura(self.excluir))
        self.editar_btn.clicked.connect(lambda: self.execucao_segura(self.editar))
        self.cancelar_btn.clicked.connect(self.padrao)
        self.sair_btn_2.clicked.connect(self.sair)
        self.tabela.itemSelectionChanged.connect(self.verifica_selecao)  
        self.tabela.itemSelectionChanged.connect(self.highlight_selected_row)
        self.print_btn.clicked.connect(self.imprimir)
        
    config = configparser.ConfigParser()
    config.read("config.ini")
    userinfo = config["API"]
    userPort = userinfo['port']
    userEndpoint = userinfo['endpoint']
    token = os.environ['TOKEN']
    
    def token_db(self) :
        url_token = self.userEndpoint + 'token_db.php'
        response = requests.get(url_token)
        data = response.json()
        return data

    def validaToken(self) :
        try:
            token = os.getenv("TOKEN")
            if not token:
                return False

            decoded_bytes = base64.b64decode(token)
            decoded_str = decoded_bytes.decode('utf-8')
            dados = json.loads(decoded_str)

            exp = dados.get('exp')
            if exp is None or time.time() > exp:
                return False

            return True
        except Exception as e:
            print("Erro ao validar token:", e)
            return False
        

    
    """ def validaToken(self) :
        token = self.token
        token_dec = base64.b64decode(token)
        decoded_str = token_dec.decode("utf-8")        
        dados = json.loads(decoded_str)
        token_validado = False
        exp = dados['exp']
        if exp is None :
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('assets/images/image.png'))
            reply.setText("Token Inválido")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            x = reply.exec()
            print("token inválido")
            token_validado = False
        elif time.time() > exp :
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('assets/images/image.png'))
            reply.setText("Token Expirado, logue novamente")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            x = reply.exec()
            token_validado = False
        else :
            token_validado = True
            
        return token_validado """
    
    
    def execucao_segura(self, funcao):
        if self.validaToken():
            funcao()
        else:
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('assets/images/image.png'))
            reply.setText("Token Inválido ou expirado")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            reply.button(QMessageBox.StandardButton.Yes).setText("Sim")
            x = reply.exec()
            if x == QMessageBox.StandardButton.Yes:
                QtWidgets.QApplication.quit()
    
    def padrao(self):
        self.linha_nome.setText("")
        self.linha_telefone.setText("")
        self.linha_email.setText("")
        self.data_nasc.setDate(QDate(2000, 1, 1))
        self.linha_obs.setText("")
        self.salvar_btn.setText("Salvar")
        self.editar_btn.hide()
        self.excluir_btn.hide()

        try:
            self.salvar_btn.clicked.disconnect()
        except Exception:
            pass
        self.salvar_btn.clicked.connect(lambda: self.execucao_segura(self.envia))

    def listar(self):
        url = self.userEndpoint + 'listar.php'
        try:
            response = requests.get(url)
            dados = response.json()
        except Exception as e:
            print(f"Erro ao listar: {e}")
            dados = []
            
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
            self.tabela.setItem(linha, 0, QtWidgets.QTableWidgetItem(nome))
            self.tabela.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(id)))
            self.tabela.setItem(linha, 2, QtWidgets.QTableWidgetItem(telefone))
            self.tabela.setItem(linha, 3, QtWidgets.QTableWidgetItem(email))
            nascimento_ok = datetime.strptime(nascimento, "%Y-%m-%d").strftime("%d/%m/%Y")
            self.tabela.setItem(linha, 4, QtWidgets.QTableWidgetItem(nascimento_ok))
            self.tabela.setItem(linha, 5, QtWidgets.QTableWidgetItem(observacoes))
            
        self.padrao()
        self.token_db()
        fonte = QtGui.QFont()
        fonte.setPointSize(12)
        self.tabela.setFont(fonte)



    def envia(self):
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
            reply.button(QMessageBox.StandardButton.Yes).setText("Ok")
            x = reply.exec()
            return
        
        data = {
            'nome': texto_nome,
            'telefone': texto_telefone,
            'email': texto_email,
            'nascimento': self.data_nasc.date().toString('yyyy-MM-dd'),
            'observacoes': texto_observacoes
        }
        
        url = self.userEndpoint + 'insere.php'
        resposta = requests.post(url, json=data)
        
        if resposta.status_code == 200:
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('assets/images/image.png'))
            reply.setText("Contato adicionado com sucesso")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            reply.button(QMessageBox.StandardButton.Yes).setText("Ok")
            x = reply.exec()
            self.listar()
        else:
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('assets/images/image.png'))
            reply.setText("Preencha todos os campos!")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            reply.button(QMessageBox.StandardButton.Yes).setText("Ok")
            x = reply.exec()
            
        self.padrao()
        
        
    def verifica_selecao(self):
        linha = self.tabela.currentRow()
        selecionados = self.tabela.selectedItems()
        if selecionados:
            self.excluir_btn.show()
            self.editar()
        else:
            self.excluir_btn.hide()
            self.padrao()
    
    def highlight_selected_row(self):
        self.tabela.setStyleSheet("""
    QTableWidget::item { 
        font-size:15px; 
        padding: 6px;}
    QTableWidget::item:selected { 
        background-color: lightblue; 
        color: black; 
        font-size:15px;
        padding: 6px;}
    """)
    
    def excluir(self) :
        url_delete = self.userEndpoint + 'delete.php'
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
            reply.button(QMessageBox.StandardButton.Yes).setText("Sim")
            reply.button(QMessageBox.StandardButton.No).setText("Não")
            x = reply.exec()
            
            if x == QMessageBox.StandardButton.Yes:
                self.tabela.removeRow(linha)
                response = requests.delete(url_delete,  json=data)
        else:
            print("Nenhuma linha selecionada.")

    def editar(self):
        linha = self.tabela.currentRow()
        if linha < 0:
            QMessageBox.warning(None, "Agenda de Contatos", "Nenhuma linha selecionada.")
            return

        self.salvar_btn.setText("Atualizar")

        item_id = self.tabela.item(linha, 1).text()
        self.linha_nome.setText(self.tabela.item(linha, 0).text())
        self.linha_telefone.setText(self.tabela.item(linha, 2).text())
        self.linha_email.setText(self.tabela.item(linha, 3).text())
        self.linha_obs.setText(self.tabela.item(linha, 5).text())

        data_str = self.tabela.item(linha, 4).text()
        nascimento_ok = datetime.strptime(data_str,"%d/%m/%Y" ).strftime("%Y-%m-%d")
        qdate = QDate.fromString(nascimento_ok, "yyyy-MM-dd")
        self.data_nasc.setDate(qdate)

        try:
            self.salvar_btn.clicked.disconnect()
        except Exception:
            pass

        self.salvar_btn.clicked.connect(lambda: self.atualiza(item_id))
        self.salvar_btn.clicked.connect(lambda: self.execucao_segura(self.atualiza))
        fonte = QtGui.QFont()
        fonte.setPointSize(12)
        self.tabela.setFont(fonte)
        

    def atualiza(self, item_id):
        dados_ok = {
            'id': item_id,
            'nome': self.linha_nome.text(),
            'telefone': self.linha_telefone.text(),
            'email': self.linha_email.text(),
            'nascimento': self.data_nasc.date().toString('yyyy-MM-dd'),
            'observacoes': self.linha_obs.text()
        }

        url = self.userEndpoint + 'edita.php'
        resposta = requests.post(url, json=dados_ok)

        if resposta.status_code == 200:
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('assets/images/image.png'))
            reply.setText("Contato editado com sucesso")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            reply.button(QMessageBox.StandardButton.Yes).setText("Sim")
            x = reply.exec()
            self.listar()
        else:
            QMessageBox.warning(None, "Agenda de Contatos", "Erro ao atualizar contato")

        self.salvar_btn.setText("Salvar")
        self.padrao()

    def imprimir(self):
        from imprimir import Ui_MainWindow as ImprimirWindow
        self.window_imprimir = QtWidgets.QMainWindow()
        self.ui_imprimir = ImprimirWindow()
        self.ui_imprimir.setupUi(self.window_imprimir)
        self.window_imprimir.showMaximized()
        self.centralwidget.parent().close()


    def sair(self):
        reply = QMessageBox()
        reply.setWindowTitle("Agenda de Contatos")
        reply.setWindowIcon(QIcon('assets/images/image.png'))
        reply.setText("Deseja sair da agenda de contatos?")
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | 
                 QMessageBox.StandardButton.No)
        reply.button(QMessageBox.StandardButton.Yes).setText("Sim")
        reply.button(QMessageBox.StandardButton.No).setText("Não")

        x = reply.exec()
        
        if x == QMessageBox.StandardButton.Yes:
            QtWidgets.QApplication.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    ui.listar()
    sys.exit(app.exec())
