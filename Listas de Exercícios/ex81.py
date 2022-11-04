# Crie um programa que leia vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont_add = 0
o_cinco = -1

while True:
    nums = int(input('Digite um número: '))
    lista.append(nums)
    cont_add += 1

    for l in lista:
        if l == 5:
            o_cinco = lista.index(5)

    sn = str(input('Gostaria de continuar(S/N)? ')).strip().lower()
    while sn not in 'sn':
        sn = str(input('Resposta INVÁLIDA!!! Gostaria de continuar(S/N)? ')).strip().lower()
    if sn == 'n':
        break

lis = lista
lista.sort(reverse=True)

print(f'A lista de forma decrescente fica: {lis}')

if o_cinco == -1:
    print('Não possui 5 na lista')
else:
    print(f'Existe 5 e está na posição {o_cinco} da lista')

if cont_add == 1:
    print('Teve 1 número inserido')
else:
    print('Teve {} números inseridos'.format(cont_add))