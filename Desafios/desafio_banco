from time import sleep
sleep(0.5)
menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu).lower().strip()

    if opcao == 'd':
        sleep(0.5)
        print('Deposito')
        valor = float(input('Valor do deposito: R$'))
        if valor > 0:
            saldo += valor
            sleep(0.5)
            print('Deposito feito com Sucesso.')
        else:
            print('Não pode ser feito deposito de valores negativos.')

    elif opcao == 's':
        sleep(0.5)
        print('Saque')
        saque = float(input('Valor do Saque: R$'))

        if numero_saques >= LIMITE_SAQUES:
            sleep(0.5)
            print(f'O limite diario de saques é de {LIMITE_SAQUES}. ')
        elif saque > limite:
            sleep(0.5)
            print(f'O limite por saque é de {limite}')
        elif saque > saldo:
            sleep(0.5)
            print(f'Saldo Insuficiente...')
        else:
            numero_saques += 1
            saldo -= saque
            extrato += f'Saques: R${saque:.2f}\n'
            sleep(0.5)
            print('Saque efetuado com sucesso...')

    elif opcao == 'e':
        sleep(0.5)
        print('Extrato')
        print(f'Saldo: R${saldo:.2f}\nNumero de Saques: {numero_saques}\n{extrato}')

    elif opcao == 'q':
        print('Saindo...')
        sleep(1)
        break
    else:
        sleep(0.5)
        print('Operação invalida,por favor selecione novamente a operação desejada.')

print('Volte Sempre!!!')
