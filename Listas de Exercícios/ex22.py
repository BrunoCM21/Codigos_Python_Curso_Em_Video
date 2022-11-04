nome = input("Digite seu nome completo:\n").strip()
nome_separa = nome.split()

print(nome_separa)

nome_sem_espaco = nome.replace(' ', '')
First_name = nome_separa[0]

print(f'Letras Maiúsculas: {nome.upper()}')
print(f'Letras Minúsculas: {nome.lower()}')

print(f'Comprimento s/ espaço: {len(nome_sem_espaco)}')
print(f'Comprimento do 1o nome: {len(First_name)}')
