# ANSI escape sequence
# \033[m
# Este código pós contra barra é o codigo ANSI mais aceito pelo python
# \033[Style;Text;Backgroundm

# \033[0;33;44m
# Style --> 0 (None); 1 (Bold); 4 (Underline); 7 (Negativo/Inverte cor da letra com o background)
# Text --> 30 (White); 31 (Red); 32 (Green); 33 (Yellow); 34 (Blue); 35 (Magenta); 36 (Cyan); 37 (Grey)
# Background --> 40 (White); 41 (Red); 42 (Green); 43 (Yellow); 44 (Blue); 45 (Magenta); 46 (Cyan); 47 (Grey)

print('\033[1;30;41m Teste \033[m')
print('\033[1;33;44m Teste \033[m')
print('\033[1;30;43m Teste \033[m')
print('\033[1;37;42m Teste \033[m')
print('\033[m Teste \033[m')
print('\033[7;30m Teste \033[m')

