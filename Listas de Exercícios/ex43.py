# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
# a tabela:  Abaixo de 18.5: Abaixo do Peso ----- Entre 18.5 e 25: Peso Ideal ----- 25 até 30: Sobrepeso -----
# 30 até 40: Obesidade ----- Acima de 40: Obesidade Mórbida

# IMC = peso/altura*altura
import emoji

peso = float(input('Insira o seu peso: '))
altura = float(input('Insira sua altura: '))

imc = peso / altura**2

print(f'Seu IMC é {imc:.2f}')

if imc < 0:
    print('Erro de lógica')
elif imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print(emoji.emojize('Peso Ideal :thumbsup:', use_aliases=True))
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print ('Obesidade')
elif imc >= 40:
    print(emoji.emojize('Obesidade Mórbida :dizzy_face:', use_aliases=True))
