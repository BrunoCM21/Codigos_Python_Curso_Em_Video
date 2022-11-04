n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('Sua media foi: {}'.format(media))

if media >= 6.0:
    print('Nota boa')
else:
    if media >= 9.5:
        print('Nota excelente, PARABÉNS!!!')
    else:
        print('Nota ruim, tem que melhorar!!')
