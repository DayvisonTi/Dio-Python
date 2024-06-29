from random import randint

class Pessoa:
    # atributo de classe
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    # Esse é um metodo de instancia,por isso recebe o parametro self
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # assim como um atributo de classe vale pra todos os objetos,o classmethod é um metodo que vai valer para todo objeto
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    # staticmethod não tem por obrigação receber parametro como self ou cls
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

        

p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

print(p1.gera_id())

p1 = Pessoa.por_ano_nascimento("Dayvison", 1992)
print(p1.nome, p1.idade)
