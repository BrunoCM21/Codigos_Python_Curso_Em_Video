# Desenvolva uma programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo

print("""Você deve me passar três comprimentos de retas para que o programa resolve dando
se é ou não possível de montar este triângulo que você que montar""")
c1 = float(input('Comprimento 1: '))
c2 = float(input('Comprimento 2: '))
c3 = float(input('Comprimento 3: '))

if c1 < (c2 + c3) and c2 < (c1 + c3) and c3 < (c2 + c1):
    print('É possível montar um triângulo com essas três retas')
else:
    print('É impossível montar um triângulo com essas três retas')
    if c1 > c2 and c1 > c3:
        print(f'Devido ao {c1} ser muito grande')
    else:
        if c2 > c3 and c2 > c1:
            print(f'Devido ao {c2} ser muito grande')
        else:
            print(f'Devido ao {c3} ser muito grande')
