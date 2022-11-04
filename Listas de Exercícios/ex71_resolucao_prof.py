print('=' * 40)
print(' ' * 11 + 'BANCO BRUNIN DOIDO' + ' ' * 11)
print('=' * 40)

valor_sacado = int(input('Qual o valor a ser sacado? R$'))
total = valor_sacado
ced = 50
totced = 0

print('\n')

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

print('VOLTE SEMPRE')

# O MEU EXERCÍCIO RESOLVIDO ESTAVA CORRETO, PORÉM DECIDI POR ESCREVER O DO PROFESSOR POIS ELE UTILIZOU DE OUTRA LÓGICA
