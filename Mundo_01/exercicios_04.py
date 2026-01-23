## Aula 7 curso em video python
## Operadores aritiméticos:
## + adição
## - subtração
## * multiplicação
## / divisão
## ** potência
## // divisão inteira
## % resto da divisão
## operadores binarios precisam de dois operandos
## == serve para verificar a igualdade
## Ordem de procedencia:
## 1:()
## 2:**
## 3:*,/,//,%
## 4:+,-
##-----------------------------------
nome= str(input('Qual é o seu nome?'))
## :20 escreve o nome em 20 espaços, tambem é possivel usar <>^ para alinhar o texto e sinais como = para aparecerem em volta
print('prazer em te conhecer {:=^20}!'.format(nome))
##----------------------------------------
n1 = int(input('Um valor:'))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
## .3f limita a 3 casas decimais ou pontos flutuantes
print(' a soma vale {}, o produto é {} e a divisao é {:.3f}'.format(s,m,d),end=' ')
## end=' ' nao quebra a linha entre os prints
## \ quebra a linha sem ter que adiconar multiplos prints
print('divisao inteira {} e potencia {}'.format(di,e))