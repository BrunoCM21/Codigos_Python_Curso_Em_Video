# laço c no intervalo(1, 10)
#   passo
# pega

# for c in range(1, 10):
#    passo
# pega
moeda = True

from time import sleep

for c in range(0, 3):
    print('passo')
    print('pula')

sleep(3)
print('passo')
print('pega\n\n')

for c in range(0,3):
    if moeda:
        print('Pega moeda')
    print('passo')
    print('pula')

sleep(3)
print('passo')
print('pega')

