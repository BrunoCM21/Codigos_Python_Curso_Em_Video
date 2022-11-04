# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular e o outro chamado show, que será um valor lógico(opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(num, show=False):
    valor = 1
    for t in range(1, num + 1):
        valor = valor * t
    if show:
        for y in range(1, num + 1):
            if y == num:
                print(f'{y} = ', end='')
            else:
                print(f'{y} X ', end='')
        print(f'{valor}')
    else:
        print(f'{valor}')


fatorial(3, show=True)
fatorial(7)
fatorial(10, show=True)