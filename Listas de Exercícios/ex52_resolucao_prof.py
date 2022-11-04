num = int(input('Digite um número para saber se é primo ou não: '))

Primo = False
total = 0

for r in range(1, num + 1):
    if num % r == 0:
        print('\033[33m')
        print('{}'.format(r), end=' ')
        total += 1
    else:
        print('\033[31m')
        print('{}'.format(r), end=' ')

print(f'\n\033[mO número {num} foi dividido {total} vezes')

if total == 2:
    print(f'E por isso ele é primo')
elif total != 2:
    print(f'E por isso ele não é primo')

