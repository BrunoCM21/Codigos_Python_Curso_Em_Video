# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o número 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares

a = int(input('Digite um número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
d = int(input('Digite o quarto número: '))

insere_tupla = (a, b, c, d)
contador_nove = 0
indicador_tres = -1

print('Os números pares inseridos foram: ', end='')

for posicao in range(0, len(insere_tupla)):
    if insere_tupla[posicao] == 9:
        contador_nove += 1
    if insere_tupla[posicao] == 3:
        indicador_tres = insere_tupla.index(3)

    if insere_tupla[posicao] % 2 == 0:
        print(f'{insere_tupla[posicao]} ', end='')
    else:
        print('', end='')

print('')

if indicador_tres == -1:
    print('Não houve nenhum 3 inserido')
else:
    print(f'O primeiro número "3" está na posição {indicador_tres}')

if contador_nove == 0:
    print('Não houve nenhum 9 inserido')
elif contador_nove == 1:
    print(f'Houve {contador_nove} vez o número 9 inserido')
else:
    print(f'Houve {contador_nove} vezes o números 9 inserido')