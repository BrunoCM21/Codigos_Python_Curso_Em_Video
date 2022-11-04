import math
import random

numint = random.randint(1, 100)
numfloat = random.random()

num = numint + numfloat
numf = math.floor(num)

print(f'O número {num} tem como inteiro {numf}')
print(f'A soma dos números aleatórios {numint} com {numfloat}')
