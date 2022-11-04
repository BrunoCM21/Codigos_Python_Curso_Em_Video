# Escreva um programa que faça o computador "pensar" em um número de inteiro de 0 a 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo pc

from random import randint
# from time import sleep #
# Usado para deixar o usuário em espera por x segundos

n_random = randint(0, 5)

print("""A sua função é tentar adivinhar qual número de 0 a 5 foi sorteado pelo computador. Vamos lá!!!""")
tentativa = int(input('Tentativa: '))

while True:
    if tentativa == n_random:
        print('Parabéns!!! Você acertou!!!')
        break
    else:
        print('Você errou!!! Gostaria de tentar novamente? (Y or N) ')
        s_or_n = str(input('Y ou N: ')).strip()
        if s_or_n == 'Y':
            tentativa = int(input('Mais uma tentativa: '))
        else:
            print('Você Desistiu!!!')
            break

