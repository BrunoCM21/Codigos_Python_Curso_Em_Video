# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será  guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

jogador = dict()
gols = list()
soma = 0
rodada = 1

jogador['Nome'] = str(input('Digite o nome do jogador: ')).strip().title()
jogador['Partidas'] = int(input('Quantas partidas ele jogou na temporada? '))

for p in range(1, jogador['Partidas']+1):
    gol = int(input('Quantos gols o jogador fez na {}a. rodada? '.format(p)))
    soma += gol
    gols.append(gol)

jogador['Soma'] = soma

print('='*30)

print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas e fez {jogador["Soma"]} gols ao total')
print(f'As rodadas são:')
for marcado in gols:
    if marcado != 0:
        print(f'Fez {marcado} gols na rodada {rodada}')
    rodada += 1