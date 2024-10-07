from datetime import datetime
import textwrap

def menu():
    menu = """
    [1] \tDepositar
    [2] \tSacar
    [3] \tExtrato
    [4] \tNova conta
    [5] \tNovo usuário
    [6] \tListar Contas
    [0] \tSair

    => """
    return input(textwrap.dedent(menu))

def Depositar(saldo, valor, extrato, numero_operacoes, /):
    valor = float(input("Adicione o valor de depósito: "))
    
    if valor > 0:
        saldo += valor
        data_hora = datetime.now().strftime("%d/%m-%Y %H:%M")
        extrato += f"Depósito: R$ {valor:.2f} em {data_hora}\n"
        numero_operacoes += 1
        print("Depósito realizado com sucesso!")
    else:
        print("Operação não realizada, valor inválido!")

    return saldo, extrato, numero_operacoes

def Sacar(*, saldo, valor, extrato, limite, numero_operacoes, LIMITE_OPERACOES):
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

    return saldo, extrato, numero_operacoes

def Extrato(saldo, /, *, extrato):
    print("*****EXTRATO*****")
    print("Nenhuma operação realizada" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}.")
    print("*****************")

def criar_usuario(usuarios):
    cpf = input("Escreva seu CPF, (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta já existente neste CPF!")
        return

    nome = input("Escreva seu nome completo: ")
    data_nascimento = input("Escreva sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Escreva seu endereço (Logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, criação de conta encerrada!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\  
            Agencia: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_OPERACOES = 10
    AGENCIA = "0001"

    valor = 0
    saldo = 0
    limite = 500
    extrato = ""
    numero_operacoes = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            saldo, extrato, numero_operacoes = Depositar(saldo, valor, extrato, numero_operacoes)

        elif opcao == "2":
            saldo, extrato, numero_operacoes = Sacar(
                saldo=saldo, 
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_operacoes=numero_operacoes,
                LIMITE_OPERACOES=LIMITE_OPERACOES
            )

        elif opcao == "3":
            Extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            criar_usuario(usuarios)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Sistema fechado!")
            break

        else:
            print("Opção inválida, por favor escolha novamente a opção desejada.\n")

main()
