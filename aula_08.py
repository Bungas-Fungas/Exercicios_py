## Aula 08 do modulo 1 mundo python curso em video
## Utilizando módulos ou bibliotecas
import math

## tambem é possivel importar so uma ou mais funcoes ao inves de todas, utilizando:
from math import sqrt

## quando feito do jeito acima não é mais necessário utilizar o 'math.'

num= int(input('Digite um número: '))
## sqrt calcula a raiz quadrada
## raiz = math.sqrt(num)
raiz = sqrt(num)
## ceil arredonda para cima
## floor arredonda para baixo
print('A raiz quadrada de {} é igual a {}'.format(num,raiz))

import random
num = random.randint(1,10)
print(num)