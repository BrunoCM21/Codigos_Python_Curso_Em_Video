# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela

aluno = dict()
lista_alunos = list()

while True:
    nome = str(input('Nome: ')).strip().title()
    media = float(input(f'Digite a média de {nome}: '))

    aluno['nome'] = nome
    aluno['media'] = media
    if media >= 7.00:
        aluno['situacao'] = 'Aprovado(a)'
    elif media < 7.00:
        aluno['situacao'] = 'Reprovado(a)'

    lista_alunos.append(aluno.copy())

    sn = str(input('Gostaria de continuar? S/N ')).strip().lower()
    while sn not in 'sn':
        sn = str(input('Resposta INVÁLIDA!!! Gostaria de continuar? S/N ')).strip().lower()
    if sn == 'n':
        break

for a in lista_alunos:
    for k, v in a.items():
        if k == 'nome':
            print(f'{v} está com média: ', end='')
        if k == 'media':
            print(f'{v} e está ', end='')
        if k == 'situacao':
            print(f'{v.upper()}')