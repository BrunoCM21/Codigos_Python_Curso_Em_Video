# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.
import random

def sorteia():
    lista = []
    for a in range(0, 5):
        n = random.randint(0, 10)
        lista.append(n)
    somaPar(lista)


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num

    print(soma)

sorteia()


