def meu_decorador(funcao):
    def envelope(**kw):
        print("Faz algo antes de executar a função.")
        funcao(**kw)
        print("Faz algo depois de executar a função.")

    return envelope

@meu_decorador
def ola_mundo(ano_de_nascimento, idade , nome):
    print(f"Olá {nome} ao Mundo!!")
    print(f"Vc nasceu em {ano_de_nascimento} e portanto tem {idade} anos.")


ola_mundo(nome="Dayvison", idade=31, ano_de_nascimento=1992)