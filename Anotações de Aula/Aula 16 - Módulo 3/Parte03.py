a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a

print(c)  # Ele junta ambas as tuplas em uma só
print(d)  # Fica diferente do c

print(len(c))

print(f'O 2 aparece {c.count(2)} vezes')
print(f'O 9 aparece {c.count(9)} vezes')

print(f'Posição {c.index(4)}')  # Mostra a posição do número escolhido
print(f'Posição {c.index(5, 2)}')  # Procura o número indicado a partir da posição(que é o segundo número do index)


