# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido

peso_comp = []
mais_leve = 0
mais_pesado = 0
nome_leve = 'Vazio'
nome_pesado = 'Vazio'

for c in range(0, 5):

    nome = str(input('Insira seu nome: ')).strip().title()
    peso = float(input('Digite o seu peso em Kg: '))

    peso_comp.append(peso)

    if peso_comp[0] == peso:
        nome_leve = nome
        nome_pesado = nome
        mais_leve = peso
        mais_pesado = peso
    elif peso_comp[c-1] > peso:
        mais_leve = peso
        nome_leve = nome
    elif peso_comp[c-1] < peso:
        mais_pesado = peso
        nome_pesado = nome

    print('\n')

print('A pessoa mais magra é {} com {} Kg'.format(nome_leve, mais_leve))
print('E a pessoa mais gorda é {} com {} Kg'.format(nome_pesado, mais_pesado))
