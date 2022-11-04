import emoji

nome =str(input('Qual é o seu nome? \n')).strip()

if nome == 'Bruno':
    print('Nome Lindo')
elif nome == 'Divania':
    print('Nome quase bonitinho KKKKKKk')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print ('Nomes comuns no Brasil')
else:
    print(emoji.emojize('Seu nome é bem normal :sob: :-1:', use_aliases=True))
print('Tenha um bom dia!!!')