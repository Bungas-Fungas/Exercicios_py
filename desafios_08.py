##Desafios da aula 08 do módulo 1

## 1:ler um numero real qualquer e mostrar apenas a parte inteira
import math
num= float(input('Escreva qualquer número inteiro: '))
print(math.trunc(num))

## 2: ler o comprimento do cateto oposto e do adjacente de um triangulo retangulo e calcular a hipotenusa

## 3: ler um angulo qualquer e mostrar o valor do seu seno cosseno e tangente

## 4: ler o nome de 4 pessoas e sortear um
import random
n1= str(input('Nome do primeiro aluno: '))
n2= str(input('Nome do segundo aluno: '))
n3= str(input('Nome do terceiro aluno'))
n4= str(input('Nome do quarto aluno: '))
s= random.randint(n1,n2,n3,n4)
print('O sorteado foi {}'.format(s))

## 5: ler o nome de 4 alunos e sortar uma ordem de apresentação

## 6: abrir e reproduzir um arquivo mp3