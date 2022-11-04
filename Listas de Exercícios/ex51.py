# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão

PA = []

print('-'*31)
ptermo = int(input('Qual o Primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
print('-'*31)

for x in range(0, 10):

    pa1 = ptermo + x * razao
    PA.append(pa1)

print('E os 10 primeiros termos pós o primeiro são o ', end='')
for t in range(0, 10):
    if t == 9:
        print(f'{PA[t]}', end='. ')
    elif t == 8:
        print(f'{PA[t]}', end=' e o ')
    else:
        print(f'{PA[t]}', end=', ')
