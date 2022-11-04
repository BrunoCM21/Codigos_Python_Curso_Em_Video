import math

c_oposto = float(input('Digite o valor do cateto oposto: '))
c_adjacente = float(input('Digite o valor do cateto adjacente: '))

soma_dos_catetos = (c_adjacente * c_adjacente) + (c_oposto * c_oposto)
hipotenusa = math.sqrt(soma_dos_catetos)

# Esse agora é um teste
hipotenusa2 = math.hypot(c_adjacente, c_oposto)

print('O valor da hipotenusa é especificamente {} e arredondando vale {}'.format(hipotenusa, math.floor(hipotenusa)))

# O de baixo é o print do teste com o math
print('Específico {}'.format(hipotenusa2))
