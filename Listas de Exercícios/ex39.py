# Faça um programa que leia o ano de nascimento de uma pessoa e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# Além de mostrar o tempo que falta ou que passou do prazo

import emoji
import datetime

ano_de_nasc = int(input('Qual seu ano de nascimento? \n'))
ano = datetime.date.today().year

tempo = ano - ano_de_nasc

if ano_de_nasc > ano:
    print('Para de querer trollar FDP, sai daqui!!!!')
elif tempo < 18:
    falta = 18 - tempo
    if falta == 1:
        print('Você tem {} anos e ainda irá se alistar, falta {} ano ainda'.format(falta))
    else:
        print('Você tem {} anos e ainda irá se alistar, faltam {} anos ainda'.format(falta))
elif tempo == 18:
    print(emoji.emojize('Está na hora de você se alistar e se juntar ao exército do país :thumbsup:', use_aliases=True))
elif tempo > 18:
    falta = tempo - 18
    if falta == 1:
        print('Se você ainda não se alistou, já está atrasado por {} ano'.format(falta))
    else:
        print('Se você ainda não se alistou, já está atrasado por {} anos'.format(falta))
