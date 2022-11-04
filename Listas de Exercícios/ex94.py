# Crie um programa que leia nome, sexo, e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média

pessoas = dict()
lista_pessoas = lista_mulheres = lista_acima_da_media = list()
soma_idade = 0


while True:
    pessoas['Nome'] = str(input('Digite seu nome: ')).strip().title()
    pessoas['Sexo'] = str(input('Digite seu sexo: (M ou F) ')).strip().upper()[0]
    while pessoas['Sexo'] not in 'MF':
        pessoas['Sexo'] = str(input('Valor INVÁLIDO!!!! Digite seu sexo: (M ou F) ')).strip().upper()
    pessoas['Idade'] = int(input('Digite sua idade: '))
    soma_idade += pessoas['Idade']

    lista_pessoas.append(pessoas.copy())

    sn = str(input('Gostaria de continuar? S/N ')).strip().lower()
    while sn not in 'sn':
        sn = str(input('Resposta INVÁLIDA!!! Gostaria de continuar? S/N ')).strip().lower()
    if sn == 'n':
        break

total_pessoas = len(lista_pessoas)
print(f'Houve {total_pessoas} cadastradas')


media_idade = soma_idade / len(lista_pessoas)
print(f'A média de idade das pessoas é de {media_idade:5.2f} anos')

print('As mulheres cadastradas foram: ')
for pp in lista_pessoas:
    if pp['Sexo'] in 'F':
        print(f'{pp["Nome"]}, ', end='')

print('As pessoas mais velhas que a média de idade são: ')
for ff in lista_pessoas:
    if ff['Idade'] > media_idade:
        print(f'{ff["Nome"]}, ', end='')