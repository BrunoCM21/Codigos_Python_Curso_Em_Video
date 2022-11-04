amigos = [['Bruno', 19], ['Eduardo', 19], ['Gustavo', 18], ['Thael', 20]]

print(amigos[3])
print(amigos[2][0])
print(amigos[0][1])

print('='*20)

for pessoa in amigos:
    print(pessoa)

print('='*20)

for pessoa in amigos:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

print('='*20)
