# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas células de cada valor serão entregues.
# Obs. Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1

print('='* 40)
print(' '*11+'BANCO BRUNIN DOIDO'+' '*11)
print('='* 40)

valor_sacado = int(input('Qual o valor a ser sacado? R$'))
valor_final50 = valor_final20 = valor_final10 = valor_final1 = 0
valor_da_divisao = 1

print('\n')

while True:

    valor_da_divisao = valor_sacado // 50
    valor_final50 = valor_sacado - (valor_da_divisao * 50)

    if valor_da_divisao != 0:
        print(f'Se teve {valor_da_divisao} notas de R$50,', end='')

    if valor_final50 == 0:
        break

    valor_da_divisao = valor_final50 // 20
    valor_final20 = valor_final50 - (valor_da_divisao * 20)

    if valor_da_divisao != 0:
        print(f' {valor_da_divisao} notas de R$20,', end='')

    if valor_final20 == 0:
        break

    valor_da_divisao = valor_final20 // 10
    valor_final10 = valor_final20 - (valor_da_divisao * 10)

    if valor_da_divisao != 0:
        print(f' {valor_da_divisao} notas de R$10', end='')

    if valor_final10 == 0:
        break

    valor_da_divisao = valor_final10 // 1
    valor_final1 = valor_final10 - (valor_da_divisao * 1)

    if valor_da_divisao != 0:
        print(f' e {valor_da_divisao} notas de R$1.', end='')
    print('\n')

    if valor_final1 == 0:
        break
