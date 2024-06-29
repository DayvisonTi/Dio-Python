class Casa:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        
    
    def area(self):
        return self.comprimento * self.largura


minha_casa = Casa(10, 5)
print(minha_casa.comprimento)  # Isso vai imprimir 50, que é o resultado de 10 * 5
