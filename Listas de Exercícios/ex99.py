# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é maior

def maior(valor, valoranterior):
    if valor >= valoranterior:
        maior_var = valor

        return maior_var


valoranterior = 0

while True:
    valor = int(input('Insira um valor: '))
    sn = str(input('Gostaria de continuar? S/N ')).strip().lower()
    maior_var = maior(valor, valoranterior)
    valoranterior = valor
    while sn not in 'sn':
        sn = str(input('Resposta INVÁLIDA!!! Gostaria de continuar? S/N ')).strip().lower()
    if sn == 'n':
        break

print(f'O maior número inserido foi: {maior_var}')
