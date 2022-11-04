# Melhore o jogo do exercício 28, onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador
# vai tentar adivinhar até acertar mostrando no final, quantos palpites foram necessários para vencer

from random import randint
# from time import sleep #
# Usado para deixar o usuário em espera por x segundos

n_random = randint(0, 10)
contador = 0

print("""A sua função é tentar adivinhar qual número de 0 a 10 foi sorteado pelo computador. Vamos lá!!!""")
tentativa = int(input('Tentativa: '))

while True:
    if tentativa == n_random:
        print('Parabéns!!! Você acertou!!!')
        contador = contador + 1
        break
    else:
        print('Você errou!!! Gostaria de tentar novamente? (Y or N) ')
        contador = contador + 1
        s_or_n = str(input('Y ou N: ')).strip().upper()
        if s_or_n == 'Y':
            tentativa = int(input('Mais uma tentativa: '))
        elif s_or_n == 'N':
            print('Você Desistiu!!!')
            break
        else:
            print('Valor inválido!!!')

print(f'Você adivinhou com {contador} tentativas')
