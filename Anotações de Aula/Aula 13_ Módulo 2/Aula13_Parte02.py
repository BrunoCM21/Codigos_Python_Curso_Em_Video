for i in range(0, 100):
    print(i)

print(i+1)
print('Acabo')

print('\n')

for c in range(0, 10, 2):
    print(c)

print('\n')

for f in range(10, 0, -2):
    print(f)

r = int(input('Digite um número inteiro aleatório: '))
for p in range(0, r+1):
    print(p)
print('FIM')

inic = int(input('Digite um número para começar a contagem: '))
fim = int(input('Digite um número para terminar a contagem: '))
passo = int(input('Digite um número para ser o pulo da contagem: '))
for q in range(inic, fim+1, passo):
    print(q)
print('FIM')
