lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'sorvete de creme'
print(lanche)
# Listas, diferente de tuplas, são mutáveis, ou seja, é possível substituir seus valores

lanche.append('cookie')  # Adiciona um elemento no final da lista
print(lanche)
lanche.insert(0, 'hot dog')  # Adiciona um elemento na posição desejada
print(lanche)

del lanche[3]
# Deleta um elemento da posição que quiser

lanche.pop(3)
lanche.pop()
# Usado normalmente para eliminar o último elemento,
# mas pode ser passado por parâmetro qual o item que você deseja eliminar

if 'pizza' in lanche:
    lanche.remove('pizza')  # Indica o conteúdo que você quer eliminar e o python refaz os índices

print(lanche)