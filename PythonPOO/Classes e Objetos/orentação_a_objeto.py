class Casa:
    def __init__(self,vaga_garagem,quartos,salas,cozinha,banheiros):
        self.vaga_garagem = vaga_garagem
        self.quartos = quartos
        self.salas = salas
        self.cozinha = cozinha
        self.banheiros = banheiros

    def __str__(self):
        return f"""A Casa tem {self.vaga_garagem} Vaga(s) de garagem,{self.quartos} Quarto(s),{self.salas} Sala(s),{self.cozinha} Cozinha(s) Maravilhosa(s) e {self.banheiros} Banheiro(s)."""
        
casa1 = Casa(vaga_garagem=2,quartos=3,salas=2,cozinha=1,banheiros=2)
print(casa1.__str__())