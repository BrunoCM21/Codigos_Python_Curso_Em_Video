# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares.
# No final mostre os valores pares e ímpares em ordem crescente

lista = [[], []]

for cont in range(1, 8):
    num = int(input(f'Digite o {cont}º valor: '))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[1].sort()
lista[0].sort()

print('='*20)
print(f'A lista de números pares é: {lista[0]}')
print(f'A lista de números ímpares é: {lista[1]}')
print('='*20)