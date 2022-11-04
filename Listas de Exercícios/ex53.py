# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input('Insira uma frase para ver se ela é um palíndromo:\n')).strip().upper()

frase_mod = frase.replace(' ', '')
frase_reverte = frase_mod[::-1]

if frase_mod == frase_reverte:
    print(f'"{frase}" é um palíndromo')
else:
    print(f'"{frase}" não é um palíndromo')
