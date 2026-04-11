## Desafio 46: mostrar na tela uma contagem regressiva para o estrou de fogos de artificio. indo de 10 ate 0, com pausas de 1 segundo entre eles
n=10
from time import sleep
for temporizador in range(0,n+1):
    print(n)
    n -= 1
    sleep(1)
print("\033[0;35mTe Amo Bomboncito <3\033[m")
