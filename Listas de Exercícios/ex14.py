tempC = int(input('Qual a temperatuta em ºC?\n'))

transK = tempC + 273
transF = (9 * tempC) / 5 + 32

print(f'A temperatura de {tempC}ºC correponde a {transF:.0f}ºF e a {transK} K')
