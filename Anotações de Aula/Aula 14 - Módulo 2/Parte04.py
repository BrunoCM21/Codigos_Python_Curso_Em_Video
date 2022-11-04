n = 1
somap = somai = cont = 0

while n != 0:
    n = int(input('Digite um value: '))
    cont = cont + 1
    if n != 0:
        if n % 2 == 0:
            somap = somap + 1
        else:
            somai = somai + 1

print(f'Você digitou {somap} números pares e {somai} números ímpares em {cont} números inseridos')
print('Acabou')