# Faça um programa que tenha uma função chamado escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável

def escreva(msg):
    tamanho = len(msg) + 2
    print('=' * tamanho)
    print(msg.center(tamanho))
    print('=' * tamanho)


mensagem = str(input('Insira uma mensagem para ser exibida: \n'))
escreva(mensagem)
