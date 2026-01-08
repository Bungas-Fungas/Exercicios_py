##desafios da aula 7

## 1: ler um numero intero e mostrar seu sucessor e antecessor
n = int(input('Digite um valor:'))
print(' O antecessor de {} é {} e o seu sucessor é {}'.format(n,(n-1),(n+1)))

## 2: ler um numero e mostrar seu dobro, triplo e raiz quadrada
n= int(input('Digite um valor:'))
print('O dobro de {} é {} o triplo é {} e sua raiz quadrada é {:.2f}'.format(n,(n*2),(n*3),(n**(1/2))))

## 3: ler duas notas e mostrar a media
n1 = float(input('primeira nota:'))
n2 = float(input('segunda nota: '))
m = (n1+n2)/2
print('A média é de {:.1f}'.format(m))

## 4: ler um valor em metros e exibir convertido em centimetro e milimetro
n1 = float(input('digite um valor em metros: '))
c= n1*100
mm = n1*1000
print('para centimetros resulta em {:.0f} e para milimetros em {:.0f}'.format(c,mm))

## 5: ler um numero inteiro e mostrar sua tabuada
n1 = int(input('digite um numero inteiro: '))
print('-'*12)
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
print('-'*12)

## 6: ler quanto dinheiro alguem tem e converter para dolar
d= float(input('Digite um valor em reais: '))
print('Você consegue comprar {:.2f} dólares'.format(n/5,38))
print('Você consegue comprar {:.2f} euros'.format(n/6,27))

## 7: ler a largura e a altura de uma parede,calcular a area e a quantidade de tinta necessaria para pinta-la, cada litro de tinta printa 2m²
l= float(input('largura: '))
a= float(input('altura: '))
area= l*a
qnt_tinta=area/2
print('para pintar essa parede com area de {:.2f}m² sera necessario {:.2f} litros de tinta'.format(area,qnt_tinta))

## 8: ler um preco e mostrar com 5% de descoto
p= float(input('Digite o preco: '))
print('Apos o desconto o produto custara {} reais'.format(p*0.95))

## 9: ler um salario e mostrar um novo com aumento de 15%
s= int(input('seu salario: '))
print('Apos o aumento seu salario de {} passara a ser {}'.format(s,s+s*0.15))

## 10: celsius para Fahrenheit
c = float(input('informe a temperatura em Cº: '))
f= ((9*c)/5)+32
print('A temperatura de {}Cº corresponde a {}Fº'.format(c,f))

## 11:  perguntar qnts km um carro alugado rodou e a quantidade de dias e calcular o preco a pagar sendo que o dia é 60R$ e o km rodado é 0.15R$

d= int(input('Informe a quantidade de dias que o carro foi alugado: '))
km= float(input('Informe a quantidade de Km rodados nesse tempo: '))
p_d= d*60
p_Km= km*0.15
t= p_d+p_Km
print('Por rodar por {} dias o valor a pagar será de {:.2f}R$'.format(d,p_d))
print('Por rodar por {:.2f}Km o valor a pagar será de {:.2f}R$'.format(km,p_Km))
print('Resultando no total a pagar de {:.2f}R$'.format(t))