try:  # operação
    n = int(input('Numerador: '))
    n2 = int(input('Divisor: '))
    div = n / n2

except (ValueError, TypeError):  # falha
    print('\033[31mErro!!!')
    print(f'Erro encontrado com os tipos de dados que foram digitados\033[m')

except ZeroDivisionError:  # falha
    print('\033[31mErro!!!')
    print(f'Não é possível dividir um número por zero\033[m')

except KeyboardInterrupt:
    print('\033[31mErro!!!')
    print(f'O usuário preferiu não informar os dados\033[m')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')

else:  # deu certo
    print(f'O resultado é {div}')
finally:  # finalmente, acontece independente se deu certo ou errado
    print(f'\033[34mObrigado! Volte sempre!\033[m')
