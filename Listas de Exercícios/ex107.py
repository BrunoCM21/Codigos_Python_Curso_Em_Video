# Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções

from ex107uteis import moeda

dindin = float(input('Digite o preço em R$: '))
print(f'A metade de R${dindin:.2f} é R${moeda.metade(dindin):.2f}')
print(f'O dobro de R${dindin:.2f} é R${moeda.dobro(dindin):.2f}')
print(f'Aumentando 5% de R${dindin:.2f}, temos R${moeda.aumentar(dindin, 5):.2f}')
print(f'Diminuindo 15% de R${dindin:.2f}, temos R${moeda.diminuir(dindin, 15):.2f}')