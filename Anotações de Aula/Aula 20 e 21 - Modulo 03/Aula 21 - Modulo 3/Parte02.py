def contador(i, f, p):
    """--> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno"""
    # Isso criado é um docstring, para caso seja importado e o usuário pedir o help, irá aparecer isso.
    c = i
    while c <= f:
        print(f'  {c}', end='...')
        c += p
    print(' FIM!')


contador(2, 10, 2)

help(contador)
