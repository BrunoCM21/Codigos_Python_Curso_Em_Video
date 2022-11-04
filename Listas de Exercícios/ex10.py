dindin = float(input("Quantos reais você tem na carteira?\nR$ "))

compra_dol = dindin // 5.45
doleta = dindin / 5.45
realusado = compra_dol * 5.45
realsobra = dindin - realusado

print(f"Você consegue comprar {compra_dol:.0f} notas de 1 dólar com R${dindin:.2f} e sobra R${realsobra:.2f}")
print(f"Mas se você transferir direto é possível conseguir U${doleta:.2f} com R${dindin:.2f}")
