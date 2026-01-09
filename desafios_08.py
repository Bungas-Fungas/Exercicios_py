##Desafios da aula 08 do módulo 1

## 1:ler um numero real qualquer e mostrar apenas a parte inteira
import math
num= float(input('Escreva qualquer número inteiro: '))
## as duas funcoes abaixo mostram apenas a parte inteira do numero mas uma é interna e a outra importada
print(math.trunc(num))
print(int(num))

## 2: ler o comprimento do cateto oposto e do adjacente de um triangulo retangulo e calcular a hipotenusa

co= float(input('Informe o comprimento do cateto oposto: '))
ca= float(input('Informe o comprimento do cateto adjacente: '))

## usando a formula
h= ((ca**2)+(co**2))**(1/2)
print('A hipotenusa medirá: {:.2f} '.format(h))

## usando a biblioteca math
h= math.hypot(co,ca)
print('A hipotenusa medirá: {:.2f} '.format(h))
## deixa o codigo mais simples 




## 3: ler um angulo qualquer e mostrar o valor do seu seno cosseno e tangente

a= int(input('Informe um ângulo qualquer: '))

sen=math.sin(math.radians(a))
cos= math.cos(math.radians(a))
tan= math.tan(math.radians(a))
print('O seno deste ângulo é {:.2f} o cosseno é {:.2f} e a tangente é {:.2f}'.format(sen,cos,tan))




## 4: ler o nome de 4 pessoas e sortear um
import random
n1= str(input('Nome do primeiro aluno: '))
n2= str(input('Nome do segundo aluno: '))
n3= str(input('Nome do terceiro aluno: '))
n4= str(input('Nome do quarto aluno: '))
s= random.randint(n1,n2,n3,n4)
print('O sorteado foi {}'.format(s))

## 5: ler o nome de 4 alunos e sortar uma ordem de apresentação

## 6: abrir e reproduzir um arquivo mp3