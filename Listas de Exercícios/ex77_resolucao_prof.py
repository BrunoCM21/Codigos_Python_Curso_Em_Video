palavras = ('Computador', 'Monitor', 'Celular', 'Mouse', 'Papel', 'Fio', 'Arroz')
contador = 0

for p in palavras:
    print(f'Na palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
        contador += 1

    print('\n')