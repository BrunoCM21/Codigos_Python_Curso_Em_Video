def somar(a=0, b=0, c=0):  # Ambos irão ser parâmetros opcionais
    """--> Faz a soma de três valores e mostra o resultado na tela
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    :return: Não possui retorno"""
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)  # Irá tem parâmetro opcional
somar(c=2, b=7)  
help(somar)