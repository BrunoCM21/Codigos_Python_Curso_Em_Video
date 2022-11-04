# Modifique as funções que foram criadas no ex107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no ex108

from ex109uteis import moeda

dindin = float(input('Digite o preço em R$: '))
print(f'A metade de {moeda.moeda(dindin)} é {moeda.metade(dindin)}')
print(f'O dobro de {moeda.moeda(dindin)} é {moeda.dobro(dindin, False)}')
print(f'Aumentando 5% de {moeda.moeda(dindin)}, temos o valor de {moeda.aumentar(dindin, 5, True)}')
print(f'Diminuindo 15% de {moeda.moeda(dindin)}, temos o valor de {moeda.diminuir(dindin, 15, True)}')