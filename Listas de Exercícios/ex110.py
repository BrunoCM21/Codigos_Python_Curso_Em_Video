# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui

from ex110uteis import moeda

dindin = float(input('Digite o preço em R$: '))
moeda.resumo(dindin, 20, 10)