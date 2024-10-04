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
numero_saques = 0
LIMITE_SAQUES = 3  

while True:
    opcao = input(f"Seja bem vindo! Escolha a opção desejada: \n{menu}")

    # Depósito
    if opcao == "1":
        valor = float(input(f"Adicione o valor de depósito: "))
        
        if valor > 0:
            saldo += valor  # mesma coisa que: saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Depósito falhou! O valor deve ser positivo.\n")

    # Saque
    elif opcao == "2":
        valor = float(input(f"Adicione o valor de saque: "))
        
        if valor > saldo:
            print("ERRO, saldo insuficiente!\n")

        elif valor > limite:
            print("ERRO! Valor máximo por saque: R$500,00 reais.\n")

        elif numero_saques >= LIMITE_SAQUES:
            print("ERRO! Limite de saques acima do permitido.\n")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1  # Incrementando o número de saques para parar no limite de saque.
            print("Operação realizada com sucesso!\n")
            
        else:
            print("ERRO! Valor inválido para saque.\n")

    # Extrato
    elif opcao == "3":    
        print("*****EXTRATO*****")
        print("Nenhuma operação realizada" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}.")
        print("*****************")
    
    # Sair
    elif opcao == "0":
        break

    else:
        print("Opção inválida, por favor escolha novamente a opção desejada.\n")
