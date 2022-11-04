# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)

soma = n = contador = 0

while True:
    n = int(input('Digite um número (999 para encerrar): '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'A soma de todos os números inseridos dá: {soma} e teve {contador} números inseridos')
