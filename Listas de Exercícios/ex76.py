# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular

nomes_precos = ('Monitor', 399.99, 'Computador', 2999.99, 'Mouse', 99.99, 'Celular', 1500.00, 'Máscara', 10.00,
                'Papel Higiênico', 25.00, 'Cabo de Internet', 50.00, 'Fone de Ouvido Intrauricular', 70.00,
                'Bateria de Computador', 326.75, 'Caixa de Som Bluetooth', 750.00, 'Ventilador', 150.00)
final = quantidade = 0

print('='*50)
print(' '*16+'LISTAGEM DE PREÇOS'+' '*16)
print('='*50)
for contador in range(0, len(nomes_precos)):

    if contador % 2 == 0:
        if nomes_precos[contador + 1] - 10 < 0:
            quantidade = quantidade + len(nomes_precos[contador]) + 6
        elif nomes_precos[contador+1] - 100 < 0:
            quantidade = quantidade + len(nomes_precos[contador]) + 7
        elif nomes_precos[contador+1] - 1000 < 0:
            quantidade = quantidade + len(nomes_precos[contador]) + 8
        elif nomes_precos[contador + 1] - 10000 < 0:
            quantidade = quantidade + len(nomes_precos[contador]) + 9
        elif nomes_precos[contador + 1] - 100000 < 0:
            quantidade = quantidade + len(nomes_precos[contador]) + 10

    final = 50 - quantidade

    if contador % 2 == 0:
        print(f'{nomes_precos[contador]}', end='')
        print('.'*final, end='')
        print(f'R${nomes_precos[contador+1]:.2f}')

    final = quantidade = 0

print('='*50)