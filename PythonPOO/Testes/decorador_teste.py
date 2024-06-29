from abc import ABC, abstractmethod

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico 

    def saldo(self):
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero, agencia, saldo_inicial=0):
        historico = Historico()
        return cls(saldo_inicial, numero, agencia, cliente, historico)
    
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print("Saque efetuado com sucesso")
            return True
        print("Erro na operação de saque")
        return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito efetuado com sucesso")
            return True
        print("Erro na operação de depósito")
        return False

class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques, saldo, numero, agencia, cliente, historico):
        self._limite = limite
        self._limite_saques = limite_saques
        super().__init__(saldo, numero, agencia, cliente, historico)

class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.depositar(self._valor):
            conta._historico.adicionar_transacao(f"Depósito de {self._valor}")

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.sacar(self._valor):
            conta._historico.adicionar_transacao(f"Saque de {self._valor}")

class Cliente:
    def __init__(self, endereco, contas=None):
        if contas is None:
            contas = []
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas=None):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(endereco, contas)
