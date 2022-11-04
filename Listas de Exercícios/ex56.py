# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

soma_idade = 0
soma_idade_sexo_F = 0
soma_sexo_F = 0
soma_sexo_M = 0
idade_extra = 0
idede_dele = 0
ota_idade = []
cont = 0
nome_do_mais_velho = 'Vazio'

for r in range(1, 5):
    print(f' -------- {r}ª Pessoa --------')

    nome = str(input('Digite seu nome: ')).strip().title()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo(F ou M)? ')).strip().upper()

    soma_idade = soma_idade + idade
    ota_idade.append(idade)
    cont += 1

    if sexo == 'F' or sexo == 'M':
        if sexo == 'F':
            if idade <= 20:
                soma_idade_sexo_F = soma_idade_sexo_F + 1
            else:
                soma_sexo_F = soma_sexo_F + 1
        else:
            soma_sexo_M = soma_sexo_M + 1

            if ota_idade[0] == idade:
                nome_do_mais_velho = nome
                idede_dele = idade

            elif ota_idade[r-1] < idade:
                nome_do_mais_velho = nome
                idede_dele = idade
            else:
                nome_do_mais_velho = nome
                idede_dele = idade
    else:
        r = r - 1
        print('Sexo inválido!')


media = soma_idade / 4
print(f'A média de idade será {media}')

if nome_do_mais_velho == 'Vazio':
    print('Não existe homens nessa pesquisa')
else:
    print(f'O homem mais velho é o {nome_do_mais_velho} com {idede_dele} anos')

print(f'A quantidade de mulheres com menos de 20 anos é de {soma_idade_sexo_F}')

print(f'{soma_sexo_M}')