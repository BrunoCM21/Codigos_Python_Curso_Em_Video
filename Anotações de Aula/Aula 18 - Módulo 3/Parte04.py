galera = list()
dado = list()  # Usado como lista temporária/secundária

for c in range(0, 3):
    dado.append(str(input('NOME: ')).strip())
    dado.append(int(input('IDADE: ')))

    galera.append(dado[:])
    # Cópia dos dados da lista 'dado', não link de dados (pois nesse caso, oq faz em uma lista acontece com a outra)
    dado.clear()  # Exclui os dados da lista

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')

print(galera)