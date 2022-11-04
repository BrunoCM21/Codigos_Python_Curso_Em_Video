nome = input("Digite seu nome:\n")
nomef = nome.title()

answer = nomef.find('Silva')

if answer != -1:
    print("Possui Silva no nome")
else:
    print("Não possui Silva no nome")