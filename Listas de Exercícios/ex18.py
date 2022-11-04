import math

ang = float(input('Insira o valor do ângulo: '))

tan = math.tan(math.radians(ang))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))

print(f' Seno     --> {seno:.2f}')
print(f' Cosseno  --> {cos:.2f}')
print(f' Tangente --> {tan:.2f}')
