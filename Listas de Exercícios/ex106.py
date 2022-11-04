# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: use cores
from time import sleep

print('----------'*4+' BEM-VINDO '+'----------'*4)
print("""Aqui você consegue toda a ajuda disponível dentro do seu próprio código Python""")
print('')
while True:

    print('O que você deseja pesquisar?\n\033[0;31mEscreva fim para encerrar aplicação\033[m\n')
    ajuda = str(input())
    if ajuda == 'Fim' or ajuda == 'fIm' or ajuda == 'fiM' or ajuda == 'FIM' or ajuda == 'FIm' or ajuda == 'FiM' or ajuda == 'fIM' or ajuda == 'fim':
        print('')
        print('\033[33mEncerrando\033[m')
        print('')
        sleep(2)
        print('\033[31mAcabou\033[m')
        break
    help(ajuda)
