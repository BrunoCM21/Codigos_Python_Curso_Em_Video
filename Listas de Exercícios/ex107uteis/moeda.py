def metade(valor):
    """--> Recebe o preço/valor de uma moeda ou item e encontra a metade do valor
     :param valor: preço/valor de algo
     :return: retorna a conta para essa função, no caso, a metade do parâmetro passado"""
    return valor / 2


def dobro(valor):
    """--> Recebe o preço/valor de uma moeda ou item e encontra o dobro do valor
     :param valor: preço/valor de algo
     :return: retorna a conta para essa função, no caso, a metade do parâmetro passado"""
    return valor * 2


def aumentar(valor, porcentagem=0):
    """--> Recebe o preço/valor de uma moeda ou item e entrega o acréscimo de valor daquele produto
     :param valor: preço/valor de algo
     :param porcentagem: porcentagem que irá acrescentar ao valor final do produto
     :return: dependendo da porcentagem, se a porcentagem for 0 irá retornar o valor normal, caso porcentagem seja
     diferente de 0, retorna, após todas as contas, o valor final com acréscimo da porcentagem """
    if porcentagem == 0:
        return valor
    else:
        valor_porcentagem = porcentagem / 100
        valor_de_acrescimo = valor_porcentagem * valor
        valor_final = valor + valor_de_acrescimo
        return valor_final


def diminuir(valor, porcentagem=0):
    """--> Recebe o preço/valor de uma moeda ou item e entrega a redução de valor daquele produto
     :param valor: preço/valor de algo
     :param porcentagem: porcentagem que irá reduzir ao valor final do produto
     :return: dependendo da porcentagem, se a porcentagem for 0 irá retornar o valor normal, caso porcentagem seja
     diferente de 0, retorna, após todas as contas, o valor final com a redução da porcentagem """
    if porcentagem == 0:
        return valor
    else:
        valor_porcentagem = porcentagem / 100
        valor_de_reducao = valor_porcentagem * valor
        valor_final = valor - valor_de_reducao
        return valor_final
