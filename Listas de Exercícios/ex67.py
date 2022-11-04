# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo

num = 0

while True:
    num = int(input('Insira um número para a tabuada: '))
    if num < 0:
        print('Número negativo inserido, ENCERRANDO APLICAÇÃO')
        break

    print('\n')
    print('-' * 3 + 'Tabuada' + '-' * 3)

    for f in range(0, 11):
        tab = num * f

        print(f' {num} x {f:2} = {tab}')

    print('-' * 13)
