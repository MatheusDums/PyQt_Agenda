import requests
import configparser
from configparser import ConfigParser

config = configparser.ConfigParser()
config.read("config.ini")
userinfo = config["API"]
userPort = userinfo['port']
userEndpoint = userinfo['endpoint']

url = userEndpoint + "etiquetas.php"
res = requests.get(url)
dados = res.json()


largura = int(59 * 8)
altura = int(81 * 8)


for r in dados:
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
    
print("etiqueta salva")

""" ^FO100,580^FD{r['col1']} {r['col2']}    Tear {r['tear']}^FS """