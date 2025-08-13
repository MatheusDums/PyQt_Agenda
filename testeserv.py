""" import psutil
def verificar_portas():
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == psutil.CONN_LISTEN:
            print(f"Porta {conn.laddr.port} ({conn.type}) está ouvindo em {conn.laddr.ip}:{conn.laddr.port}")
if __name__ == "__main__":
    verificar_portas() """
    
import configparser
config_reader = configparser.ConfigParser()

config_reader.read('application.ini')

print(config_reader.sections())

print(config_reader['Default']['port'])