def teste(b):
    """--> Teste de variáveis globais e locais"""
    global a  # Pede para que utilize o mesmo a da variável global, ao invés de criar uma nova variável local
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')