produto = str(input("Insira qual é o produto: "))
preco = float(input("Insira qual é o preço do produto: "))

pfinal = preco - (preco*0.05)

print(f"{produto} possuia preço de {preco:.2f} reais e agora com desconto fica {pfinal:.2f} reais")