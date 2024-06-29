import os

def meu_decorador(funcao):
    def envelope(*aw, **kw):
        print("Faz algo antes de executar a função.")
        funcao(*aw, **kw)
        print("Faz algo depois de executar a função.")

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá {nome} ao Mundo!!")


ola_mundo("Dayvison")

input()
os.system("clear")