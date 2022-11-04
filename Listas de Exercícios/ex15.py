carro = input('Qual o nome do carro que você alugou?\n')
km = int(input('Quanto km foram percorridos com o carro alugado?\n'))
dias = int(input('Quantos dias o carro ficou com você?\n'))

preco = (dias * 60) + (0.15 * km)

print(f'O preço a pagar pelo carro {carro} é de R${preco:.2f} pelos motivos de ter andado {km}km por {dias} dias')