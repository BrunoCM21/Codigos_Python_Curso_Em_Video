# Escreva um programa para aprovar empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar

valor_casa = float(input('Qual o valor da casa para o financiamento?\n'))
salario_comp = float(input('Qual o salário do comprador?\n'))
anos = int(input('Em quantos anos o valor será pago?\n'))

meses = anos * 12


valor_prestacao = valor_casa / meses
valor_max_salario = 0.30 * salario_comp

if valor_prestacao > valor_max_salario:
    print('Pedido negado, a prestação ultrapassa o valor máximo mensal!!!')
elif valor_prestacao <= valor_max_salario:
    print('Seu pedido foi aprovado!!!')

