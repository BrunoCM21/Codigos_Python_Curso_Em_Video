n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2  # Potência
divint = n1 // n2  # Divide sem utilizar vírgula (não coloca o 0 e , no momento da divisão
resto = n1 % n2  # Resto da Divisão, parte que sobra da conta

print(f"Soma: {soma}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")
print(f"Potência: {pot}")
print(f"Divisão Inteira: {divint}")
print(f"Resto da Divisão: {resto}")

# Ordem de Precedência
# 1º ()
# 2º **
# 3º *   /   //   %
# 4º +   -
