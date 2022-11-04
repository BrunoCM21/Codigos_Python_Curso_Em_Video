# Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que agora com o laço for

numero = int(input('Digite um número para a tabuada: '))

print('-'*12)

for f in range(0, 11):
    tab = numero * f

    print(f'{numero} x {f:2} = {tab}')

print('-'*12)
