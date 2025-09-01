import serial
from serial.tools import list_ports
import re
import os


def configurar_porta_serial(porta, vltransmissao, bits_dados, paridade, bits_parada):
    """
    Configura a porta serial com os parâmetros fornecidos.
    """
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
        print(f"Texto: ", texto)
        print(f"match: ", match)
        if match:
            parte_inteira = match.group(1).lstrip("0") or "0"
            parte_decimal = match.group(2)
            # peso_formatado = f"{int(parte_inteira)}.{parte_decimal}".replace(".", ",")
            peso_formatado = f"{parte_inteira}.{parte_decimal}"
            print(f"formatado: ", peso_formatado)
            return peso_formatado
    except Exception as e:
        print(f"Erro ao extrair peso: {e}")
    return None

def testar_balanca():
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
    """ log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "leituras_balanca.txt") """

    try:
        print("Iniciando leitura da balança. Pressione Ctrl+C para parar.")
        while True:
            leitura = serial_conn.read_until(b'\n').strip()  # Lê até encontrar uma nova linha
            print(f"Dados brutos recebidos: {leitura}")  # Exibe os dados brutos recebidos

            # Salva os dados brutos no arquivo de log
            """ with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"{leitura.decode('utf-8', errors='ignore').strip()}\n") """
            
            peso = extrair_peso(leitura)
            print(peso)
            if peso:
                print(f"Peso lido: {peso}")
            else:
                print("Peso inválido ou não detectado.")
    except KeyboardInterrupt:
        print("Leitura interrompida pelo usuário.")
    except Exception as e:
        print(f"Erro durante a leitura: {e}")
    finally:
        if serial_conn and serial_conn.is_open:
            serial_conn.close()
            print("Conexão serial fechada.")

if __name__ == "__main__":
    testar_balanca()