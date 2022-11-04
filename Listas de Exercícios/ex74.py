# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

num_random = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

for compara in range(0, len(num_random)):
    if compara == 0:
        maior = num_random[compara]
        menor = num_random[compara]
    elif num_random[compara] > maior:
        maior = num_random[compara]
    elif num_random[compara] < menor:
        menor = num_random[compara]

print(f'Os números aleatórios gerados são:', end='')
for cont in range(0, len(num_random)):
    if cont == len(num_random)-1:
        print(f'{num_random[cont]}.')
    elif cont == len(num_random)-2:
        print(f' {num_random[cont]} e ', end='')
    else:
        print(f' {num_random[cont]},', end='')

# print(max(num_random))
# print(min(num_random))
# Esses métodos são usados nas tuplas para achar o menor e o maior número

print(f'O maior número gerado é {maior} e o menor número gerado é {menor}')