## Desafios Aula 1 mundo 2 curso em video python

## Desafio 01: programa para aprovar emprestimo bancario para a comprea de uma casa. perguntar o valor da casa o salario do comprador e quantos anos ele vai pagar
## Calcular o valor da prestacao mensal, se passar de 30% do salario entao o emprestimo deve ser negado

valor_casa = int(input('Digite o valor da casa: '))
salario = int(input('Digite seu salário: '))
tempo = int(input('Em quanto tempo deseja pagar(Mêses): '))

parcela_mes = valor_casa/tempo

if(parcela_mes>=(salario-(salario*0.7))):
    print('Seu salário não é o suficiente seu empréstimo será \033[0;31mnegado\033[m.')
else:
    print('Seu empréstimo será \033[0;32maprovado\033[m e custará {:.2f}R$ por mês'.format(parcela_mes))

## desafio 02: ver depois




## desafio 03: ler dois valores e dizer qual é maior e qual é o menor ou se os dois são iguais

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if(n1>n2):
    print(' O {} é maior que {}'.format(n1,n2))
elif(n1<n2):
    print('O {} é maior que {}'.format(n2,n1))
else:
    print('Os dois números tem o mesmo valor.')

## desafio 04: ler o ano em que alguem nasceu e dizer se a pessoa ainda vai se alistar ou esta na hora de se alistar ou ja passou do tempo de se alistar, e mostrar quanto tempo falta ou ja passou de se alistar

data_nascimento = int(input('Digite o ano em que nasceu: '))
idade = 2026 - data_nascimento
if(idade<18):
    tempo_falta= 18 - idade
    print('Você ainda vai se alistar, faltam {} ano(s) para você se alistar'.format(tempo_falta))
elif(idade == 18):
    print('Está na hora de você se alistar.')
else:
    tempo_passou = idade - 18
    print('Já passou da hora de você se alistar, você está a {} ano(s) sem se alistar'.format(tempo_passou))

## Desafio 05: ler duas notas e mostrar se o aluno foi reprovado, esta de recuperação ou foi aprovado

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if(media<5):
    print('Você foi \033[0;31mrepovado\033[m!')
elif(media<6.9):
    print('Você ficou de \033[0;33mrecuperação\033[m!')
else:
    print('Você foi \033[0;32maprovado\033[m!')

## desafio 06: a confederação de natação tem categorias de acordo com a idade, leia o ano de nascimento de alguem e diga sua categoria

ano_nascimento = int(input('Digite o ano em que nasceu: '))
idade = 2026 - ano_nascimento
if(idade<=9):
    print('Você está na categoria Mirim!')
elif(idade<=14):
    print('Você está na categoria Infantil!')
elif(idade<=19):
    print('Você está na categoria Junior!')
elif(idade<=20):
    print('Você está na categoria Sênior!')
else:
    print('Você está na categoria Master!')