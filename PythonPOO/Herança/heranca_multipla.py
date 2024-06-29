class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f" O {self.__class__.__name__} : {" | ".join([f"{chave} = {valor}"for chave, valor in self.__dict__.items()])} "
        

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo
        


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico
        




class Cachorro(Mamifero,Animal):
    pass

class Gato(Mamifero, Animal):
    pass

class Leao(Mamifero, Animal):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self,cor_pelo, cor_bico, num_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, num_patas=num_patas)
       


# cachorro = Cachorro(4, "Branco")
# gato = Gato(8, 'Preto')
# leao = Leao(5, "Amarelo")
ornitorrinco = Ornitorrinco(num_patas=6, cor_pelo="Marrom", cor_bico="Amarelo")

# print(gato)
# print(cachorro)
# print(leao)
print(ornitorrinco)