# enquanto verdadeiro:
# se bloco:
#   passo()
# se sem_bloco:
#   pula()
# se moeda:
#   pega()
# se trofeu:
#   pula()
#   interrompa
# pega()

bloco = 1
sem_bloco = 2
moeda = 3
troféu = 4

from random import randint

while True:

    x = randint(1, 4)

    if x == bloco:
        print('passo')
    elif x == sem_bloco:
        print('Pulo')
    elif x == moeda:
        print('Pega moeda')
    elif x == troféu:
        print('Pula p/ plataforma')
        print('Pega troféu')
        break
    else:
        print('ERRO')
