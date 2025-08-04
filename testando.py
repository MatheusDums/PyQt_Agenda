from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: #ffffff;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(50, 30, 50, 30)
        self.layout.setSpacing(15)
        self.title_label = QtWidgets.QLabel("Agenda de Contatos")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font: 20pt 'Segoe Print';")
        self.layout.addWidget(self.title_label)
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
        self.botoes_layout = QtWidgets.QHBoxLayout()
        self.salvar_btn = QtWidgets.QPushButton("Salvar")
        self.salvar_btn.setStyleSheet("""
            QPushButton {
                background-color: #00ff00;
                font-weight: bold;
                padding: 10px;
                border: none;
            }
        """)
        self.cancelar_btn = QtWidgets.QPushButton("Cancelar")
        self.cancelar_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff0000;
                color: black;
                font-weight: bold;
                padding: 10px;
                border: none;
            }
        """)
        self.botoes_layout.addWidget(self.salvar_btn)
        self.botoes_layout.addWidget(self.cancelar_btn)
        self.layout.addLayout(self.botoes_layout)
        self.horizontal_main_layout = QtWidgets.QHBoxLayout()
        self.tabela = QtWidgets.QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(["Nome", "ID", "Telefone", "Email", "Nascimento", "Observações"])
        self.tabela.setColumnHidden(1, True)
        self.tabela.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        self.tabela.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.horizontal_main_layout.addWidget(self.tabela)
        self.side_button_layout = QtWidgets.QVBoxLayout()
        self.side_button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.editar_btn = QtWidgets.QPushButton("Editar")
        self.editar_btn.setStyleSheet("""
            QPushButton {
                background-color: #0000ff;
                color: white;
                font-weight: bold;
                padding: 10px;
                border: none;
            }
        """)
        self.editar_btn.setFixedWidth(120)
        self.excluir_btn = QtWidgets.QPushButton("Excluir")
        self.excluir_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff0000;
                color: white;
                font-weight: bold;
                padding: 10px;
                border: none;
            }
        """)
        self.excluir_btn.setFixedWidth(120)
        self.sair_btn_2 = QtWidgets.QPushButton("Sair")
        self.sair_btn_2.setStyleSheet("""
            QPushButton {
                background-color: #444444;
                color: white;
                font-weight: bold;
                padding: 10px;
                border: none;
            }
        """)
        self.sair_btn_2.setFixedWidth(120)
        self.side_button_layout.addWidget(self.editar_btn)
        self.side_button_layout.addWidget(self.excluir_btn)
        self.side_button_layout.addStretch()
        self.side_button_layout.addWidget(self.sair_btn_2)
        self.horizontal_main_layout.addLayout(self.side_button_layout)
        self.layout.addLayout(self.horizontal_main_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.editar_btn.hide()
        self.excluir_btn.hide()
        
        """ desenvolvimento """
        self.salvar_btn.clicked.connect(self.envia)
        self.cancelar_btn.clicked.connect(self.padrao)
        self.editar_btn.clicked.connect(self.editar)
        self.excluir_btn.clicked.connect(self.excluir)
        self.sair_btn_2.clicked.connect(self.sair)
        self.tabela.itemSelectionChanged.connect(self.verifica_selecao)
        
        
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
        self.salvar_btn.clicked.connect(self.envia)

    def listar(self):
        url = 'http://localhost/pyqt_agenda/php/api/listar.php'
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
            self.tabela.setItem(linha, 4, QtWidgets.QTableWidgetItem(nascimento))
            self.tabela.setItem(linha, 5, QtWidgets.QTableWidgetItem(observacoes))

        self.padrao()

    def envia(self):
        texto_nome = self.linha_nome.text()
        texto_telefone = self.linha_telefone.text()
        texto_email = self.linha_email.text()
        texto_observacoes = self.linha_obs.text()

        if not texto_nome or not texto_email or not texto_telefone or not texto_observacoes:
            QMessageBox.information(None, "Agenda de Contatos", "Preencha todos os campos!")
            return

        data = {
            'nome': texto_nome,
            'telefone': texto_telefone,
            'email': texto_email,
            'nascimento': self.data_nasc.date().toString('dd-MM-yyyy'),
            'observacoes': texto_observacoes
        }

        url = 'http://localhost/pyqt_agenda/php/api/insere.php'
        resposta = requests.post(url, json=data)

        if resposta.status_code == 200:
            QMessageBox.information(None, "Agenda de Contatos", "Contato adicionado com sucesso")
            self.listar()
        else:
            QMessageBox.warning(None, "Agenda de Contatos", "Erro ao adicionar contato")

        self.padrao()

    def verifica_selecao(self):
        selecionados = self.tabela.selectedItems()
        if selecionados:
            self.editar_btn.show()
            self.excluir_btn.show()
        else:
            self.editar_btn.hide()
            self.excluir_btn.hide()

    def excluir(self):
        linha = self.tabela.currentRow()
        if linha < 0:
            QMessageBox.warning(None, "Agenda de Contatos", "Nenhuma linha selecionada.")
            return

        item_id = self.tabela.item(linha, 1).text()
        resposta = QMessageBox.question(None, "Agenda de Contatos", "Deseja apagar o contato?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if resposta == QMessageBox.StandardButton.Yes:
            url_delete = 'http://localhost/pyqt_agenda/php/api/delete.php'
            data = {'id': item_id}
            try:
                response = requests.delete(url_delete, json=data)
                if response.status_code == 200:
                    self.tabela.removeRow(linha)
                    QMessageBox.information(None, "Agenda de Contatos", "Contato removido com sucesso")
                else:
                    QMessageBox.warning(None, "Agenda de Contatos", "Erro ao remover contato")
            except Exception as e:
                QMessageBox.warning(None, "Agenda de Contatos", f"Erro: {e}")

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
        qdate = QDate.fromString(data_str, "dd-MM-yyyy")
        if not qdate.isValid():
            qdate = QDate(2000, 1, 1)
        self.data_nasc.setDate(qdate)

        try:
            self.salvar_btn.clicked.disconnect()
        except Exception:
            pass

        self.salvar_btn.clicked.connect(lambda: self.atualiza(item_id))

    def atualiza(self, item_id):
        dados_ok = {
            'id': item_id,
            'nome': self.linha_nome.text(),
            'telefone': self.linha_telefone.text(),
            'email': self.linha_email.text(),
            'nascimento': self.data_nasc.date().toString('dd-MM-yyyy'),
            'observacoes': self.linha_obs.text()
        }

        url = 'http://localhost/pyqt_agenda/php/api/edita.php'
        resposta = requests.post(url, json=dados_ok)

        if resposta.status_code == 200:
            QMessageBox.information(None, "Agenda de Contatos", "Contato atualizado com sucesso")
            self.listar()
        else:
            QMessageBox.warning(None, "Agenda de Contatos", "Erro ao atualizar contato")

        self.salvar_btn.setText("Salvar")
        self.padrao()

    def sair(self):
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
