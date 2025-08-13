""" servers = [ 
        "localhost:3306" 
        ]

for server in servers:
    try:
        host, port = server.split(":")
        port = int(port)
        socket.create_connection((host, port), 3)
        print(server, "OK")
    except:
        print(server, "FAIL") """
        
        
import socket
import configparser

config = configparser.ConfigParser()

config['API'] = {
    'Port' : '3306',
    'EndPoint' : 'http://localhost/pyqt_agenda/php/api/'
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)