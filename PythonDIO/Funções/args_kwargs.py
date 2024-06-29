from datetime import date
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave,valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

hoje = date.today()
str_hj = hoje.strftime("%d/%m/%Y")
exibir_poema(str_hj, "Zen of Python", "Beautiful is better than ugly.","Explicit is better than implicit.",autor="Tim Peters", ano=1999)