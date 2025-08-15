import configparser

""" cria o config.ini """
config = configparser.ConfigParser()

config['API'] = {
    'Port' : '3306',
    'EndPoint' : 'http://localhost/pyqt_agenda/php/api/'
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)

""" ler o config.ini """
config.read("config.ini")
userinfo = config["API"]

print(f'a porta é {userinfo['port']}')