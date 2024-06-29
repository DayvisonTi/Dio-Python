import os

class Nome:
    def __init__(self, nome=''):
        self._nome_completo = nome 

    @property
    def nome(self):
        return self._nome_completo
  
    
    @nome.setter
    def nome(self, value):
        full = self._nome_completo.split()
        _value = value or ""
        self._nome_completo = full[0] + _value + full[1]

    @nome.deleter
    def nome(self):
        print("Deletando...")
        self._nome_completo = "Vazio"
        

    

p1 = Nome("Dayvison Lacerda")
p1.nome = " Araujo "


print(p1.nome)


input()
os.system("clear")

