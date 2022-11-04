# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1250.00, calcule um aumento de 10% e para os inferiores ou iguais um aumento de 15%

salario = float(input('Digite seu salário: (Ex: 1000.00) \n'))

if salario > 1250.00:
    calculo = salario * 1.10
    print(f'O novo salário será de {calculo}')
else:
    calculo = salario * 1.15
    print(f'O novo salário será de {calculo}')
