# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valor0 = int(input('Digite um valor para a Posição 0: '))
valor1 = int(input('Digite um valor para a Posição 1: '))
valor2 = int(input('Digite um valor para a Posição 2: '))
valor3 = int(input('Digite um valor para a Posição 3: '))
valor4 = int(input('Digite um valor para a Posição 4: '))

lista = [valor0, valor1, valor2, valor3, valor4]
print(f'Você digitou os valores {lista}')

maior = max(lista)
menor = min(lista)

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for contador in range(0, 5):
    if lista[contador] == menor:
        posicao = lista.index(menor, contador)
        print(f'{posicao}...', end=' ')

print(f'\nO maior valor digitado foi {maior} nas posições ', end='')
for contador in range(0, 5):
    if lista[contador] == maior:
        posicao = lista.index(maior, contador)
        print(f'{posicao}...', end=' ')
