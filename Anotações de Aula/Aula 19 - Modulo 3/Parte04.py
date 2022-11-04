estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    for k, v in e.items():
        if k == 'uf':
            print(f'Unidade Federativa: {v}')
        else:
            print(f'Sigla: {v}')