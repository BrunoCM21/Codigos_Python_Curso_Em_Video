def dobravalores(valores_alterado):
    for a in range(0, len(valores_alterado)):
        valores_alterado[a] *= 2
    print(valores_alterado)


valores = [7, 2, 5, 0, 4]
dobravalores(valores[:])
print(valores)