'''
Turma 1TDCG
Professor: Fabio Cabrini
Integrantes:
Danilo da Gama Campos, RM99680
Eduardo do Nascimento Silva, RM99225
Gustavo Duarte Bezerra da Silva, RM99774
Henrique Batista de Souza, RM99742
'''
# pip install nmap
import nmap

def scan_ports(host):                           # Chama o nmap para verificar da porta 1 a 65535
    scanner = nmap.PortScanner()                # Escaneia as portas
    scanner.scan(host, arguments='-p 1-65535')  # Da 1ª á 65.535ª
    return scanner[host]['tcp'].keys()

def save_results(filename, resultados):         
    with open(filename, 'w') as file:
        for porta in resultados:
            file.write(f"Porta {porta}: Aberta\n")

def main():
    maquina = "127.0.0.1"                       # IP da máquina
    
    portas_abertas = scan_ports(maquina)        # Para salvar o scan em .txt
    save_results("resultado_do_scan.txt", portas_abertas)
    
    fiware = [1026, 1883, 4041, 8666, 27017]    # Portas para verificar 
    
    fiware_encontrado = False                   # Caso encontre as portas abertas
    for portas in fiware:
        if portas in portas_abertas:
            fiware_encontrado = True
            break
    
    if fiware_encontrado:                       # Avisa se foi encontrado ou não
        print("Fiware em funcionamento")
    else:
        print("Fiware desligado")

if __name__ == "__main__":
    main()
