# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

print('Os números pares são:')
for c in range(1, 51):
    if c % 2 == 0:
        if c == 50:
            print(f'{c}.')
        else:
            print(f'{c}, ', end='')

print('\nE os ímpares são:')
for c in range(1, 51):
    if c % 2 != 0:
        if c == 49:
            print(f'{c}.')
        else:
            print(f'{c}, ', end='')
