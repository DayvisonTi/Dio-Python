# import a Biblioteca os
import os
# limpa o terminal
os.system('clear')
# classe Pai Passaro com um metodo 'voar'
class Passaro:
    def voar(self):
        print('Voando...')

# classe filha de Passaro herdando o metodo voar 
class Pardal(Passaro):
    def voar(self): 
        return super().voar()
# classe filha de Passaro herdando o metodo voar porem com o metodo personalizado    
class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não voa....')
# FIXME: exemplo não recomendado do uso de herança
class Aviao(Passaro):
    def voar(self):
        print('O Avião esta decolando...')
# função voar que pode receber como parametro a propria classe e retornar o metodo de cada uma
def plano_voo(obj):
    obj.voar()

# instancia de classes
p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()

# chamando a função voar e implementando o metodo em uma instancia de classe
plano_voo(p2)


# plano_voo(Pardal())
# plano_voo(Avestruz())
# plano_voo(Aviao())




