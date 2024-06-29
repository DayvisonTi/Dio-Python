import os

class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print("Ligando Motor...")

    def __str__(self):
        return self.cor

    def __str__(self):
        return f'''Cor: {self.cor} {os.linesep}Placa: {self.placa} {os.linesep}Nº Rodas: {self.num_rodas}'''

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado
        
        
    def esta_carregado(self):
        return f'{"Sim" if self.carregado else "Não"} estou carregado.'

class Motocicleta(Veiculo):
    pass
        

class Carro(Veiculo):
    pass



os.system("clear") 
cam = Caminhao("roxo","ABC-4321",10, True)
cam.esta_carregado()
cam.ligar_motor()
print(f'Caminhão\n{cam}')
print(cam.esta_carregado())

# mesmo que não tenha atributos na sua classe mas ele herda os atributos da Classe Pai (Veiculo)
moto = Motocicleta("vermelha", "ABC-1234", 2)
print(f"Moto\n{moto}")

