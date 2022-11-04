# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas;
# - A maior nota;
# - A menor nota;
# - A média da turma;
# - A situação(opcional).
# Adicione também as docstrings da função

def notas_function(*notas, situacao=False):
    """--> Faz uma análise completa das notas passadas, apresentando através de um dicionário os dados de
    Quantidade de Notas, a Maior e Menor Nota, a Média da Turma e a Situação da sala.
    :param notas: recebe todas as notas
    :param situacao: é opcional, porém a sua função é apresentar qual o estado de aprendizado da sala de aula

    :return: retorna um dicionário com diversos dados (Quantidade de Notas, a Maior e Menor Nota, a Média da Turma e a
    Situação da sala)
    """
    maior = menor = soma = contador = 0
    dicts = dict()
    for n in notas:
        soma += n
        if contador == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        contador += 1
    media = soma/contador

    dicts['Quantidade de Notas'] = contador
    dicts['Maior Nota'] = maior
    dicts['Menor Nota'] = menor
    dicts['Média da Sala'] = media
    if situacao:
        if media > 9:
            dicts['Situação'] = 'Ótima'
        elif media > 8:
            dicts['Situação'] = 'Boa'
        elif media > 6:
            dicts['Situação'] = 'Na Média'
        elif media > 4:
            dicts['Situação'] = 'Ruim'
        elif media > 2:
            dicts['Situação'] = 'Horroroso'

    return dicts


print('-'*30)

dictnotas = notas_function(3, 5, 9, 10, 3, 2, 7, 7, situacao=True)
for k, v in dictnotas.items():
    print(f'{k}: {v}')

print('-'*30)

dictnotas = notas_function(1, 4, 7, 9, 10, 8, 5, 7, 9, situacao=False)
for k, v in dictnotas.items():
    print(f'{k}: {v}')

print('-'*30)

help(notas_function)