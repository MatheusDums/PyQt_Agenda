from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon, QColor
from PyQt6.QtWidgets import QMessageBox, QAbstractItemView
from PyQt6.QtCore import QDate, Qt, QSize
import base64
import codecs
import subprocess
import os
import requests
import shutil
from datetime import datetime
import configparser
import time
import json
import serial
from serial.tools import list_ports
import re
import func_timeout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()
        MainWindow.setStyleSheet("background-color: white;")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: white;")

        self.layout_principal = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout_principal.setContentsMargins(10, 10, 10, 10)
        self.layout_principal.setSpacing(10)

        self.frame_titulo = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_titulo.setStyleSheet("background-color: white;")
        self.layout_titulo = QtWidgets.QHBoxLayout(self.frame_titulo)
        self.titulo = QtWidgets.QLabel(parent=self.frame_titulo)
        font = QtGui.QFont("Dubai", 30)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titulo.setStyleSheet("background-color: white;")
        self.layout_titulo.addWidget(self.titulo)
        self.layout_principal.addWidget(self.frame_titulo)

        self.frame_principal = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_principal.setStyleSheet("background-color: white;")
        self.layout_frame_principal = QtWidgets.QVBoxLayout(self.frame_principal)
        self.layout_frame_principal.setSpacing(10)

        self.label_code = QtWidgets.QLabel("Código da Etiqueta", parent=self.frame_principal)
        self.label_code.setFont(QtGui.QFont("Dubai", 15))
        self.layout_frame_principal.addWidget(self.label_code)
        self.linha_code = QtWidgets.QTextEdit(parent=self.frame_principal)
        self.linha_code.setFont(QtGui.QFont("Dubai", 20))
        self.linha_code.setFixedHeight(45)
        self.layout_frame_principal.addWidget(self.linha_code)

        self.label_qtd = QtWidgets.QLabel("Quantidade de etiquetas para imprimir", parent=self.frame_principal)
        self.label_qtd.setFont(QtGui.QFont("Dubai", 15))
        self.layout_frame_principal.addWidget(self.label_qtd)
        self.linha_qtd = QtWidgets.QTextEdit(parent=self.frame_principal)
        self.linha_qtd.setFont(QtGui.QFont("Dubai", 20))
        self.linha_qtd.setFixedHeight(45)
        self.layout_frame_principal.addWidget(self.linha_qtd)
        
        self.label_peso = QtWidgets.QLabel("Peso", parent=self.frame_principal)
        self.label_peso.setFont(QtGui.QFont("Dubai", 15))
        self.layout_frame_principal.addWidget(self.label_peso)
        self.linha_peso = QtWidgets.QTextEdit(parent=self.frame_principal)
        self.linha_peso.setFont(QtGui.QFont("Dubai", 20))
        self.linha_peso.setFixedHeight(45)
        self.layout_frame_principal.addWidget(self.linha_peso)

        self.layout_botoes = QtWidgets.QHBoxLayout()
        self.cancelar_btn = QtWidgets.QPushButton(parent=self.frame_principal)
        self.cancelar_btn.setIcon(QIcon("./assets/images/cancel-svgrepo-com.svg"))
        self.cancelar_btn.setText("  Cancelar")
        self.cancelar_btn.setIconSize(QSize(26, 26))
        self.cancelar_btn.setStyleSheet("background-color: #ff7f05; color: black; font-size: 18pt; border-radius: 0px;")
        self.cancelar_btn.setMinimumHeight(40)
        self.layout_botoes.addWidget(self.cancelar_btn)
        self.imprimir_btn = QtWidgets.QPushButton(parent=self.frame_principal)
        self.imprimir_btn.setIcon(QIcon("./assets/images/print-svgrepo-com.svg"))
        self.imprimir_btn.setText("  Imprimir")
        self.imprimir_btn.setIconSize(QSize(26, 26))
        self.imprimir_btn.setStyleSheet("background-color: #009417; color: black; font-size: 18pt; border-radius: 0px;")
        self.imprimir_btn.setMinimumHeight(40)
        self.layout_botoes.addWidget(self.imprimir_btn)
        self.layout_frame_principal.addLayout(self.layout_botoes)

        self.layout_principal.addWidget(self.frame_principal)

        self.frame_table = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_table.setStyleSheet("background-color: white;")
        self.layout_frame_table = QtWidgets.QHBoxLayout(self.frame_table)
        self.layout_frame_table.setSpacing(10)

        self.tabela_layout = QtWidgets.QVBoxLayout()
        self.tabela_label = QtWidgets.QLabel("Registro de impressões", parent=self.frame_table)
        self.tabela_label.setFont(QtGui.QFont("Dubai", 15))
        self.tabela_layout.addWidget(self.tabela_label)
        self.tabela = QtWidgets.QTableWidget(parent=self.frame_table)
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["Código", "Quantidade", "Peso"])
        self.tabela.horizontalHeader().setStretchLastSection(False)
        self.tabela.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tabela.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tabela.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tabela.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.tabela_layout.addWidget(self.tabela)
        self.layout_frame_table.addLayout(self.tabela_layout)

        self.layout_lateral = QtWidgets.QVBoxLayout()
        self.layout_lateral.addStretch(2)
        self.voltar_btn = QtWidgets.QPushButton(parent=self.frame_table)
        self.voltar_btn.setMinimumSize(QSize(220, 60))
        self.voltar_btn.setIcon(QIcon("./assets/images/contact-book-2-svgrepo-com.svg"))
        self.voltar_btn.setText("  Voltar para a Agenda")
        self.voltar_btn.setIconSize(QSize(27, 27))
        self.voltar_btn.setStyleSheet("background-color: #BCC1AC; color: black; font-size: 14pt;border-radius: 0px; padding: 0px 25px;")
        self.sair_btn = QtWidgets.QPushButton(parent=self.frame_table)
        self.sair_btn.setMinimumSize(QSize(220, 60))
        self.sair_btn.setText("  Sair")
        self.sair_btn.setIcon(QIcon("./assets/images/exit-to-app-svgrepo-com.svg"))
        self.sair_btn.setIconSize(QSize(27, 27))
        self.sair_btn.setStyleSheet("background-color: #FF0000; color: black; font-size: 14pt; border-radius: 0px;")
        self.layout_lateral.addWidget(self.voltar_btn)
        self.layout_lateral.addWidget(self.sair_btn)
        self.layout_lateral.addStretch(1)
        self.layout_frame_table.addLayout(self.layout_lateral)

        self.layout_principal.addWidget(self.frame_table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.peso_atual = ""


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Impressão de etiquetas")
        MainWindow.setWindowIcon(QIcon("./assets/images/image.png"))
        self.titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Impressão de Etiquetas</p></body></html>"))
        self.label_code.setText(_translate("MainWindow", "Código da Etiqueta"))
        self.label_qtd.setText(_translate("MainWindow", "Quantidade de etiquetas para imprimir"))
        self.linha_qtd.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Dubai\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cancelar_btn.setText(_translate("MainWindow", "Cancelar"))
        self.imprimir_btn.setText(_translate("MainWindow", "Imprimir"))
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantidade"))
        item = self.tabela.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Peso"))
        self.tabela_label.setText(_translate("MainWindow", "Registro de impressões"))


        """ desenvolvimento """
        self.sair_btn.clicked.connect(lambda: self.execucao_segura(self.sair))
        self.imprimir_btn.clicked.connect(lambda: self.execucao_segura(self.etiquetas))
        self.voltar_btn.clicked.connect(lambda: self.execucao_segura(self.voltar))
        self.cancelar_btn.clicked.connect(lambda: self.execucao_segura(self.padrao))
        
    config = configparser.ConfigParser()
    config.read("config.ini")
    userinfo = config["API"]
    userPort = userinfo['port']
    userEndpoint = userinfo['endpoint']
    
    """  mapeamento """
    #### Mapeamento da Impressora Zebra na porta LPT1 ####
    comp_impzebra = config['IMPZEBRA']['nomecompartilhamento']
        
    # Executa o comando no CMD
    subprocess.run('cd \\', shell=True)
    subprocess.run('NET USE LPT1 /DELETE', shell=True)
    subprocess.run("NET USE LPT1 \\\\127.0.0.1\\" + comp_impzebra + " /PERSISTENT:YES", shell=True)   
    
        #parte de peso
    def testar_balanca():
            
        def configurar_porta_serial(porta, vltransmissao, bits_dados, paridade, bits_parada):
            try:
                serial_conn = serial.Serial(
                    port=porta,
                    baudrate=vltransmissao,
                    bytesize=bits_dados,
                    parity=serial.PARITY_NONE if not paridade else getattr(serial, f"PARITY_{paridade.upper()}", serial.PARITY_NONE),
                    stopbits=bits_parada,
                    timeout=1
                )
                print(f"Porta {porta} configurada com sucesso.")
                return serial_conn
            except serial.SerialException as e:
                print(f"Erro ao configurar a porta serial: {e}")
                return None

        def extrair_peso(str_receive):
            """
            Extrai o peso do dado recebido da balança no formato esperado.
            Exemplo: b'\x02;0 000673000000' retorna "673".
            """
            #print(f"Recebido: {str_receive}")
            if not str_receive:
                return None
            try:
                texto = str_receive.decode("utf-8", errors="ignore").strip()
                match = re.search(r'(\d{2})(\d{3})', texto)
                """ print(f"Texto: ", texto)
                print(f"match: ", match) """
                if match:
                    parte_inteira = match.group(1).lstrip("0") or "0"
                    parte_decimal = match.group(2)
                    # peso_formatado = f"{int(parte_inteira)}.{parte_decimal}".replace(".", ",")
                    peso_formatado = f"{parte_inteira}.{parte_decimal}"
                    #print(f"formatado: ", peso_formatado)
                    return peso_formatado
            except Exception as e:
                print(f"Erro ao extrair peso: {e}")
            return None
        """
        Testa a leitura da balança, exibe os dados no console e salva em um arquivo .txt.
        """
        # Configurações da balança (substitua pelos valores reais)
        porta = "COM3"  # Substitua pela porta correta
        vltransmissao = 9600
        bits_dados = 8
        paridade = "N"
        bits_parada = 1

        # Configurar a porta serial
        serial_conn = configurar_porta_serial(porta, vltransmissao, bits_dados, paridade, bits_parada)
        if not serial_conn:
            return

        # Define o caminho do arquivo de log na pasta raiz
        log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "leituras_balanca.txt")
        try:
            print("Iniciando leitura da balança. Pressione Ctrl+C para parar.")
            peso = ""
            while True:
                leitura = serial_conn.read_until(b'\n').strip() # Lê até encontrar uma nova linha
                #print(f"Dados brutos recebidos: {leitura}")  # Exibe os dados brutos recebidos
                    
                # Salva os dados brutos no arquivo de log
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(f"{leitura.decode('utf-8', errors='ignore').strip()}\n")
                
                peso = extrair_peso(leitura)
                #print(peso)
                if peso:
                    print(f"Peso lido: {peso}")
                else:
                    print("Peso inválido ou não detectado.")
                return peso
                
        except KeyboardInterrupt:
            print("Leitura interrompida pelo usuário.")
        except Exception as e:
            print(f"Erro durante a leitura: {e}")
        finally:
            if serial_conn and serial_conn.is_open:
                serial_conn.close()
                print("Conexão serial fechada.")      
        #fim da parte de peso
    os.environ["PESO"] = testar_balanca()
    
    peso_ok = os.getenv("PESO")
    print(f"Peso Atual: {peso_ok}")
    
    def etiquetas(self):          
        print(f"Peso atual: {self.peso_atual}")
        
        codigo = self.linha_code.toPlainText()
        
        dados_codigo = {
            'codigo': codigo
        }
        url_codigo = self.userEndpoint + "buscaEtiqueta.php"
        envia = requests.post(url_codigo, json=dados_codigo)
        dados = envia.json()
        
        if not dados:
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('./assets/images/image.png'))
            reply.setText("Nenhum registro encontrado com esse código.")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            reply.button(QMessageBox.StandardButton.Yes).setText("Sim")
            x = reply.exec()
            return
        
        id = dados[0]['pyt_id']
        codigo = dados[0]['pyt_telefone']
        
        """ parte de quantidade """
        quantidade = self.linha_qtd.toPlainText()
        
        
        if not quantidade.isdigit() or int(quantidade) <= 0:
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('./assets/images/image.png'))
            reply.setText("Quantidade inválida. Por favor, insira o número de cópias que deseja imprimir.")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            reply.button(QMessageBox.StandardButton.Yes).setText("Sim")
            x = reply.exec()
            return
        valorqtd = int(quantidade)
        reply = QMessageBox()
        reply.setWindowTitle("Agenda de Contatos")
        reply.setWindowIcon(QIcon('./assets/images/image.png'))
        reply.setText(f"Deseja imprimir {valorqtd} cópias da etiqueta {codigo} ?")
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | 
                 QMessageBox.StandardButton.No)
        reply.button(QMessageBox.StandardButton.Yes).setText("Sim")
        reply.button(QMessageBox.StandardButton.No).setText("Não")
        x = reply.exec()
        
        if x == QMessageBox.StandardButton.Yes:
            config_etq_pesagem = 'etiquetas/etiqueta.prn'
            with open(config_etq_pesagem, 'r', encoding='utf-8') as arquivo:
                # Leia as linhas do arquivo e armazene em uma lista
                linhas = arquivo.readlines()
            
            # Percorra cada linha e substitua os marcadores pelas variáveis
            for i in range(len(linhas)):
                nascimento = dados[0]['pyt_nascimento']
                linhas[i] = linhas[i].replace('%nome%', dados[0]['pyt_nome'])
                linhas[i] = linhas[i].replace('%telefone%', dados[0]['pyt_telefone'])
                """ linhas[i] = linhas[i].replace('%peso%', peso) """
                linhas[i] = linhas[i].replace('%email%', dados[0]['pyt_email'])
                nascimento_ok = datetime.strptime(nascimento, "%Y-%m-%d").strftime("%d/%m/%Y")
                linhas[i] = linhas[i].replace('%nasc%', nascimento_ok)
                linhas[i] = linhas[i].replace('%observacoes%', dados[0]['pyt_observacoes'])

            # Concatenar as linhas em uma única string
            codigo_zpl = ''.join(linhas)

            # Criar um arquivo temporário com o código ZPL
            temp_file = 'temp.zpl'
            with codecs.open(temp_file, 'w', 'utf-8') as temp:
                temp.write(codigo_zpl)

            # Enviar o arquivo para a impressora Zebra na porta LPT1
            """ while (valorqtd > 0):
                shutil.copyfile(temp_file, "LPT1")
                valorqtd = valorqtd - 1 """

            # Remover o arquivo temporário
            """ os.remove(temp_file) """
            
            nova_linha = self.tabela.rowCount()
            self.tabela.insertRow(nova_linha)
            self.tabela.setItem(nova_linha, 0, QtWidgets.QTableWidgetItem(codigo) )
            self.tabela.setItem(nova_linha, 1, QtWidgets.QTableWidgetItem(quantidade))
            """ self.tabela.setItem(nova_linha, 2, QtWidgets.QTableWidgetItem(peso)) """
            
            self.padrao()
            self.token_db()


    def voltar(self):
        from testando import Ui_MainWindow as TestandoWindow
        self.window_principal = QtWidgets.QMainWindow()
        self.ui_principal = TestandoWindow()
        self.ui_principal.setupUi(self.window_principal)
        self.ui_principal.listar()
        self.window_principal.showMaximized()
        self.centralwidget.parent().close()


    def padrao(self):
        self.linha_code.setText("")
        self.linha_qtd.setText("")
        self.linha_peso.setText("")


    def sair(self):
        reply = QMessageBox()
        reply.setWindowTitle("Agenda de Contatos")
        reply.setWindowIcon(QIcon('assets/images/image.png'))
        reply.setText("Deseja sair da Impressão de Etiquetas?")
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | 
                 QMessageBox.StandardButton.No)
        reply.button(QMessageBox.StandardButton.Yes).setText("Sim")
        reply.button(QMessageBox.StandardButton.No).setText("Não")

        x = reply.exec()
        
        if x == QMessageBox.StandardButton.Yes:
            QtWidgets.QApplication.quit()

    """ parte de token """
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())