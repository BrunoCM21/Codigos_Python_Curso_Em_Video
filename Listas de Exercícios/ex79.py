# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. Continue perguntando ao usuário se ele quer continuar
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente

lista = []
Ja_add = False

while True:
    numero = int(input('Digite um número: '))
    for l in lista:
        if l == numero:
            Ja_add = True
        else:
            Ja_add = False
        while Ja_add:
            numero = int(input('Número já inserido!!! Digite outro número: '))
            for l in lista:
                if l == numero:
                    Ja_add = True
                else:
                    Ja_add = False
    lista.append(numero)

    continuar = str(input('Gostaria de continuar? S/N ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Resposta Inválida!!!\nGostaria de continuar? S/N ')).strip().upper()
    if continuar == 'N':
        print('OBRIGADO!')
        lista.sort()
        break

print(f'A lista numérica é: {lista}')