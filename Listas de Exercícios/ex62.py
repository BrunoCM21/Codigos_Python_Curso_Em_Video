# Melhore o ex61, perguntando se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer
# mostrar 0 termos

x = 0
pedido = 10
total = 0

print('-'*31)
ptermo = int(input('Qual o Primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
print('-'*31)

while pedido != 0:

    total = total + pedido

    while x < total:

        pa1 = ptermo + x * razao
        x = x + 1
        print(f'{pa1} --> ', end='')

    print('PAUSA')
    pedido = int(input('Quantos termos você quer a mais? '))

print('`-´'*3, 'Acabou', '`-´'*3)



