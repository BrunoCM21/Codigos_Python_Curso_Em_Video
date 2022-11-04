num = int(input("Digite um número entre 0 a 9999\n"))

if num > 9999 or num < 0:
    print("Ah seu pilantra, faz esse negócio denovo!!!")
    num = int("Digite um número entre 0 a 9999\n")

num_str = str(num)

num_tracado = '-'.join(num_str)
num_separado = num_tracado.replace('-', ' ')

num_splitado = num_separado.split()

print(f'\nMilhar  --> {num_splitado[0]}')
print(f'Centena --> {num_splitado[1]}')
print(f'Dezena  --> {num_splitado[2]}')
print(f'Unidade --> {num_splitado[3]}')

# Modo matemático
num2 = int(input("\nDigite novamente o número entre 0 a 9999\n"))
uni = num2 // 1 % 10
dez = num2 // 10 % 10
cen = num2 // 100 % 10
mil = num2 // 1000 % 10

print(f'\nMilhar  --> {mil}')
print(f'Centena --> {cen}')
print(f'Dezena  --> {dez}')
print(f'Unidade --> {uni}')
