# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto

num = 1
Valido = False
contador = 0
sexo = 'p'

while sexo != '0':
    sexo = str(input('Digite seu sexo (M ou F) ou 0 para encerrar app: ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        contador = contador + 1
        print(f'Sexo {sexo} registrado com sucesso')
    elif sexo == 'p':
        print('', end='')
    else:
        print('Valor Inválido!!', end=' ')
        sexo = str(input('Digite seu sexo (M ou F) corretamente, ou 0 para encerrar app: ')).strip().upper()


print(f'Teve {contador} valores válidos inseridos!')
