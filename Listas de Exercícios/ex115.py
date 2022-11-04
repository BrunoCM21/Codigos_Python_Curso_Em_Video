# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo .txt simples
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
def mostratudo():
    arquivo = open("cadastro.txt", "r")
    linhas = arquivo.readlines()
    print('\033[36m-' * 50)
    print('PESSOAS CADASTRADAS'.center(50))
    print('-' * 50, end='')
    print('\033[m')

    for line in linhas:
        print(line, end='')

    print('\n')
    print('\033[36m-' * 50)
    print('\033[m')


def cadastranovo():
    arquivo = open("cadastro.txt", "a")
    try:
        nome = str(input('Insira o nome: ')).strip().title()
    except Exception as erro:
        print(f'O erro \033[31m{erro.__class__}\033[m foi encontrado')

    try:
        idade = int(input('Insira a idade: '))
    except Exception as erro:
        print(f'O erro \033[31m{erro.__class__}\033[m foi encontrado')

    pessoa = f'\n {nome:<33}{idade:>10} anos'
    try:
        print(f'A pessoa, {nome}, de {idade} anos foi adicionada ')
        arquivo.write(pessoa)
    except Exception as erro:
        print(f'O erro \033[31m{erro.__class__}\033[m foi encontrado')


print('\033[36m-'*50)
print('MENU PRINCIPAL'.center(50))
print('-'*50)
print('\033[m')

print("""\033[33m1 - \033[mVer todas as pessoas cadastradas
\033[33m2 - \033[mCadastrar nova pessoa
\033[33m3 - \033[mSair\033[36m""")
print('-'*50)
print('\033[m')

while True:
    try:
        opc = int(input('Sua Opção: '))
    except Exception as erro:
        print(f'O erro \033[31m{erro.__class__}\033[m foi encontrado')
    else:
        if opc == 1:
            mostratudo()
        elif opc == 2:
            cadastranovo()
        elif opc == 3:
            print('\033[32mOBRIGADO!!!\033[m')
            break
        else:
            print(f'Valor inserido é \033[31mINVÁLIDO\033[m, escolha uma opção válida do menu')
