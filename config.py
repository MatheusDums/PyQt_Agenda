""" import configparser

config = configparser.ConfigParser() """

import socket

servers = [ 
        "localhost:3306" 
        ]

for server in servers:
    try:
        host, port = server.split(":")
        port = int(port)
        socket.create_connection((host, port), 3)
        print(server, "OK")
    except:
        print(server, "FAIL")