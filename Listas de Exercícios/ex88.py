# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint

qtd = int(input('Quantos jogos da MEGA SENA serão criados? '))
lista = []

for criacao_de_listas_internas in range(0, qtd):
    lista.append(list())

for contagem_listas in range(0, len(lista)):
    for contagem_numeros_interno in range(0, 6):
        num = randint(0, 60)
        while num in lista[contagem_listas]:
            num = randint(0, 60)
        lista[contagem_listas].append(num)
    print(f'O {contagem_listas+1}º jogo da MEGA SENA é: {lista[contagem_listas]}')
