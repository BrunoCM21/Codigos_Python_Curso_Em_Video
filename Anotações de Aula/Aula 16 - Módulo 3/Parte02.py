lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} da posição {cont}')

print('\n')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} da posição {pos}')

print('\n')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('\n')

lanche2 = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata-frita')

print(sorted(lanche2))  # Ordem alfabética, ou seja, ordenado
print(lanche2)

print('\nEita CARALHO, Comi pra PORRA!!!!')