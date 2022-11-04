# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número para saber se é primo ou não: '))

primo = False
r = 0

for r in range(2, num+1):
    if num % r == 0:
        if num == r:
            primo = True
            break
        primo = False
        break
    else:
        primo = True

if primo is True:
    print(f'{num} é um número primo, pois é divisível apenas por 1 e por ele mesmo')
else:
    print(f'{num} não é primo pois é dividido por {r} que da zero como sobra')
