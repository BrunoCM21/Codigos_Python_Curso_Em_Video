# print(x)
# É uma exceção

# primt(8)
# É um erro de sintaxe

n = int(input('Número: '))
print(f'Você digitou o número {n}')
# Erro com atribuição surge, ValueError, erro de exceção também

n = int(input('Numerador: '))
n2 = int(input('Divisor: '))
div = n / n2
print(f'O resultado é {div}')
# Caso insira o 0 no divisor irá dar o "ZeroDivisionError", erro de exceção