# Crie um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nomeficha='<desconhecido>', golsficha=0):
    print(f'{nomeficha} fez {golsficha} gols na temporada')


nome = str(input('Qual o nome do jogador?\n'))
gols = str(input('Quantos gols o jogador fez?\n'))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(golsficha=gols)
else:
    ficha(nome, gols)

ficha(golsficha=3)
ficha(nomeficha='Bruno')