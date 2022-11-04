# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento

produto = str(input('Qual o produto?\n')).strip()
valor_prod = float(input('Qual o valor do produto?\n'))
tipo_de_pag = int(input("""FORMAS DE PAGAMENTO

À VISTA no dinheiro/cheque --> Digite 1
À VISTA no cartão          --> Digite 2
Em 2x no cartão            --> Digite 3
Em 3x ou mais no cartão    --> Digite 4
"""))

if tipo_de_pag != 1 and tipo_de_pag != 2 and tipo_de_pag != 3 and tipo_de_pag != 4:
    print('Valor inserido não disponível')
elif tipo_de_pag == 1:
    valorfinal = valor_prod * 0.9
    print(f'Com o desconto o produto {produto} ficará pelo valor de R${valorfinal:.2f}')
elif tipo_de_pag == 2:
    valorfinal = valor_prod * 0.95
    print(f'Com o desconto o produto {produto} ficará pelo valor de R${valorfinal:.2f}')
elif tipo_de_pag == 3:
    print(f'O produto {produto} ficará pelo valor de R${valor_prod:.2f}')
elif tipo_de_pag == 4:
    valorfinal = valor_prod * 1.2
    print(f'O produto {produto} terá 20% de juros, portanto ficará pelo valor de R${valorfinal:.2f}')