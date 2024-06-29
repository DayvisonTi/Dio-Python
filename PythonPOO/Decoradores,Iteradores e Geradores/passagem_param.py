def mensagem(nome):
    print("Executando mensagem....")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f"Olá tubo bem com voçê {nome}?"

def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)


print(executar(mensagem, "Dayvison"))

print(executar(mensagem_longa, "Dayvison"))



# pessoa = mensagem("Dayvison")
# pessoa2 = mensagem_longa(pessoa)
# print(pessoa2)