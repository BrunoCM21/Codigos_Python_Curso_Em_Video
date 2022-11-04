# Crie uma tupla preenchida com os 20 primeiros colocados do Campeonato Brasileiro, na ordem de colocação.
# Depois mostre:
# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time da Chapecoense

times = ('São Paulo', 'Vasco', 'Flamengo', 'Palmeiras', 'Corinthians', 'Chapecoense', 'Santos', 'Red Bull Bragantino',
         'Grêmio', 'Internacional', 'Bahia', 'Goiás', 'Vitória', 'ABC de Natal', 'Criciúma', 'Cruzeiro',
         'Athlético Paranaense', 'Atlético Mineiro', 'América Mineiro', 'Cuiabá')

# print(f'Os primeiros colocados são {times[0:5]}')  # --> Uma forma de colocar

print('Os primeiros colocados são: ', end='')
for cont in range(0, 5):
    if cont == 4:
        print(f'{times[cont]}.', end='')
    else:
        print(f'{times[cont]}, ', end='')


print('\n\nOs 4 últimos colocados são: ', end='')
for contagem in range(len(times)-4, len(times)):
    if contagem == len(times)-1:
        print(f'{times[contagem]}.', end='')
    else:
        print(f'{times[contagem]}, ', end='')

times_ordenado = sorted(times)
print(f'\n\nOs times ordenados ficam: {times_ordenado}')

for localiza in range(0, len(times)):
    if 'Chapecoense' == times[localiza]:
        print(f'\nA Chapecoense está em {localiza}º')