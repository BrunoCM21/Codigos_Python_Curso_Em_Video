# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

from time import sleep
from datetime import date


def voto(a):
    if a < 16:
        return 'NEGADO'
    elif a == 16 and a < 18:
        return 'OPCIONAL'
    elif a >= 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


datanasc = int(input('Qual seu ano de nascimento?\n'))
ano_atual = date.today().year
idade = ano_atual - datanasc
retorno = voto(idade)
sleep(2)
print(f'A pessoa possui {idade} anos e o voto dela é {retorno}')
