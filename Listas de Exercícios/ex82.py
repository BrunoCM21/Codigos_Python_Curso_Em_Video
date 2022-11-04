# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas

lista = []
lista_par = []
lista_impar = []

while True:
    nums = int(input('Digite um número: '))
    lista.append(nums)

    if nums % 2 == 0:
        lista_par.append(nums)
        print(f'{nums} é número par')
    else:
        lista_impar.append(nums)
        print(f'{nums} é número ímpar')

    sn = str(input('Gostaria de continuar? S/N ')).strip().lower()
    while sn not in 'sn':
        sn = str(input('Resposta INVÁLIDA!!! Gostaria de continuar? S/N ')).strip().lower()
    if sn == 'n':
        break

lista.sort()
lista_par.sort()
lista_impar.sort()

print(f'TODOS: {lista}\nPARES: {lista_par}\nÍMPARES: {lista_impar}')