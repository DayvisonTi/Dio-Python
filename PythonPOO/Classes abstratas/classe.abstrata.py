from abc import ABC, abstractmethod ,abstractproperty

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    def desligar(self):
        pass

    
    @abstractproperty
    def marca(self):
        pass      



class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando....")
        print("Ligada.")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada.")

    @property
    def marca(self):
        return "Philco"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado....")
        print("Ligada.")

    def desligar(self):
        print("Desligando o Ar condicionado...")
        print("Desligada.")

    @property
    def marca(self):
        return "LG"

controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)