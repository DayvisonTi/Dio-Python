
# def meu_decorador(funcao):
#     def envelope(*aw, **kw):
#         print("Faz algo antes de executar a função.")
#         funcao(*aw, **kw)
#         print("Faz algo depois de executar a função.")

#     return envelope

# @meu_decorador
# def ola_mundo(nome, idade):
#     print(f"Olá {nome} com {idade} anos de idade,Bem vindoao Mundo!!")


# ola_mundo("Dayvison", 20)

def duplicar(func):
    def envelope(*aw, **kw):
        func(*aw, **kw)
        return func(*aw, **kw)
    return envelope   


def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}.")
    return tecnologia.upper()

tecnologia = aprender("Python")
print(tecnologia)