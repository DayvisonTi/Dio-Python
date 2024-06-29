import os
# Classe base (superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        pass

# Subclasses que herdam de Animal
class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

class Pato(Animal):
    def fazer_som(self):
        return "Quack!"

# Função que demonstra polimorfismo
def fazer_barulho(animal):
    print(animal.fazer_som())

# Criando instâncias das subclasses
rex = Cachorro("Rex")
garfield = Gato("Garfield")
donald = Pato("Donald")

# Chamando a função com diferentes tipos de animais
fazer_barulho(rex)       # Saída: Au au!
fazer_barulho(garfield)  # Saída: Miau!
fazer_barulho(donald)    # Saída: Quack!

input()
os.system('clear')