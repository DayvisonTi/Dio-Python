class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo


    def verificar_saldo(self):
        return self.__saldo
    

    def mensagem_personalizada(self):
        if self.__saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# Classe UsuarioTelefone:
class UsuarioTelefone(PlanoTelefone):
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano
        

    def verificar_saldo(self):
        saldo = self.plano.verificar_saldo()
        mensagem = self.plano.mensagem_personalizada()
        return saldo, mensagem
 



nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

 
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  


saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)

