# Retornando variáveis --> Return
def somar(a=0, b=0, c=0):  # Ambos irão ser parâmetros opcionais
    """--> Faz a soma de três valores e mostra o resultado na tela
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    :return: Não possui retorno"""
    s = a + b + c

    return s


somatot = 0
resp = somar(3, 2, 5)
print(f'A soma vale {resp}')
somatot += resp

resp = somar(8, 4)  # Irá tem parâmetro opcional
print(f'A soma vale {resp}')
somatot += resp

resp = somar(c=2, b=7)
print(f'A soma vale {resp}')
somatot += resp

print(f'A soma total das respostas da {somatot}')

help(somar)