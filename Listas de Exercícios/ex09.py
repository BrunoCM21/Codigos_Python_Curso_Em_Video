numero = int(input('Digite um número para a tabuada: '))

x = 0
print('------------------')
while True:
    print(f'{numero} x {x:2} = {numero * x}')
    x = x + 1
    if x == 10:
        print(f'{numero} x {x} = {numero * x}')
        break

print('------------------')

# ISSO AQUI PROVAVELMENTE EU ADIANTEI O QUE FARIAMOS NO FUTURO
