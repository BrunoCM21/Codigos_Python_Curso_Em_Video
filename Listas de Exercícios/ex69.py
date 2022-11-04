# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos

contador_mulher_menor_de_vinte = 0
contador_maior_de_18 = 0
contador_de_homem = contador = 0

while True:

    sexo = str(input('Digite seu sexo (F ou M): ')).strip().upper()
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Digite o sexo válido (F ou M): ')).strip().upper()

    idade = int(input('Digite sua idade: '))
    while idade < 0:
        idade = int(input('Idade inválida, digite sua idade: '))

    if idade >= 18:
        contador_maior_de_18 += 1

    if sexo == 'M':
        contador_de_homem += 1

    if sexo == 'F' and idade < 20:
        contador_mulher_menor_de_vinte += 1

    mais = str(input('Deseja cadastrar mais (S ou N)? ')).strip().upper()
    while mais != 'N' and mais != 'S':
        mais = str(input('Valor inválido, insira o valor válido para caso deseja cadastrar mais (S ou N): ')).strip().upper()

    contador += 1

    if mais == 'N':
        break

print('\n')

if contador_maior_de_18 >= 2:
    print(f'Possuem {contador_maior_de_18} pessoas cadastradas que são maiores de 18 anos')
elif contador_maior_de_18 == 1:
    print(f'Possui {contador_maior_de_18} pessoa cadastrada que é maior de 18 anos')
else:
    print(f'Não possui nenhuma pessoa cadastrada com maior de 18 anos')

if contador_de_homem >= 2:
    print(f'Possuem {contador_de_homem} homens cadastrados')
elif contador_de_homem == 1:
    print(f'Possui {contador_de_homem} homem cadastrado')
else:
    print(f'Não possui homens cadastrados')

if contador_mulher_menor_de_vinte >= 2:
    print(f'Possuem {contador_mulher_menor_de_vinte} mulheres menores de 20 anos cadastradas')
elif contador_mulher_menor_de_vinte == 1:
    print(f'Possui {contador_mulher_menor_de_vinte} mulher menor de 20 anos cadastrada')
else:
    print('Não possui nenhuma mulher menor de vinte anos cadastrada')

if contador >= 2:
    print(f'Possuem {contador} pessoas cadastradas')
elif contador == 1:
    print(f'Possui {contador} pessoa cadastrada')
else:
    print('Não possui nenhuma pessoa cadastrada')

print('\nObrigado')
