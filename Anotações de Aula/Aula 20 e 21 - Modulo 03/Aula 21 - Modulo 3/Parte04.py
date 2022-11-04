def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')  # o X é uma variável local


# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
# Mesmo 'n' ter sido definido embaixo, ele irá aparecer na função teste --> Escopo Global
