# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expressao = str(input('Digite sua expressão: ')).strip()
conta_abre = conta_fecha = 0

for letra in expressao:
    if letra == '(':
        conta_abre += 1
    elif letra == ')':
        conta_fecha += 1

if conta_fecha == conta_abre:
    print(f'Sua expressão ({expressao}) está escrita de forma correta!!!')
elif conta_fecha != conta_abre:
    print(f'Sua expressão ({expressao}) está escrita de forma incorreta!!!')