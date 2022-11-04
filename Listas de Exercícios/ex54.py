# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores

from datetime import date

ano_atual = date.today().year
contador = 0

for n in range(0, 7):
    ano_nasc = int(input('Digite seu ano de nascimento: '))

    idade = ano_atual - ano_nasc

    if ano_nasc > ano_atual:
        print('Ano inserido é inválido')
        n = n - 1

    if idade >= 21:
        if idade == 21:
            print('Maioridade atingida')
            contador = contador + 1
        elif idade > 21:
            print('Maioridade ultrapassada')
            contador = contador + 1
        elif idade < 21:
            print('A maioridade ainda não foi atingida')

print(f'Teve {contador} pessoas com idade maior de 21 anos!!')

print('\n')
