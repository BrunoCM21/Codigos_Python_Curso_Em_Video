# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from operator import itemgetter
from random import randint
dado = dict()
lista_dado = list()

for q in range(0, 4):
    nome = str(input('Digite o seu nome: ')).strip().title()
    valor_dado = randint(1, 6)
    dado['nome'] = nome
    dado['numero_dado'] = valor_dado

    lista_dado.append(dado.copy())

lista_dado_organizado = sorted(lista_dado, key=itemgetter("numero_dado"), reverse=True)
print('Os dados em ordem: ')

for d in lista_dado_organizado:
    for k, v in d.items():
        if k == 'nome' and d == 0:
            print(f'O ganhador foi o {v}! PARABÉNS!!!')
        if k == 'nome':
            print(f'\nNome = {v}; ', end='')
        if k == 'numero_dado':
            print(f'Número do Dado: {v}')
