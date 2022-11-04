# Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
# início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1.
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada

def contador(escolha):
    if escolha == 1:
        print('Você escolheu uma contagem de 1 a 10 padrão')
        for a in range(1, 10 + 1):
            print(f'{a}')
    elif escolha == 2:
        print('Você escolheu uma contagem de 10 a 0 de 2 em 2')
        for a in range(10, 0 - 1, -2):
            print(f'{a}')
    else:
        print('Você escolheu uma contagem personalizada!')
        minimo = int(input('Qual o começo da contagem? '))
        maximo = int(input('Qual o final da contagem? '))
        qnto = int(input('De quanto em quanto você gostaria que a contagem funcionasse(insira só o número)? '))
        if maximo > 0:
            if qnto < 0:
                for a in range(minimo, maximo + 1, qnto * (-1)):
                    print(f'{a}')
            else:
                for a in range(minimo, maximo + 1, qnto):
                    print(f'{a}')
        else:
            if qnto < 0:
                for a in range(minimo, maximo - 1, qnto * (-1)):
                    print(f'{a}')
            else:
                for a in range(minimo, maximo - 1, qnto):
                    print(f'{a}')


print("""Escolha a opção apropriada para a contagem que você deseja:
    1) De 1 até 10, de 1 em 1.
    2) De 10 até 0, de 2 em 2
    3) Uma contagem personalizada""")
escolha = int(input())
while escolha <= 0 or escolha >= 4:
    escolha = int(input('Valor inválido, escolha outro: '))
contador(escolha)
