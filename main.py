import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import os
from winotify import Notification

app = QtWidgets.QApplication(sys.argv)
if not(os.path.exists("config.ini")):
    notificacao = Notification(app_id="Agenda de Contatos", title="Notificação de erro",
                            msg="Agenda de contatos não contém o arquivo 'Config.ini', entre em contato com a TI.",
                            duration="short", icon="C://xampp/htdocs/pyqt_agenda/assets/images/icone.ico")
    notificacao.add_actions(label="Abrir HelpDesk", launch="https://hydra.buddemeyer.com.br/help_desk/")
    notificacao.show()
    sys.exit()
else :
    from login_ok import Ui_Tela1
    window_login = QtWidgets.QMainWindow()
    ui_login = Ui_Tela1()
    ui_login.setupUi(window_login)
    window_login.showMaximized()
    
sys.exit(app.exec())