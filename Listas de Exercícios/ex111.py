# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from ex111uteis.utilidadesCeV import moeda, dado

dindin = float(input('Digite o preço em R$: '))
moeda.resumo(dindin, 27, 16)