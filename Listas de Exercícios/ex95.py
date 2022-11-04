# Aprimore o ex93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

jogador = dict()
gols = list()
soma = 0
rodada = 1
codigo = -1
lista_jogadores = list()

while True:
    jogador['Nome'] = str(input('Digite o nome do jogador: ')).strip().title()
    jogador['Partidas'] = int(input('Quantas partidas ele jogou na temporada? '))

    for p in range(1, jogador['Partidas']+1):
        gol = int(input('   Quantos gols o jogador fez na {}a. rodada? '.format(p)))
        soma += gol
        gols.append(gol)

    jogador['Soma'] = soma
    jogador['Gols'] = gols[:]

    lista_jogadores.append(jogador.copy())

    gols.clear()
    soma = 0

    sn = str(input('Gostaria de continuar? S/N ')).strip().lower()
    while sn not in 'sn':
        sn = str(input('Resposta INVÁLIDA!!! Gostaria de continuar? S/N ')).strip().lower()
    if sn == 'n':
        break

while True:
    print('=' * 70)
    print('cod ', end='')
    for i in jogador.keys():
        print(f'{i:<15}', end='')
    print()
    print('=' * 70)
    for k, v in enumerate(lista_jogadores):
        print(f'{k:>3} ', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
    print('=' * 70)

    codigo = int(input('Escolha o código do jogador: (999 p/ encerrar) '))
    if codigo == 999:
        print('ENCERRANDO APLICAÇÃO!!!')
        break
    elif codigo >= len(lista_jogadores):
        print('ERRO!!! Código não existe.')
    else:
        print(f'JOGADOR --> {lista_jogadores[codigo]["Nome"]}: ')
        for rodada, golss in enumerate(lista_jogadores[codigo]['Gols']):
            print(f'Fez {golss} gols na rodada {rodada + 1}')
