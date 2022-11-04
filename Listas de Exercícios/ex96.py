# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimentro) e mostre a área do terreno

def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área do terreno é {area_terreno} m²')


l = float(input('Insira a largura do terreno (em metros): '))
c = float(input('Insira a comprimento do terreno (em metros): '))
area(l, c)
