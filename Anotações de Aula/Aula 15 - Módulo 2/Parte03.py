n = contador = s = 0

while True:
    n = int(input('Digite um número: '))
    contador += 1
    if n == 999:
        break
    # s = s + n
    s += n
print(s)