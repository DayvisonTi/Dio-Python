class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    @property
    def nome(self):
        return self.__nome
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def plano(self):
        return self.__plano

    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

# Entrada de dados
nome = input()
numero = input()
plano = input()

# Criação do objeto UsuarioTelefone com os dados fornecidos
usuario = UsuarioTelefone(nome, numero, plano)

# Impressão da representação string do objeto usando print()
print(usuario)