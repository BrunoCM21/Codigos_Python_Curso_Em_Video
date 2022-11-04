# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato

preco_lista = []
maior = menor = total = contador = contagem_mais_de_mil = 0
maior_nome = menor_nome = 'piu'

while True:
    print('-'*26)
    nome_produto = str(input('Digite o nome do produto: ')).strip().upper()
    preco_produto = float(input('Digite o preço do produto: '))
    print('-' * 26)

    preco_lista.append(preco_produto)

    total = total + preco_produto

    if preco_produto >= 1000:
        contagem_mais_de_mil += 1

    if preco_lista[0] == preco_produto:
        maior = preco_produto
        maior_nome = nome_produto
        menor = preco_produto
        menor_nome = nome_produto
    elif preco_produto > maior:
        maior = preco_produto
        maior_nome = nome_produto
    elif preco_produto < menor:
        menor = preco_produto
        menor_nome = nome_produto

    mais = str(input('Deseja continuar (S ou N)? ')).strip().upper()

    while mais != 'N' and mais != 'S':
        mais = str(
            input('Valor inválido, insira o valor válido para caso deseja continuar (S ou N): ')).strip().upper()

    contador += 1

    if mais == 'N':
        break

print('\n')

if contagem_mais_de_mil >= 2:
    print(f'Possuem {contagem_mais_de_mil} produtos com valor maior que R$1000.00')
elif contagem_mais_de_mil == 1:
    print(f'Possui {contagem_mais_de_mil} produto com valor maior que R$1000.00')
else:
    print(f'Não possui nenhum produto com valor maior que R$1000.00')

print(f'O valor total deu R${total:.2f}')
print(f'O produto mais barato, com valor de R${menor:.2f}, é a/o {menor_nome}')

if contador >= 2:
    print(f'Possuem {contador} produtos cadastrados')
elif contador == 1:
    print(f'Possui {contador} produto cadastrado')
else:
    print('Não possui nenhum produto cadastrado')
