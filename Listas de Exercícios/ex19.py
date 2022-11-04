from random import choice

a1 = input('Digite um nome\n')
a2 = input('Digite um nome\n')
a3 = input('Digite um nome\n')
a4 = input('Digite um nome\n')

lista = [a1, a2, a3, a4]

pika_dura_e_grossa_fdp = choice(lista)

print('O nome escolhido é {}'.format(pika_dura_e_grossa_fdp))
