# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
# número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(da):
    ok = False
    valormsg = 0
    while True:
        try:
            v = int(input(da))
        except ValueError:
            print('\033[0;31mERRO!!! Digite um número inteiro que seja válido.\033[m')
        else:
            ok = True
        if ok:
            break

    return v


def leiafloat(da):
    ok = False
    valormsg = 0
    while True:
        try:
            v = float(input(da))
        except ValueError:
            print('\033[0;31mERRO!!! Digite um número real que seja válido.\033[m')
        else:
            ok = True
        if ok:
            break

    return v


n = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor real: ')
print(f'Você acabou de digitar o número inteiro {n} e o número real {n2}')