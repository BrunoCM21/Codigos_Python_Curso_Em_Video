# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

lista = []
soma_pares = soma_terceira_coluna = contador = maior = 0

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

        if lista[contador] % 2 == 0:
            soma_pares += lista[contador]

        if linha == 3:
            soma_terceira_coluna += lista[contador]

        if coluna == 2 and linha == 1:
            maior = lista[contador]
        if lista[contador] > maior and coluna == 2:
            maior = lista[contador]

        contador += 1

print(f'A soma dos números pares da {soma_pares} e a soma dos números da terceira coluna da {soma_terceira_coluna}')
print(f'Por fim, o maior número da 2ª linha é o {maior}')