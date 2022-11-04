# Crie um código em Python que teste se o site Pudim.cm está acessível pelo computador usado

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O Pudim.com.br \033[31mnão está acessível\033[m no momento')
else:
    print('Consegui abrir o \033[36mPudim.com.br\033[m com \033[32mSUCESSO\033[m!')