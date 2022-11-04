frase = input('Escreva uma frase ou algumas palavras: \n')

fraseff = frase.strip()
frasin = fraseff.lower()
frase_c_A = frasin.count('a')
print(f'A letra "a" aparece {frase_c_A} vezes')

frase_acha_A = frasin.find('a' or 'A')
print(f'A primeira vez que a letra "a" foi encontrada foi na casa {frase_acha_A}')

frase_reverte = frasin[::-1]
frase_acha_A_revertido = frasin.find('a')
frase_soma = len(frase_reverte)

frase_fim = frase_soma - frase_acha_A_revertido

print(f'A última vez que a letra "a" foi encontrada foi na casa {frase_fim}')