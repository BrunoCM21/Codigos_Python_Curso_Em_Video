cidade = input("Digite o nome de uma cidade: ")

cidade_splitado = cidade.split()
city = cidade_splitado[0].title()

answer = city.find('Santo')

if answer != -1:
    print("A cidade digitada começa com Santo")
else:
    print("A cidade digitada NÃO começa com Santo")
