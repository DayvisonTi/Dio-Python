import os
os.system('clear')

class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        var = 123
        print(var)

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
    def comer(self, comendo):
        self.comendo = comendo
        if comendo:
            print(f"{self.nome} está comendo.")



 

p = Pessoa("Guilherme", 31)
p.comer(True)
print(p.idade, p.comendo)
print(Pessoa.e_maior_idade(p.idade))
print(Pessoa.e_maior_idade(8))


p2 = Pessoa("Dayvison", 5)


print(Pessoa.e_maior_idade(p.idade))
