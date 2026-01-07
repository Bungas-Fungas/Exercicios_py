##desafios da aula 7

## 1: ler um numero intero e mostrar seu sucessor e antecessor
n = int(input('Digite um valor:'))
print(' O antecessor de {} é {} e o seu sucessor é {}'.format(n,n-1,n+1))

## 2: ler um numero e mostrar seu dobro, triplo e raiz quadrada
n= int(input('Digite um valor:'))
print('O dobro de {} é {} o triplo é {} e sua raiz quadrada é {}'.format(n,n*2,n*3,n**(1/2)))

## 3: ler duas notas e mostrar a media
n1 = int(input('primeira nota:'))
n2 = int(input('segunda nota: '))
m = (n1+n2)/2
print('A média é de {}'.format(m))

## 4: ler um valor em metros e exibir convertido em centimetro e milimetro
n1 = float(input('digite um valor em metros: '))
c= n1*100
mm = n1*1000
print('para centimetros resulta em {} e para milimetros em {}'.format(c,mm))

## 5: ler um numero inteiro e mostrar sua tabuada
n1 = int(input('digite um numero inteiro: '))
print('{} * 1 = {}'.format(n1,n1*1))
print('{} * 2 = {}'.format(n1,n1*2))
print('{} * 3 = {}'.format(n1,n1*3))
print('{} * 4 = {}'.format(n1,n1*4))
print('{} * 5 = {}'.format(n1,n1*5))
print('{} * 6 = {}'.format(n1,n1*6))
print('{} * 7 = {}'.format(n1,n1*7))
print('{} * 8 = {}'.format(n1,n1*8))
print('{} * 9 = {}'.format(n1,n1*9))
print('{} * 10 = {}'.format(n1,n1*10))

## 6: ler quanto dinheiro alguem tem e converter para dolar
d= int(input('Digite um valor em reais: '))
print('Você consegue comprar {} dólares'.format(n/3.27))

## 7: ler a largura e a altura de uma parede,calcular a area e a quantidade de tinta necessaria para pinta-la, cada litro de tinta printa 2m²
l= int(input('largura: '))
a= int(input('altura: '))
area= l*a
qnt_tinta=area/2
print('para pintar essa parede com area de {} sera necessario {} litros de tinta'.format(area,qnt_tinta))

## 8: ler um preco e mostrar com 5% de descoto
p= float(input('Digite o preco: '))
print('Apos o desconto o produto custara {} reais'.format(p*0.95))

## 9: ler um salario e mostrar um novo com aumento de 15%
s= int(input('seu salario: '))
print('Apos o aumento seu salario de {} passara a ser {}'.format(s,s+s*0.15))