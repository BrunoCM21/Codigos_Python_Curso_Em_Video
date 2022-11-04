# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0.50 por Km para viagens de até 200 KM e R$0,45 para viagens mais longas

cidade = str(input('Qual cidade você deseja ir?\n')).strip()
km = int(input(f'Quantos quilometros dão da sua cidade até {cidade}: \n'))

if km <= 200:
    valor = 0.5 * km
    print(f'O valor da passagem será de R${valor:.2f}')
else:
    valor2 = 0.45 * km
    print(f'O valor da passagem será de R${valor2:.2f}')
