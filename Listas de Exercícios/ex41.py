# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade

# import datetime
from datetime import date

print("""A Confederação Nacional de Natação pede que 
coloque sua data de nascimento para saber em que categoria você se 
encaixa para as competições nacionais de natação
(-1 encerra a aplicação)""")

ano = date.today().year

while True:
    ano_nasc = int(input('Ano --> '))

    idade = ano - ano_nasc

    if ano_nasc == -1:
        print(f'--Obrigado--')
        break
    elif idade <= 9:
        print('Mirim')
    elif idade <= 14:
        print('Infatil')
    elif idade <= 19:
        print('Junior')
    elif idade <= 20:
        print('Sênior')
    elif idade > 20:
        print('Master')
    elif idade < 0:
        print('Idade Inválida')

    print(f'O atleta tem {idade} anos')
