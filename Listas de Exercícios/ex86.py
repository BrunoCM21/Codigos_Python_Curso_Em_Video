# Crie um programa que crie uma matriz de dimensão 3x3 e prencha com valores lidos pelo teclado
# No final, mostre a matriz na tela, com a formatação correta

lista = []
contador = 0

for linha in range(1, 4):
    for coluna in range(1, 4):
        num = int(input(f'Insira um número para a linha {linha} e coluna {coluna}: '))
        lista.append(num)


for coluna in range(1, 4):
    for linha in range(1, 4):
        if linha == 3:
            print(f'|{lista[contador]:^7}| ')
        else:
            print(f'|{lista[contador]:^7}| ', end='')
        contador += 1