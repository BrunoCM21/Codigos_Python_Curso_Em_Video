# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando a condição de parada)

valor = contador_de_digitados = soma = 0

while valor != 999:
    valor = int(input('Digite um número inteiro: '))

    soma = soma + valor

    if valor == 999:
        soma = soma - 999
        contador_de_digitados = contador_de_digitados - 1

    contador_de_digitados = contador_de_digitados + 1


print('A soma de todos os números é igual a {}'.format(soma), end='')
print(' e teve {} números digitados'.format(contador_de_digitados))

