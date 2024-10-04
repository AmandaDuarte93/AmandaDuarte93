menu = """
Escolha a opção desejada: 

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

valor = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3  

while True:

    opcao = input(menu)

    #deposito
    if opcao == "1":

        valor = float(input(f"Adicione o valor de depósito: "))
    
        if valor > 0:

            saldo += valor  #mesma coisa que: saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else: 
            print("Operação não realizada, saldo insuficiente!")

    #saque
    elif opcao == "2":
        valor = float(input(f"Adicione o valor de saque: "))
        
        sem_saldo = valor > saldo

        sem_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if sem_saldo:
            print("Erro! Saldo insuficiente.")
        
        elif sem_limite:
            print("Erro! Valor de saque maior que R$ 500,00 reais.")
        
        elif excedeu_saques:
            print("Erro! Número de saques acima do permitido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1  #incrementando o numero de saques p/ para em limite de saque.

        else: 
            print("Operação não realizada, saldo insuficiente!")

    #Extrato
    elif opcao == "3":
        print("\n*****EXTRATO*****")
        print("Nenhuma operação realizada" if not extrato else extrato )
        print(f"\nSaldo: R${saldo:.2f}.")
        print("*****************")
    #sair
    elif opcao == "0":
        break

    else:
        print("Opção inválida, por favor escolha novamente a opção desejada.")