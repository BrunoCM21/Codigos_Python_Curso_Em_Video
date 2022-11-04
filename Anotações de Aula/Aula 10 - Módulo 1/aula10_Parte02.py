nome = str(input('Qual é o seu nome? \n')).strip()

if len(nome) > 7:
    print('Que nome grande da porra bicho!!!')
else:
    print('Ownt que nome curto e fofo!!!')

#______________________________________________________________________________________________________________________
if nome == 'Bruno':
    print('Que nome lindo que você tem!!!')
else:
    print('Nada fora do normal.\n ue nome bosta')
print('Bom dia {}!!'.format(nome))
