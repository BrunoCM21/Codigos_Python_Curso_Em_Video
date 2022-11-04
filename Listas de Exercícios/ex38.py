# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, ambos são iguais

num1 = int(input('Insira um número: \n'))
num2 = int(input('Insira outro número: \n'))

if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior nem menor, ambos são iguais')
