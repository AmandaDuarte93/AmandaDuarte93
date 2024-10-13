from datetime import datetime
import textwrap
from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def fazer_transacao():
        pass

    def add_conta(self, conta):
        self.contas.append(conta)
        

class PessoaFisica(Cliente):
    def __init__(self, cpf, data_nascimento, nome, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.nome = nome   

class Conta:
    def __init__(self, numero, cliente):
        self._cliente = cliente
        self._numero = numero
        self._agencia = "0001"
        self._saldo = 0
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def saldo(self):
        return self._saldo
    
    def historico(self):
        return self._historico
    
    def sacar(self, valor,):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\nERRO: saldo insuficiente!")
            
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True
        
        else:
            print("\nERRO: valor inválido para saque.")

        return False
        
    def depositar(self, valor, numero_operacoes):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
        
        else:
            print("Operação não realizada, valor inválido!")
            return False
        
        return True
    

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes 
             if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques
    
        if excedeu_limite:
            print("\nSaque não realizado! O valor excedeu o limite.")

        elif excedeu_saques:
            print("\nSaque não realizado! Número de saques acima do permitido.")

        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return f"""\t
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    

class Historico:
     def __init__(self):
         self.transacoes = []

     @property
     def transacoes(self):
         return self._transacoes
     
     def add_transacao(self, transacao):
         self._transacoes.append(
             {   
                "tipo": transacao.__class__.__name__,
                 "valor": transacao.valor,
                 # adicionando hora e data na operação
                 "data": datetime.now().strftime("%d/%m-%Y %H:%M"),
             }
         )
                 
          
class transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registar(self, conta):
        pass


class Saque(transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucess_transacao = conta.sacar(self.valor)
    
        if sucess_transacao:
            conta.historico.add_transacao(self)
        

class Deposito(transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucess_transacao = conta.depositar(self.valor)
    
        if sucess_transacao:
            conta.historico.add_transacao(self)


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

def Depositar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_usuario(usuario)
    if not conta:
        return

    usuario.realizar_transacao(conta, transacao)
       
def Sacar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_usuario(usuario)
    if not conta:
        return

    usuario.realizar_transacao(conta, transacao)
    
def Extrato(usuarios):
    cpf = input("Informe o cpf do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n Cliente não encontrado!")
        return
    conta = conta ######## ARRUMAR CORRETAMENTE#############
    if not conta:
        return
    
    print("*****EXTRATO*****")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Sem movimentações nesta conta!"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao["tipo"]}: \n\tR$ {transacao["valor"]:.2f}"

    print(extrato)
    print(f"\nSaldo: \n\tR$ {conta.saldo:.2f}.")
    print("*****************")

def recuperar_conta_usuario(usuario):
    if not usuario.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return usuario.contas[0]

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, criação de conta encerrada!")

def criar_usuario(usuarios):
    cpf = input("Escreva seu CPF, (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta já existente neste CPF!")
        return

    nome = input("Escreva seu nome completo: ")
    data_nascimento = input("Escreva sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Escreva seu endereço (Logradouro, numero - bairro - cidade/sigla estado): ")

    usuario = PessoaFisica(
        nome=nome, 
        data_nascimento=data_nascimento, 
        cpf=cpf, 
        endereco=endereco
    )
    
    usuarios.append(usuario)

    print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            Depositar(usuarios)

        elif opcao == "2":
             Sacar(usuarios)

        elif opcao == "3":
            Extrato(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1 # incrementando numero de contas para não repetir.
            conta = criar_conta(numero_conta, usuarios, contas)

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