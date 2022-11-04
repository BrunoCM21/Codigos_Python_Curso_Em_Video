# Os exemplos são dados com os import sendo relacionados ao que entra no corpo humano, ou seja, bebida, comida e doce
# import bebida --> Mais generalista
# from bebida import pudim --> Mais especifista

# import math --> Importa operadores "extras"
# from math import sqrt --> Importa apenas um item do math

# função ceil --> Arredondamento p cima.        função floor --> Arredondamento p cima
# função trunc --> Corta a partir da vírgula
# função pow --> Potência, semelhante ao **
# função sqrt --> Raiz quadrada
# função factorial --> Fatorial matemático

import math

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

print(f'{raiz}')

