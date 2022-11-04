def contador(* num):  # O * significa que vai desempacotar o pacote passado na função
    for valor in num:
        print(f' {valor} ', end='')
    print('FIM!')


def contador2(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(3, 7, 1, 10, 7)
contador(1, 0)
print()
contador2(2, 1, 7)
contador2(3, 7, 1, 10, 7)
contador2(1, 0)