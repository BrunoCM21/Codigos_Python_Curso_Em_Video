frase = 'Curso em Video Python'
farsa = '   Aprenda Python  '

print(frase[9])  # Um caractere
print(frase[9:14])  # Todos os caracteres do 9 até o 13, não insere o 14
print(frase[9:21])  # Todos os caracteres do 9 até o 20, não insere o 21
print(frase[9:21:2])  # Pega caracteres do 9 ao 21 só que de 2 em 2
print(frase[:5])  # Pega até a "casinha" 5, não incluindo-a e depois para
print(frase[15:])  # Pega todos caracteres a partir do 15
print(frase[9::3])  # Começa do 9 até o final e de 3 em 3

print(f'Possui {len(frase)} caracteres')  # Comprimento da frase/Conta quantas "casinhas" tem

# Conta a quantidade de "tal coisa" dentro da frase, nesse caso, da "casinha 0 até a 13, sem inclui-la
ha = frase.count('o', 0, 13)
print(f'Possui {ha} a letra "o" minúsculo')

# Indica em que "casinha" inicia esse conjunto de caracteres
ba = frase.find('deo')
print(f'"deo" começa na casa {ba}')

# Não irá encontrar nada nessa frase, irá retornar o valor -1
fall = frase.find('z')
print(fall)

# Responde True or False em caso de existência ou inexistência
c = 'Curso' in frase
print(c)

# Substitui algo por outro
pia = frase.replace('Python', 'Android')
print(pia)

# Deixa tudo maiúsculo
uuy = frase.upper()
print(uuy)

# Deixa tudo minúsculo
pp = frase.lower()
print(pp)

# Joga todos os caracteres para minúsculo e deixa apenas a primeira letra em maiúscula
u = frase.capitalize()
print(u)

# Transforma todos os caracteres iniciais das palavras em maiúsculas
h = frase.title()
print(h)

# Remove espaços inúteis da caixa de texto, como por exemplo no começo e no fim
t = farsa.strip()
print(t)

# Remove espaços inúteis da direita
hu = farsa.rstrip()
print(hu)

# Remove espaços inúteis da esquerda
kkk = farsa.lstrip()
print(kkk)

# Pega onde tem espaço e em divide em novas casinhas colocada dentro de outra lista
ppp = frase.split()

# Curso (Primeira Divisão) em (Segunda Divisão) Video (Terceira Divisão) Python (Quarta Divisão)
print(ppp[0])
print(ppp[0][1])
print(ppp[3])
print(ppp[3][3])

# Junta tudo com - (Tracinho/Menos)
pipiz = '-'.join(frase)
print(pipiz)

piziao = '-'.join(ppp)
print(piziao)

# As três aspas duplas funcionam para textos grandes e com isso não seria necessário escrever diversos prints
print("""\nOlá!!! Boa tarde, meu nome é Bruno, tenho 18 anos, estarei cursando em breve ciencias da computação E 
gostaria de entrar em alguma empresa decente e boa para que consiga ter um salario bom e sustentar minimamente a 
minha família e agradecer a tudo o que fizeram a mim nestes 18 anos""")
