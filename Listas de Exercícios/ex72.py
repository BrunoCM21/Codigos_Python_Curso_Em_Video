# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero a vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostra-lo por extenso.
numero = ('zero', 'um', 'dois', 'três', 'quarter', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    leitor = int(input('Digite um número entre 0 a 20: '))
    while leitor < 0 or leitor > 20:
        leitor = int(input('TENTE NOVAMENTE!!! Digite um número entre 0 a 20: '))

    print(f'O número {leitor} em extenso é: {numero[leitor]}')

    validacao = str(input('Gostaria de Continuar?(S/N)\n')).upper().strip()
    while validacao != 'S' and validacao != 'N':
        validacao = str(input('Insira um valor válido. Gostaria de Continuar?(S/N)\n')).upper().strip()
    if validacao == 'N':
        print('OBRIGADO!')
        break