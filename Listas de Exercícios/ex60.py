# Faça um programa que leia um número qualquer e mostre o seu fatorial
# EX: fatorial de 5 => 5! = 5*4*3*2*1 = 120

num = 0
fatorial = 1

while num != -1:

    num = int(input('Insira um número para o fatorial: '))

    for p in range(num, 0, -1):
        fatorial = fatorial * p

    print(f'O fatorial de {num} é igual a {fatorial}')

    fatorial = 1
