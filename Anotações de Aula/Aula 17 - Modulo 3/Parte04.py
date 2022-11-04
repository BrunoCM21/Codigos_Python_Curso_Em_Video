a = [2, 3, 4, 8]
b = a[:]  # Cria uma cópia de a dentro de b
c = a  # Cria uma ligação, mas não cópia entree c e a

b[2] = 8
c[3] = 100

print(a)
print(b)
print(c)

