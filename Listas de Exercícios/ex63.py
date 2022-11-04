# Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os n primeiros elementos de uma
# Sequência de Fibonacci
# Ex -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
# P.S.: Eu não tive ideia de como fazia esse exercício, portanto deixei p fazer com o prof

n = int(input('Quantos termos da sequência de Fibonnacci você quer mostrar? '))

t1 = 0
t2 = 1
contador = 1
print(f'{t1} --> {t2}', end='')
contador = 3

while contador <= n:
    t3 = t1 + t2
    print(f' --> {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1

