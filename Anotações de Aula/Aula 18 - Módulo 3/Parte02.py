teste = list()
teste.append('Bruno')
teste.append(19)
print(teste)

amigos = list()
amigos.append(teste[:])
teste[0] = 'Gustavo'
teste[1] = '18'
amigos.append(teste[:])

print(amigos)