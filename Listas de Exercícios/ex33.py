# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Insira um número:\n'))
n2 = int(input('Insira mais um número:\n'))
n3 = int(input('Insira mais outro número:\n'))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior')
else:
    if n2 > n3 and n2 > n1:
        print(f'{n2} é o maior')
    else:
        if n3 > n2 and n3 > n1:
            print(f'{n3} é o maior')
        else:
            print('Tem 2 números maiores iguais')

if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor')
else:
    if n2 < n3 and n2 < n1:
        print(f'{n2} é o menor')
    else:
        if n3 < n2 and n3 < n1:
            print(f'{n3} é o menor')
        else:
            print('Tem dois números menores iguais')

if n1 == n2 and n1 == n3:
    print(f'São todos iguais {n1}')
else:
    if n1 == n2:
        print(f'Tem-se dois números {n1}')
    else:
        if n2 == n3:
            print(f'Tem-se dois números {n2}')
        else:
            if n1 == n3:
                print(f'Tem-se dois números {n1}')
