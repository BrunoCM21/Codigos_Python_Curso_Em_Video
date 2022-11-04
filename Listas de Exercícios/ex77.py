# Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são suas vogais

palavras = ('Computador', 'Monitor', 'Celular', 'Mouse', 'Papel', 'Fio', 'Arroz')
contagem_consoante = contagem_a = contagem_e = contagem_i = contagem_o = contagem_u = 0


for palavrinha in palavras:
    palavrinha = palavrinha.lower()
    for contagem in range(0, len(palavrinha)):
        if palavrinha[contagem] == 'a':
            contagem_a += 1
        elif palavrinha[contagem] == 'e':
            contagem_e += 1
        elif palavrinha[contagem] == 'i':
            contagem_i += 1
        elif palavrinha[contagem] == 'o':
            contagem_o += 1
        elif palavrinha[contagem] == 'u':
            contagem_u += 1
        else:
            contagem_consoante += 1

    print(f'A palavra {palavrinha.upper()} possui {contagem_a} letras "A", {contagem_e} letras "E", {contagem_i} letras "I", '
          f'{contagem_o} letras "O", {contagem_u} letras "U" e {contagem_consoante} consoantes')
    print('\n')
    contagem_consoante = contagem_a = contagem_e = contagem_i = contagem_o = contagem_u = 0