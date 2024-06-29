from datetime import datetime
import os

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento


    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        ano_atual = datetime.now().year
        return ano_atual - self._ano_nascimento
    
    @idade.setter
    def idade(self, value):
        _value = value or 0
        self._ano_nascimento = _value
    
    @idade.deleter
    def idade(self):
        self._ano_nascimento = 0
    
    
        


p = Pessoa('Dayvison', 1992)

print(p.nome)
p.idade = 1979

del p.idade

print(f"O Meu nome é {p.nome} e minha idade é {p.idade}.")
p.idade = 1950

print(f"O Meu nome é {p.nome} e minha idade é {p.idade}.")

input()
os.system('clear')