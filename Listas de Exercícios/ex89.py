# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente

lista = []
contador = 0

while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = int(input('Nota 1: '))
    while nota1 < 0 or nota1 > 10:
        nota1 = int(input('Nota 1 inválida, insira uma nota válida: '))
    nota2 = int(input('Nota 2: '))
    while nota2 < 0 or nota2 > 10:
        nota2 = int(input('Nota 2 inválida, insira uma nota válida: '))

    lista.append(list())
    lista[contador].append(nome)
    lista[contador].append(nota1)
    lista[contador].append(nota2)

    contador += 1

    sn = str(input('Gostaria de continuar? S/N ')).strip().lower()
    while sn not in 'sn':
        sn = str(input('Resposta INVÁLIDA!!! Gostaria de continuar? S/N ')).strip().lower()
    if sn == 'n':
        break

print('\n')
print('='*32)
print(f'|No.| NOME          | MÉDIA    |')
insert = -1

for cont in range(0, len(lista)):

    media = (lista[cont][1] + lista[cont][2]) / 2
    print(f'|{cont:^3}| {lista[cont][0]:<14}| {media:<9}|')

print('='*32)

while insert != 999:

    insert = int(input('Mostrar notas de qual aluno? (999 interrompe)\n'))
    print(f'{lista[insert][0]} possui as notas {lista[insert][1]} e {lista[insert][2]}\n')
