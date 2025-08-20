import subprocess
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

#### Mapeamento da Impressora Zebra na porta LPT1 ####
comp_impzebra = config['IMPZEBRA']['nomecompartilhamento']

print(comp_impzebra)

# Executa o comando no CMD
subprocess.run('cd \\', shell=True)
subprocess.run('NET USE LPT1 /DELETE', shell=True)
subprocess.run('NET USE LPT1 \\\\127.0.0.1\\' + comp_impzebra + ' /PERSISTENT:YES', shell=True)