'''
Turma 1TDCG
Professor: Fabio Cabrini
Integrantes:
Danilo da Gama Campos, RM99680
Eduardo do Nascimento Silva, RM99225
Gustavo Duarte Bezerra da Silva, RM99774
Henrique Batista de Souza, RM99742
'''

import socket

def scan_ports(host, ports):
    portas_abertas = []  # Criação de uma lista vazia que armazenara as portas abertas encontradas durante o escaneamento.
    for port in ports:   # Inicia um loop que percorrerá cada número de porta na lista
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um objeto de socket usando IPv4 e o tipo de socket para fluxos de dados TCP 
        sock.settimeout(1)  # Definindo um timeout para a conexão
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:     # Verifica se a conexão foi estabelecida com sucesso. Se sim, adiciona o número da porta à lista portas_abertas.
            portas_abertas.append(port)
    return portas_abertas

def save_results(filename, results):
    with open(filename, 'w') as file:
        for portas in results:
            file.write(f"Porta {portas}: Aberta\n")

def main():
    ip_alvo = "127.0.0.1"           # IP onde haverá o escaneamento
    portas_alvos = range(1, 65536)  # Todas as portas de 1 a 65535
    
    portas_abertas = scan_ports(ip_alvo, portas_alvos)    # Realizado o escaneamento das portas no IP especificado. O resultado é armazenado na variável portas_abertas
    save_results("resultados.txt", portas_abertas)        # Vê quais portas estão abertas e armazena em um .txt
    
    portas_fiware = [1026, 1883, 4041, 8666, 27017]            # Portas que o Fiware abre
    
    fiware_encontrado = any(port in portas_abertas for port in portas_fiware)    # verifica se algum dos números de porta Fiware está presente na lista de portas abertas
    if fiware_encontrado:
        print("Fiware rodando aqui")
    else:
        print("Nenhum fiware encontrado")

if __name__ == "__main__":
    main()
