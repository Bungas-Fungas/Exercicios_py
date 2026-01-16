##Desafios aula 09 curso em video python mundo 1

## 1: ler o nome completo de uma pessoa e mostrar o nome em maiusco,minusculos,todas as letras sem os espacos e quantas letras tem o primeiro nome

nome = str(input("Qual seu nome?:"))
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(nome.split()[0], len(nome.split()[0]))



## 2: ler um numero e mostrar cada digito separado

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analise do numero {}: '.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

## 3: ler o nome de uma cidade e dizer se começa ou nao com o nome 'santo'

cidade = str(input('Em que cidade você nasceu: ')).strip()
cidade = cidade.lower()
print(cidade[:5] == 'santo')

## 4: ler o nome de alguem e dizer se a pessoa tem 'silva' no nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem silva: {}'.format('silva' in nome.lower()))

## 5: ler uma frase e mostrar quantas vezes aparece a letra 'a', em que posicao ela aparece na primeira vez e qual posicao ela aparece pela ultima vez

## 6: ler um nome e mostrar o primeiro e o ultimo nome
