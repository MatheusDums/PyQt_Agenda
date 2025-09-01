import serial
import time

try:
    ser = serial.Serial('COM3', 9600, timeout=1)
    print(f"Conectado em: {ser.name}")
    dataRead = ser.read(10)
    
    peso_str = dataRead.strip()

    print(f"Peso atual: {peso_str} kg")
    
except serial.SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")
except Exception as e:
            print(f"Ocorreu um erro: {e}")




""" ser = serial.Serial('COM3', baudrate=9600, timeout=1) 

try:
    print(f"Conectado a porta {ser.portstr} em baud {ser.baudrate}")
    
    while True: 
        line = ser.readline().decode('utf-8').strip()
        if(line):
            print(f"{line} recebido")
    
except serial.SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")
except Exception as e:
            print(f"Ocorreu um erro: {e}") """

 
""" ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)
 
time.sleep(2)
 
try:
    while True:
        ser.write(b'P\r\n')
        data = ser.readline().decode('utf-8').strip()
        if data:
            print("Peso:", data)
        time.sleep(1)
 
except KeyboardInterrupt:
    print("Saindo...")
finally:
    ser.close() """



""" 
port = 'COM3'
baudrate = 9600
parity = serial.PARITY_NONE
stopbits = serial.STOPBITS_ONE
bytesize = serial.EIGHTBITS

try:
    temp = serial.Serial(port, baudrate, bytesize, parity, stopbits)
    
    temp.reset_input_buffer()
    temp.reset_output_buffer()

    temp.close()
except:
    print('Unable to open/clean ' + port + ':' + str(baudrate))
    
with serial.Serial(port, baudrate, bytesize, parity, stopbits) as ser:

    while True:
        
        if ser.in_waiting > 0:
            time.sleep(0.1)
            continue

        x = ser.readline()
        print(x)
        time.sleep(1) """


""" try:
    ser = serial.Serial('COM3', 9600)
    print(f"Conectado em: {ser.name}")
    dataRead = ser.read(6).decode('utf-8')
    
    print(dataRead)
except serial.SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")
except Exception as e:
            print(f"Ocorreu um erro: {e}") """

""" try:
    ser = serial.Serial('COM3', 9600, timeout=1)
    print(f"Conectado em: {ser.name}")
    dataRead = ser.read(6).decode('utf-8')
    
    with open('dados.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
    
    
    print(dataRead)
    
except serial.SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")
except Exception as e:
            print(f"Ocorreu um erro: {e}") """
            
            

""" porta_serial = 'COM3'
baud_rate = 9600
timeout = 1

try:
    ser = serial.Serial(porta_serial, baud_rate, timeout=timeout)
    print(f"Porta {porta_serial} aberta com sucesso.")
    
    dados_bytes = ser.readline()
    dados_string = dados_bytes.decode('utf-8', errors='ignore')
    
    peso_str = dados_string.strip().split(" ")[0]
    
    try:
        peso = float(peso_str)
        print(f"Peso atual: {peso} kg")
    except ValueError:
        print(f"Dados recebidos: {dados_string.strip()}")
    time.sleep(0.1)
except serial.SerialException as e:
    print(f"Erro ao abrir ou comunicar com a porta serial: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    if 'ser' in locals() and ser.isOpen():
        ser.close()
        print("Porta serial fechada.") """
        
        

""" try:
    ser = serial.Serial('COM3', 9600, timeout=1)
    print(f"Conectado em: {ser.name}")
    dataRead = ser.read(6).decode(errors='ignore')
    
    peso_str = dataRead.strip().split(" ")[0]
        
    if peso_str.startswith('00'):
        peso_str = peso_str[1:]
    if peso_str.startswith('0') :
        peso_str = peso_str[:1] + "." + peso_str[1:]
    if not peso_str.startswith('0'):
        peso_str = peso_str[:1] + "." + peso_str[1:]

    print(f"Peso atual: {peso_str} kg")
    
    print(dataRead)
    
except serial.SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")
except Exception as e:
            print(f"Ocorreu um erro: {e}") """
            
            
