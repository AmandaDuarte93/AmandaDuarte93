from datetime import datetime

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

valor = 0
saldo = 0
limite = 500
extrato = ""
numero_operacoes = 0 
LIMITE_OPERACOES = 10

def Depositar():
    global valor, extrato, saldo, numero_operacoes
    valor = float(input("Adicione o valor de depósito: "))
    
    if valor > 0:
        saldo += valor
        data_hora = datetime.now().strftime("%d/%m-%Y %H:%M")
        extrato += f"Depósito: R$ {valor:.2f} em {data_hora}\n"
        numero_operacoes += 1
        print("Depósito realizado com sucesso!")
    else:
        print("Operação não realizada, valor inválido!")

def Sacar():
    global valor, extrato, saldo, limite, numero_operacoes
    valor = float(input("Adicione o valor de saque: "))

    if valor > saldo:
        print("ERRO: saldo insuficiente!\n")
    elif valor > limite:
        print("ERRO: valor máximo por saque é R$ 500,00.\n")
    elif numero_operacoes >= LIMITE_OPERACOES:
        print("ERRO: limite de operações acima do permitido por dia!\n")
    elif valor > 0:
        saldo -= valor
        data_hora = datetime.now().strftime("%d/%m-%Y %H:%M")
        extrato += f"Saque: R$ {valor:.2f} em {data_hora}\n"
        numero_operacoes += 1
        print("Saque realizado com sucesso!\n")
    else:
        print("ERRO: valor inválido para saque.\n")

def Extrato():
    global extrato
    print("*****EXTRATO*****")
    print("Nenhuma operação realizada" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}.")
    print("*****************")

while True:
    opcao = input(menu)

    if opcao == "1":
        Depositar()
    elif opcao == "2":
        Sacar()
    elif opcao == "3":
        Extrato()
    elif opcao == "0":
        print("Sistema fechado!")
        break
    else:
        print("Opção inválida, por favor escolha novamente a opção desejada.\n")
