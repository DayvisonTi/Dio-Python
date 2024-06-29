# Encapsulamento

# public: atributos ou metodos que podem ser acessados dentro e fora da classe
# (_) protected: são atributos ou metodos que podem ser acessados somente dentro da classe ou pelas filhas da classe
# (__) private : são atributos ou metodos que só estão disponiveis dentro da classe (_NOMECLASSE__nome_atributo)

class Conta:

    def __init__(self,num_agencia, saldo=0):
        # se o atributo tiver um underline(_) antes do nome,por convenção não deve ser acessado diretamente
        self._saldo = saldo
        # self.conta = conta
        self.num_agencia = num_agencia

    # def __str__(self):
    #     return f'A sua Conta {self.conta} na Agencia {self.num_agencia} esta com saldo de R${float(self._saldo):.2f}.'
        

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor
    
    def mostrar_saldo(self, senha):
        if senha == 1234:
            return self._saldo
        
        print(f"Senha Incorreta.")
    

        

    
b1 = Conta('0001', 1000)
b1.depositar(100)
b1.sacar(300)
print(b1.num_agencia)
print(b1.mostrar_saldo(1234))





