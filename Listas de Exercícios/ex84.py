# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

from operator import itemgetter

dados = []
peso = []
nome = list()
contador = 0
mais_peso = menos_peso = 0
mais_peso_nome = ''

while True:
    dados.append(str(input('NOME: ')).strip().title())
    dados.append(float(input('PESO: ')))

    peso.append(dados[:][1])
    nome.append(dados[:])

    contador += 1

    sn = str(input('Gostaria de continuar? S/N ')).strip().lower()
    while sn not in 'sn':
        sn = str(input('Resposta INVÁLIDA!!! Gostaria de continuar? S/N ')).strip().lower()
    if sn == 'n':
        break

    dados.clear()


print(f'O mais leve é na ordem de {sorted(nome, key=itemgetter(1))}')

print(f'O mais pesado é na ordem de {sorted(nome, key=itemgetter(1), reverse=True)}')

print(f'Houve {contador} pessoas cadastradas')
