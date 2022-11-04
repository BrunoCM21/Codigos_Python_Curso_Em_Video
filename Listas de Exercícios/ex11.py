altura = float(input("Qual a altura da sua parede?\n"))
largura = float(input("Qual a largura da sua parede?\n"))

area = altura * largura

litro = area / 2

print(f"Você vai precisar de {litro:.1f} litros de tinta para pintar uma área de {area}m²")
