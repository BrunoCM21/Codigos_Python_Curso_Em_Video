# Crie um programa que leia dois valores e mostre um menu na tela:
# (1) Somar
# (2) Multiplicar
# (3) Maior
# (4) Novos Números
# (5) Sair
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep

menu = -100
maior = 0
menor = 0

valor1 = float(input('Insira um primeiro valor: '))
valor2 = float(input('Insira um segundo valor: '))

while menu != 5:

    print("""    (1) Somar
    (2) Multiplicar
    (3) Maior
    (4) Novos Números
    (5) Sair""")

    menu = int(input('Insira a escolha: '))

    if menu == 1:
        soma = valor1 + valor2
        print(f'A soma vale {soma}')
    elif menu == 2:
        mult = valor1 * valor2
        print(f'A multiplicação vale {mult}')
    elif menu == 3:
        if valor1 > valor2:
            maior = valor1
            menor = valor2
            print(f'{maior} é maior que {menor}')
        elif valor2 > valor1:
            maior = valor2
            menor = valor1
            print(f'{maior} é maior que {menor}')
        else:
            print('São iguais')
    elif menu == 4:
        valor1 = float(input('Insira um primeiro valor: '))
        valor2 = float(input('Insira um segundo valor: '))
    elif menu != -100:
        if menu != 1:
            if menu != 2:
                if menu != 3:
                    if menu != 5:
                        if menu != 4:
                            print('Valor inválido!!!!')

    sleep(1.5)

print('-'*6, 'Saindo', '-'*6)
sleep(1.5)
