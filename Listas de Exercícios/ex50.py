# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o

soma = 0
cont = 0

for p in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
        print(f'{num} é par\n')
    else:
        print(f'{num} é ímpar\n')

print('A soma de todos os números pares inseridos é de {}'.format(soma), end=' ')
print('e a quantidade de números pares é: {}'.format(cont))
