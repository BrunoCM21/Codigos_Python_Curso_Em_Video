dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0], dados[1])

pessoas = list()
pessoas.append(dados[:])  # Cópia de dados
print(pessoas)

pessoas_dois = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas_dois)

print(pessoas_dois[0][0])
print(pessoas_dois[0][1])
print(pessoas_dois[0])
print(pessoas_dois[1][1])
print(pessoas_dois[2][0])
print(pessoas_dois[1])

