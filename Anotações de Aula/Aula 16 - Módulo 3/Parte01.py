# Existe três formas de fazer mais de um armazenamento na mesma variável, e são: Tuplas,
# Listas e Dicionários

# Tupla --> ()     Lista --> []     Dicionário --> {}

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')  # Pode colocar sem parênteses, mesmo não sendo o mais recomendado

print('='*20)
print(lanche[3])  # Mostra só o pudim
print(lanche[0:2])  # Mostra o hamburguer e o suco, sem incluir a pizza
print(lanche[::-1])  # Mostra a lista ao contrária
print(lanche[1:])  # Mostra o suco até o fim da lista
print(lanche[-1])  # Mostra o último da lista
print(lanche[-2])  # Mostra o penúltimo da lista
print('='*20)

print(f'Existe {len(lanche)} coisas dentro da lista')  # Comprimento da lista

print('='*20)
for comida in lanche:  # Passa por dentro da lista inteira
    print(comida)
print('='*20)
for contador in range(0, len(lanche)):  # Passa também por dentro da lista, mas pela forma do for já conhecido
    print(lanche[contador])
print('='*20)

# As tuplas são imutáveis, não é possível retirar itens da tupla enquanto o sistema estiver em funcionamento
# lanche[2] = Frango Frito # --> Exemplo para dar erro
