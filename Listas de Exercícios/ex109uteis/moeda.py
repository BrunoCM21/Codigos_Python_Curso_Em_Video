def metade(valor=0, format=True):
    valor_final = valor / 2
    return valor_final if format is False else moeda(valor_final)


def dobro(valor=0, format=True):
    valor_final = valor * 2
    return valor_final if format is False else moeda(valor_final)


def aumentar(valor=0, porcentagem=0, format=True):
    if porcentagem == 0:
        return valor
    else:
        valor_porcentagem = porcentagem / 100
        valor_de_acrescimo = valor_porcentagem * valor
        valor_final = valor + valor_de_acrescimo
        return valor_final if format is False else moeda(valor_final)


def diminuir(valor=0, porcentagem=0, format=True):
    if porcentagem == 0:
        return valor
    else:
        valor_porcentagem = porcentagem / 100
        valor_de_reducao = valor_porcentagem * valor
        valor_final = valor - valor_de_reducao
        return valor_final if format is False else moeda(valor_final)


def moeda(preco=0.00, moedinha='R$'):
    return f'{moedinha}{preco:.2f}'.replace('.', ',')
