def leiadinheiro(msg):
    ok = False
    valormsg = 0
    while not ok:
        entrada = str(input(msg)).replace(',', '.').strip()

        if entrada.isalpha() or entrada == '':
            print('\033[0;31mERRO!!! Preço inválido.\033[m')
        else:
            ok = True
            valormsg = float(entrada)

    return valormsg


