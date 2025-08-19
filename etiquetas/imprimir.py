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
        MainWindow.resize(752, 558)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_titulo = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_titulo.setGeometry(QtCore.QRect(-20, -1, 821, 101))
        self.frame_titulo.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame_titulo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_titulo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_titulo.setObjectName("frame_titulo")
        self.titulo = QtWidgets.QLabel(parent=self.frame_titulo)
        self.titulo.setGeometry(QtCore.QRect(20, 0, 751, 101))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(30)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")
        self.frame_principal = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_principal.setGeometry(QtCore.QRect(0, 100, 751, 251))
        self.frame_principal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_principal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_principal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_principal.setObjectName("frame_principal")
        self.label_code = QtWidgets.QLabel(parent=self.frame_principal)
        self.label_code.setGeometry(QtCore.QRect(10, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.label_code.setFont(font)
        self.label_code.setObjectName("label_code")
        self.linha_code = QtWidgets.QTextEdit(parent=self.frame_principal)
        self.linha_code.setGeometry(QtCore.QRect(10, 30, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(18)
        self.linha_code.setFont(font)
        self.linha_code.setObjectName("linha_code")
        self.label_qtd = QtWidgets.QLabel(parent=self.frame_principal)
        self.label_qtd.setGeometry(QtCore.QRect(10, 100, 321, 16))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.label_qtd.setFont(font)
        self.label_qtd.setObjectName("label_qtd")
        self.linha_qtd = QtWidgets.QTextEdit(parent=self.frame_principal)
        self.linha_qtd.setGeometry(QtCore.QRect(10, 130, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(18)
        self.linha_qtd.setFont(font)
        self.linha_qtd.setObjectName("linha_qtd")
        self.cancelar_btn = QtWidgets.QPushButton(parent=self.frame_principal)
        self.cancelar_btn.setGeometry(QtCore.QRect(10, 190, 351, 41))
        self.cancelar_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.cancelar_btn.setObjectName("cancelar_btn")
        self.imprimir_btn = QtWidgets.QPushButton(parent=self.frame_principal)
        self.imprimir_btn.setGeometry(QtCore.QRect(380, 190, 341, 41))
        self.imprimir_btn.setStyleSheet("background-color: #009417;\n"
"color: rgb(255, 255, 255);")
        self.imprimir_btn.setObjectName("imprimir_btn")
        self.frame_table = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_table.setGeometry(QtCore.QRect(0, 350, 751, 191))
        self.frame_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_table.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_table.setObjectName("frame_table")
        self.tabela = QtWidgets.QTableWidget(parent=self.frame_table)
        self.tabela.setGeometry(QtCore.QRect(10, 30, 681, 151))
        self.tabela.setMinimumSize(QtCore.QSize(681, 0))
        self.tabela.setBaseSize(QtCore.QSize(0, 0))
        self.tabela.setLineWidth(1)
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(2)
        self.tabela.setColumnWidth(0,339)
        self.tabela.setColumnWidth(1,339)
        self.tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        item.setFont(font)
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(10)
        item.setFont(font)
        self.tabela.setHorizontalHeaderItem(1, item)
        self.tabela_label = QtWidgets.QLabel(parent=self.frame_table)
        self.tabela_label.setGeometry(QtCore.QRect(10, 10, 321, 16))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.tabela_label.setFont(font)
        self.tabela_label.setObjectName("tabela_label")
        self.sair_btn = QtWidgets.QPushButton(parent=self.frame_table)
        self.sair_btn.setGeometry(QtCore.QRect(700, 140, 41, 41))
        self.sair_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../xampp/htdocs/pyqt_agenda/assets/images/exit-to-app-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.sair_btn.setIcon(icon)
        self.sair_btn.setObjectName("sair_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.tabela_label.setText(_translate("MainWindow", "Registro de impressões"))


        """ desenvolvimento """
        self.sair_btn.clicked.connect(self.sair)
        self.imprimir_btn.clicked.connect(self.etiquetas)
        
    config = configparser.ConfigParser()
    config.read("config.ini")
    userinfo = config["API"]
    userPort = userinfo['port']
    userEndpoint = userinfo['endpoint']
        
    def etiquetas(self):
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
        print(quantidade)
        if not quantidade.isdigit() or int(quantidade) <= 0:
            reply = QMessageBox()
            reply.setWindowTitle("Agenda de Contatos")
            reply.setWindowIcon(QIcon('./assets/images/image.png'))
            reply.setText("Quantidade inválida. Por favor, insira o número de cópias que deseja imprimir.")
            reply.setStandardButtons(QMessageBox.StandardButton.Yes)
            reply.button(QMessageBox.StandardButton.Yes).setText("Sim")
            x = reply.exec()
            return
        
        for r in dados:
            largura = int(59 * 8)
            altura = int(81 * 8)
            zpl = f"""
        ^XA

        ^PW{largura}
        ^LL{altura}
        ^FS

        ^CF0,25

        ^FO30,30^BXN,6,200
        ^FD{dados[0]['pyt_telefone']}^FS

        ^FO370,30^BXN,6,200
        ^FD{dados[0]['pyt_telefone']}^FS

        ^FO30,150^BXN,6,200
        ^FD{dados[0]['pyt_telefone']}^FS

        ^FO370,150^BXN,6, 200
        ^FD{dados[0]['pyt_telefone']}^FS

        ^FO30,270^BXN,6,200
        ^FD{dados[0]['pyt_telefone']}^FS

        ^FO370,270^BXN,6, 200
        ^FD{dados[0]['pyt_telefone']}^FS

        ^FO135,100^BXN,15,200
        ^FD{dados[0]['pyt_telefone']}^FS

        ^CF0,50
        ^FO110,380^FD{dados[0]['pyt_telefone']}^FS

        ^FO30,435^GB420,50,3^FS
        ^CF0,30
        ^FO40,450^FD{dados[0]['pyt_nome']}^FS

        ^FO30,482^GB420,50,3^FS
        ^CF0,30
        ^FO40,495^FD{dados[0]['pyt_telefone']}   |  {dados[0]['pyt_nascimento']}^FS

        ^FO30,529^GB420,50,3^FS
        ^CF0,30
        ^FO40,540^FD{dados[0]['pyt_email']}^FS

        ^FO30,576^GB420,50,3^FS
        ^CF0,30
        ^FO40,590^FD{dados[0]['pyt_observacoes']}^FS


        ^XZ
        """

        with open(f"etiquetas/etiqueta.zpl", "w") as f:
            f.write(zpl)
        
        reply = QMessageBox()
        reply.setWindowTitle("Agenda de Contatos")
        reply.setWindowIcon(QIcon('./assets/images/image.png'))
        reply.setText(f"Deseja imprimir a etiqueta {codigo} ?")
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | 
                 QMessageBox.StandardButton.No)
        reply.button(QMessageBox.StandardButton.Yes).setText("Sim")
        reply.button(QMessageBox.StandardButton.No).setText("Não")
        x = reply.exec()
        
        


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
    MainWindow.show()
    sys.exit(app.exec())
