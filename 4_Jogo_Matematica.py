import random 

iModo = int(input("""
███╗   ███╗ █████╗ ████████╗███████╗███╗   ███╗ █████╗ ████████╗██╗ ██████╗ █████╗ 
████╗ ████║██╔══██╗╚══██╔══╝██╔════╝████╗ ████║██╔══██╗╚══██╔══╝██║██╔════╝██╔══██╗
██╔████╔██║███████║   ██║   █████╗  ██╔████╔██║███████║   ██║   ██║██║     ███████║
██║╚██╔╝██║██╔══██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║   ██║   ██║██║     ██╔══██║
██║ ╚═╝ ██║██║  ██║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝

Escolha o Modo de Jogo:

(1) Soma
(2) Subtração
(3) Multiplicação
(4) Divisão
            
Modo: """))

i = 0
iPartidas = int(input('Quantas Partidas? '))

iCasas = int(input('Quantas Casas Decimais (1 a 5)? '))

######################################### ADIÇÃO 

if iModo == int('1') and iCasas == int('1'):
        while i < iPartidas:
         print(random.randint(0,9),'+',(random.randint(0,9)))
         input('Resultado: ')
         i += 1 

elif iModo == int('1') and iCasas == int('2'):
        while i < iPartidas:
         print(random.randint(10,99),'+',(random.randint(10,99)))
         input('Resultado: ')
         i += 1 

elif iModo == int('1') and iCasas == int('3'):
        while i < iPartidas:
         print(random.randint(100,999),'+',(random.randint(100,999)))
         input('Resultado: ')
         i += 1 

elif iModo == int('1') and iCasas == int('4'):
        while i < iPartidas:
         print(random.randint(1000,9999),'+',(random.randint(1000,9999)))
         input('Resultado: ')
         i += 1 

elif iModo == int('1') and iCasas == int('5'):
        while i < iPartidas:
         print(random.randint(10000,99999),'+',(random.randint(10000,99999)))
         input('Resultado: ')
         i += 1 

######################################### SUBTRAÇÃO 

elif iModo == int('2') and iCasas == int('1'):
        while i < iPartidas:
         print(random.randint(0,9),'-',(random.randint(0,9)))
         input('Resultado: ')
         i += 1 

elif iModo == int('2') and iCasas == int('2'):
        while i < iPartidas:
         print(random.randint(10,99),'-',(random.randint(10,99)))
         input('Resultado: ')
         i += 1 

elif iModo == int('2') and iCasas == int('3'):
        while i < iPartidas:
         print(random.randint(100,999),'-',(random.randint(100,999)))
         input('Resultado: ')
         i += 1 

elif iModo == int('2') and iCasas == int('4'):
        while i < iPartidas:
         print(random.randint(1000,9999),'-',(random.randint(1000,9999)))
         input('Resultado: ')
         i += 1 

elif iModo == int('2') and iCasas == int('5'):
        while i < iPartidas:
         print(random.randint(10000,99999),'-',(random.randint(10000,99999)))
         input('Resultado: ')
         i += 1 

######################################### Multiplicação

elif iModo == int('3') and iCasas == int('1'):
        while i < iPartidas:
         print(random.randint(0,9),'x',(random.randint(0,9)))
         input('Resultado: ')
         i += 1 

elif iModo == int('3') and iCasas == int('2'):
        while i < iPartidas:
         print(random.randint(10,99),'x',(random.randint(10,99)))
         input('Resultado: ')
         i += 1 

elif iModo == int('3') and iCasas == int('3'):
        while i < iPartidas:
         print(random.randint(100,999),'x',(random.randint(100,999)))
         input('Resultado: ')
         i += 1 

elif iModo == int('3') and iCasas == int('4'):
        while i < iPartidas:
         print(random.randint(1000,9999),'x',(random.randint(1000,9999)))
         input('Resultado: ')
         i += 1 

elif iModo == int('3') and iCasas == int('5'):
        while i < iPartidas:
         print(random.randint(10000,99999),'x',(random.randint(10000,99999)))
         input('Resultado: ')
         i += 1 

######################################### DIVISÃO

elif iModo == int('4') and iCasas == int('1'):
        while i < iPartidas:
         print(random.randint(0,9),'/',(random.randint(0,9)))
         input('Resultado: ')
         i += 1 

elif iModo == int('4') and iCasas == int('2'):
        while i < iPartidas:
         print(random.randint(10,99),'/',(random.randint(1,9)))
         input('Resultado: ')
         i += 1 

elif iModo == int('4') and iCasas == int('3'):
        while i < iPartidas:
         print(random.randint(100,999),'/',(random.randint(10,99)))
         input('Resultado: ')
         i += 1 

elif iModo == int('4') and iCasas == int('4'):
        while i < iPartidas:
         print(random.randint(1000,9999),'/',(random.randint(100,999)))
         input('Resultado: ')
         i += 1 

elif iModo == int('4') and iCasas == int('5'):
        while i < iPartidas:
         print(random.randint(10000,99999),'/',(random.randint(1000,9999)))
         input('Resultado: ')
         i += 1 
