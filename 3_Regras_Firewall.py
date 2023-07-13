#pip install requests

import requests, csv, subprocess

iOpcao = input('''
███████╗██╗██████╗ ███████╗██╗    ██╗ █████╗ ██╗     ██╗     
██╔════╝██║██╔══██╗██╔════╝██║    ██║██╔══██╗██║     ██║     
█████╗  ██║██████╔╝█████╗  ██║ █╗ ██║███████║██║     ██║     
██╔══╝  ██║██╔══██╗██╔══╝  ██║███╗██║██╔══██║██║     ██║     
██║     ██║██║  ██║███████╗╚███╔███╔╝██║  ██║███████╗███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝

Selecione a Opção:

(1) Adicionar Regras de Saída
(2) Adicionar Regras de Entrada 
(3) Remover Regras Adicionadas - Saída
(4) Remover Regras Adicionadas - Entrada 

''')


#Fonte = Abuse CH
resposta = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text

iCSV = csv.reader(filter(lambda x: not x.startswith("#"),resposta.splitlines()))

if iOpcao == 1:   
 for linha in iCSV:
    ip = linha[1]
    if(ip)!=("dst_ip"):
        print("Regra Adicionada ao Firewall:",ip)
        regra="netsh advfirewall firewall add rule name='IP Maligno' Dir=In Action=Block RemoteIP="+ip
        subprocess.run(["Powershell","-Command", regra])
        subprocess.run(["Powershell","-Command", regra])

elif iOpcao == 2: 
 for linha in iCSV:
    ip = linha[1]
    if(ip)!=("dst_ip"):
        print("Regra Adicionada ao Firewall:",ip)
        regra="netsh advfirewall firewall add rule name='IP Maligno' Dir=In Action=Block RemoteIP="+ip
        subprocess.run(["Powershell","-Command", regra])

elif iOpcao == 3:
    regra ="netsh advfirewall delete rule name='IP Maligno' Dir=Out"
    subprocess.run(["Powershell","-Command",regra])

elif iOpcao == 4:
    regra ="netsh advfirewall delete rule name='IP Maligno' Dir=In"
    subprocess.run(["Powershell","-Command",regra])