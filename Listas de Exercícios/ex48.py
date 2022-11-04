# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 a 500

soma = 0
c = 0

print('os números ímpares que são múltiplos de três: ')
for f in range(1, 501):
    if f % 2 != 0:
        if f % 3 == 0:
            soma = soma + f
            c = c + 1
            print(f'{f}, ', end='')

print(f'\n\nA soma da {soma} e existem {c} números que se encaixam nessa pesquisa')
