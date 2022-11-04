# Faça um programa que leia um ano e mostre se ele é BISSEXTO
from datetime import date

ano = int(input('Entre com um ano para ver se ele é BISSEXTO: (Digite 0 se quiser inserir a data atual)\n'))
if ano == 0:
    ano = date.today().year

while True:
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                print('É ANO BISSEXTO!')
            else:
                print('NÃO É ANO BISSEXTO!')
        else:
            print('É ANO BISSEXTO!')
    else:
        print('NÃO É ANO BISSEXTO!')

    denovo = str(input('Gostaria de inserir outro ano para confirmar se é bissexto? (Y ou N)\n')).upper()

    if denovo == 'Y':
        ano = int(input('Entre com um ano para ver se ele é BISSEXTO: \n'))
    else:
        print('Obrigado por jogar!!!')
        break
