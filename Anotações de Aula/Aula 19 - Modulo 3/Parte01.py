dados = {'nome': 'Pedro', 'idade': 25}  # Não se usa mais índices numéricos, e sim índices literais
print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M'

print(dados)

del dados['idade']

print(dados)

dados2 = dict()

dados2['titulo'] = 'Star Wars'
dados2['ano'] = '1977'
dados2['diretor'] = 'George Lucas'

print(dados2.values())
print(dados2.keys())
print(dados2.items())

for k,v in dados2.items():
    print(f'O {k} é {v}')