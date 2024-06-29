import os
os.system('clear')
class Estudante:
    escola = "Dio"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
        
aluno_1 = Estudante("guilherme", 54321)
aluno_2 = Estudante("giovana", 12345)
aluno_3 = Estudante("Dayvison", 56789)

# mostrar_valores(aluno_1, aluno_2, aluno_3)


Estudante.escola = "Python"
mostrar_valores(aluno_3)
















