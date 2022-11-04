# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é maior
import time


def maior(*num):  # O * significa que irá desempacotar o conteúdo
    cont = maior = 0
    print('\n\nAnalisando...')
    time.sleep(2)
    for n in num:
        print(f'{n}', end=' ', flush=True)
        time.sleep(0.3)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'\nForam informados {cont} valores ao todo, e o maior deles é o {maior}')


valoranterior = 0

# Programa Principal
maior(1, 4, 7, 10, 9)
maior(2, 7, 0)
maior(9, 1, 21, 3)
