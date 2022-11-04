# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele que ou não continuar a
# digitar valores


valor = 0
contador_de_digitados = 0
soma = 0
val = []

while valor != 999:
    valor = int(input('Digite um número inteiro (999 p/ parar): '))

    if valor != 999:
        val.append(valor)

    soma = soma + valor

    if valor != 999:
        val.append(valor)
        if val[0] == valor:
            maior = valor
            menor = valor
        elif valor < menor:
            menor = valor
        elif valor > maior:
            maior = valor

    if valor == 999:
        soma = soma - 999
        contador_de_digitados = contador_de_digitados - 1

    contador_de_digitados = contador_de_digitados + 1

media = soma / contador_de_digitados

print('\nA média de todos os valores digitados é igual a {:.2f}'.format(media))
print(f'O maior valor foi {maior} e o menor foi {menor}')
