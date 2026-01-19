## Desafios aula 10 curso em video python mundo 1

## desafio 01: faça o programa escolher um nmero intreiro de 0 a 5 e peça ao usuario para tentar descobrir o nuumero escolhido pelo computador, diga se ele acertou ou não

import random
num_computador = random.randint(0,5)
num_usuario = int(input('Tente adivinhar o numero que o computador escolheu (0 a 5): '))
if(num_computador == num_usuario):
    print('Você acertou parabéns!!')
else:
    print('Você errou, tente novamente')


## desafio 02: ler a velocidade de um carro, se o carro estiver acima de 80km/h ele é multado em 7R$ por cada km acima

vel_carro = int(input('Qual a velocidade de seu carro: '))
multa = (vel_carro-80)*7
if(vel_carro > 80):
    print('Você foi multado em {:.2f}R$!'.format(multa))
else:
    print('Você esta livre para ir')

## desafio 03: ler um número e dizer se ele é par ou impar
num = int(input('Digite um número: '))
if(num %2==0):
    print('O número {} é um numero par'.format(num))
else:
    print('O número {} é um número ímpar'.format(num))

## desafio 04: peça a distancia de uma viagem, se for ate 200km cobrar 0.5 por km se for mais combrar 0.45 por km
distancia = int(input('Digite a distância de sua viagem: '))
if(distancia <= 200):
    preco = distancia*0.5
    print('A sua viagem custará {:.2f}R$'.format(preco))
else:
    preco = distancia*0.45
    print('A sua viagem custará {:.2f}R$'.format(preco))

## desafio 05: ler um ano e dizer se ele é bissexto
ano = int(input('Digite um ano qualquer: '))
if(ano %4==0 and ano%100==0 or ano%400==0):
    print('Esse ano é bissexto.')
else:
    print('Esse ano não é bissexto')

## desafio 05: ler tres numero e mostrar o maior e maior
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite mais um: '))
num3 = float(input('Digite mais um: '))
menor = num1
maior = num3
if(num2<num1 and num2<num1):
    menor = num2
if(num3<num1 and num3<num2):
    menor = num3
if(num1>num3 and num1>num2):
    maior = num1
if(num2>num3 and num2>num1):
    maior = num2
print('O maior valor digitado foi: {:.2f}'.format(maior))
print('O menor número digitado foi: {:.2f}'.format(menor))


## desafio 06: ler salario e dar aumetno de 10% se for mais de 1250R$ e 15% se for menos

salario = int(input('Digite seu salario: '))
if(salario>1250):
    novo_salario = salario+(salario*0.1)
    aumento = 10
else:
    novo_salario = salario+(salario*0.15)
    aumento = 15
print('Você receberá um aumento de {}%, seu novo salario será {:.2f}'.format(aumento,novo_salario))

## desafio 07: ler tres retas e dizer se elas podem ou nao formar um triangulo
reta1 = int(input('Digite o valor para uma reta: '))
reta2 = int(input('Digite mais um: '))
reta3 = int(input('Digite mais um: '))

if(reta1+reta2>reta3 or reta1+reta3>reta2 or reta2+reta3>reta1):
    print('Com essas três retas é possível formar um triângulo.')
else:
    print('Com essas três retas não é possível formar um triângulo.')

## desafio 08: