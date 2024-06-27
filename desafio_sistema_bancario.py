import re

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    contas = []
    usuarios = []
    AGENCIA = '0001'
    LIMITE_SAQUES = 3

    
    while True:

        opcao = menu().lower().strip()

        if opcao == "d":

            valor = float(input("Informe o valor do depósito: R$"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":

            valor = float(input("Informe o valor do saque: R$"))

            saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES = saque (
                
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES 
                )
        
        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            novo_usuario(usuarios)

        elif opcao == "nc":
            num_conta = len(contas) + 1
            conta = nova_conta(usuarios,num_conta, AGENCIA)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "pu":
             pesquisar_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def menu():

    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[pu] Pesquisar Usuário
[q] Sair

=> """

    opcao = input(menu)

    return opcao

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Deposito efetuado com Sucesso!!!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(* ,saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque no valor de R${valor:.2f} efetuado com sucesso!!!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, valor, extrato, limite, numero_saques, limite_saques

def mostrar_extrato(saldo, /,*, extrato):
    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
 

def novo_usuario(usuarios):

   
    while True:
        
        cpf = input('CPF: ')
        
        if any(usuario['cpf'] == cpf for usuario in usuarios):
            print('Já existe um usuário para este CPF!!!')
            perg = input('Quer tentar outro CPF? [S/N]: ').upper().strip()
            if perg == 'N':
                return None
            
        else:
            break
            
    nome = input('Nome: ').title()
    nasc = input('Data de Nascimento (dd/mm/aaaa): ')
        
    endereco = {
        'logradouro': input('Logradouro: ').title().strip(),
        'numero': input('Nº: ').strip(),
        'bairro': input('Bairro: ').title().strip(),
        'cidade': input('Cidade: ').title().strip(),
        'estado': input('Estado (AB): ').upper().strip()
    }
    
    usuarios.append({"nome": nome, "nasc": nasc, "cpf": cpf, "endereco": endereco})
    print('Usuário cadastrado com sucesso!!!')

    

def filtro_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def nova_conta(usuarios,num_conta, agencia):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}
    
    print("Necessário cadastrar um usuário primeiro!!!")
    


def listar_contas(contas):

    for conta in contas:
    
        print("\n{:=^30}".format(' CONTA '))
        print(f"""
        Agência:{conta["agencia"]}
        Conta:{conta["num_conta"]}
        Usuário:{conta["usuario"]["nome"]}
""")
        print('=' * 30)

def pesquisar_usuario(usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro_usuarios(cpf, usuarios)

    if usuario:
        print("\n{:=^30}".format(' USUÁRIO '))
        print(f"Nome: {usuario['nome']}")
        print(f"Data de Nascimento: {usuario['nasc']}")
        print(f"CPF: {usuario['cpf']}")
        print("Endereço:")
        print(f"  Logradouro: {usuario['endereco']['logradouro']}")
        print(f"  Nº: {usuario['endereco']['numero']}")
        print(f"  Bairro: {usuario['endereco']['bairro']}")
        print(f"  Cidade: {usuario['endereco']['cidade']}")
        print(f"  Estado: {usuario['endereco']['estado']}")
        print("=" * 30)
    else:
        print("Usuário não encontrado.")
        

    
if __name__ == "__main__":
    main()