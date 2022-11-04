# Adapte o código do ex107, criando uma função adicional chamada moeda() que consiga
# mostrar os valores como um valor monetário formatado


from ex108uteis import moeda

dindin = float(input('Digite o preço em R$: '))
print(f'A metade de {moeda.moeda(dindin)} é {moeda.moeda(moeda.metade(dindin))}')
print(f'O dobro de {moeda.moeda(dindin)} é {moeda.moeda(moeda.dobro(dindin))}')
print(f'Aumentando 5% de {moeda.moeda(dindin)}, temos o valor de {moeda.moeda(moeda.aumentar(dindin, 5))}')
print(f'Diminuindo 15% de {moeda.moeda(dindin)}, temos o valor de {moeda.moeda(moeda.diminuir(dindin, 15))}')