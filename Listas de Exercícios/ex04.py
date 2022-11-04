merda = input('Insira qualquer merda ai: ')

print("O tipo de string é: {}".format(type(merda)))

if merda.isalpha():
    print("{} possui apenas letras".format(merda))

else:
    if merda.isnumeric():
        print("{} possui apenas números".format(merda))
    else:
        if merda.isalnum():
            print(f"{merda} possui letras e números")
        else:
            print("SEU FILHA DA PUTA, VOCÊ ME DEIXOU SEM RESPOSTAS.")

# print(f"{merda} possui letras e números")
# print("{} possui apenas números".format(merda))
# Os dois modos podem ser utilizados, o *f* na frente substitui .format a partir do Python 3.7 (o meu atual é o 3.9)
