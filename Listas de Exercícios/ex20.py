import random

a1 = input('Digite um nome\n')
a2 = input('Digite um nome\n')
a3 = input('Digite um nome\n')
a4 = input('Digite um nome\n')

lista = [a1, a2, a3, a4]

choice1 = random.choice(lista)
choice2 = random.choice(lista)
choice3 = random.choice(lista)
choice4 = random.choice(lista)

if choice2 == choice1 or choice2 == choice3 or choice2 == choice4:
    choice2 = random.choice(lista)
    if choice3 == choice1 and choice3 == choice2 and choice3 == choice4:
        choice3 = random.choice(lista)
        if choice4 == choice1 or choice4 == choice2 or choice4 == choice3:
            choice4 = random.choice(lista)

print(f'\n{choice1}\n{choice2}\n{choice3}\n{choice4}\n')

random.shuffle(lista)

print(f'{lista}')
