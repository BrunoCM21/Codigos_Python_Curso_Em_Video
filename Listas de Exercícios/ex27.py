nome = str(input("Digite seu nome completo:\n")).strip()
nome_separa = nome.split()

print(f' Primeiro nome => {nome_separa[0]}')

reverte_nome = nome_separa[::-1]
print(f'  Último nome  => {reverte_nome[0]}')

