class Pessoa:
    # atributo de classe
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

        

p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

p1 = Pessoa.por_ano_nascimento("Dayvison", 1992)
print(p1.nome, p1.idade)
