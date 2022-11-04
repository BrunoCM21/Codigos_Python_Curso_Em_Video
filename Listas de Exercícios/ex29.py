# Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado

velocidade = int(input('Qual a sua velocidade?\n'))

if velocidade > 80:
    print('VOCÊ FOI MULTADO!!!')
    acima = velocidade - 80
    multa = acima * 7.00
    print(f'E pagará uma multa de {multa:.2f} reais')
else:
    print('Você não foi multado, mas tenha cuidado no trânsito!')
