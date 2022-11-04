num = []
num.append(4)
num.append(3)
num.append(0)
num.append(10)

for c, v in enumerate(num):
    if c == len(num)-1:
        print(f'{v}.')
    else:
        print(f'{v}...', end='')