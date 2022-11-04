try:  # operação
    n = int(input('Numerador: '))
    n2 = int(input('Divisor: '))
    div = n / n2
except Exception as erro:  # falha
    print('\033[31mErro!!!')
    print(f'Erro encontrado foi {erro.__class__}\033[m')
else:  # deu certo
    print(f'O resultado é {div}')
finally: # finalmente, acontece independente se deu certo ou errado
    print(f'\033[34mObrigado! Volte sempre!\033[m')