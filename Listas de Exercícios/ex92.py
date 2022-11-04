# Crie um programa que leia nome, ano de nascimento e carteira de trabalho previdência social e cadastre-os (com idade)
# em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

pessoa = dict()
ano_atual = date.today()
ano_contratacao = 0

pessoa['Nome'] = str(input('Digite seu nome: ')).strip().title()

ano_nasc = int(input('Insira seu ano de nascimento: '))
idade = ano_atual.year - ano_nasc
pessoa['Idade'] = idade

ctps = int(input('Insira o número da sua carteira de trabalho (0 indica que não tem): '))
if ctps == 0:
    pessoa['Carteira de Trabalho e Previdência Social'] = 'Não Possui'
else:
    pessoa['Carteira de Trabalho e Previdência Social'] = ctps
    ano_contratacao = int(input('Insira o seu ano de contratação: '))
    pessoa['Ano de Contratação'] = ano_contratacao

    pessoa['Salário'] = int(input('Insira o seu salário: '))

    tempo_de_contribuicao = ano_atual.year - ano_contratacao
    pessoa['Tempo de Contribuição'] = tempo_de_contribuicao

print('')
for k, v in pessoa.items():
    if k == 'Salário':
        print(f'{k}: R${v:.2f}')
    elif k == 'Tempo de Contribuição' or k == 'Idade':
        print(f'{k}: {v} anos')
    else:
        print(f'{k}: {v}')