# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
# so que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')
def leiaint(da):
    ok = False
    valormsg = 0
    while True:
        v = str(input(da))
        if v.isnumeric():
            valormsg = int(v)
            ok = True
        else:
            print('\033[0;31mERRO!!! Digite um número inteiro que seja válido.\033[m')
        if ok:
            break

    return valormsg


n = leiaint('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')