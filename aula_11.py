## aula 11 do mundo 1 python curso em video
## Cores no terminal

## codigo ansi escape sequence
## sempre começa com \ e o codigo que melhor funciona com python é o 33 logo todo codigo de cor começará com \033[m
## entre o [ e o m vao 3 codigos, o da fonte, cor do texto e cor do fundo ex: \033[0;33;44m  
## texto sempre começa com 3 e do fundo sempre com 4

##\033[0;30;41m

print('Olá\033[0;30;41m')
print('Olá\033[4;33;44m')
print('Olá\033[1;35;43m')
print('Olá\033[30;42m')
print('Olá\033[m')
print('Olá\033[7;30m')