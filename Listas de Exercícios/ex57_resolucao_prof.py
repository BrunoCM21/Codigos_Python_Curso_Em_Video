card = 3

while card != '5':
    sexo = str(input('Digite seu sexo (M ou F) ')).strip().upper()
    while sexo not in 'MmFf':
        sexo = str(input('Dados Inválidos!!! Por favor digite seu sexo (M ou F): ')).strip().upper()
    print('Sexo {} cadastrado com sucesso!!!'.format(sexo))

    card = str(input('Se quiser sair, digite 5. Se não quiser, não digite nada\n')).strip().upper()
