# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida

nota1 = float(input('Qual sua primiera nota? \n'))
nota2 = float(input('Qual sua segunda nota? \n'))

media = (nota1 + nota2) / 2

if media < 0 or media > 10:
    print('Erro no sistema')
elif media < 5.0:
    print('REPROVADO')
elif 5.0 <= media < 7.0:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')
