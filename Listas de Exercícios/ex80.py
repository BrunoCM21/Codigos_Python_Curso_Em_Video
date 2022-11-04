# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# ja na posição correta de inserção(sem usar o sort())
# No final, mostre a lista ordenada na tela
cont = 0
lista = []

# Nesta atividade metade dela foi resolvida com a resolução do professor,
# pois não consegui fazer isso funcionar do jeito que deveria ser

while cont < 5:
    num = int(input('Digite um número: '))
    if cont == 0 or num > lista[len(lista)-1]:
        lista.append(num)
        print('Colocado na lista')
    else:
        pos = 0
        while pos < len(lista):
            # Isso aqui pode ser utilizado para achar os itens dentro da lista, passando por todos os pontos da lista
            if num <= lista[pos]:
                lista.insert(pos, num)
                print('Adicionado na posição {} da lista'.format(pos))
                break
            pos += 1

    cont += 1

print(f'A lista é {lista}')