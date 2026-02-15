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

## desafio 02: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
 
num = int(input('Digite um número: '))
print('''Escolha um tipo de conversão:
[1] binário
[2] octal
[3] hexadecimal''')
opcao = int(input('Sua opcção: '))
if(opcao == 1):
    print('{} em binário é {}'.format(num,bin(num)[2:]))
elif(opcao == 2):
    print('{} em octal é {}'.format(num,oct(num)[2:]))
elif(opcao == 3):
    print('{} em hexadecimal é {}'.format(num,hex(num)[2:]))
else:
    print("Opção inválida tente novamente.")


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
from datetime import date
data_nascimento = int(input('Digite o ano em que nasceu: '))
idade = date.today().year - data_nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(data_nascimento,idade,date.today().year))
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
idade = date.today().year - ano_nascimento
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


## Desafio 07: desafio 35 acrescentar o recurso de mostrar o tipo do triangulo q sera formado

reta1 = int(input('Digite o valor para uma reta: '))
reta2 = int(input('Digite mais um: '))
reta3 = int(input('Digite mais um: '))

if(reta1+reta2>reta3 or reta1+reta3>reta2 or reta2+reta3>reta1):
    print('Com essas três retas é possível formar um triângulo.')
    if(reta1 == reta2 or reta1==reta2 or reta2==reta3):
        print('O triangulo formado sera um triangulo isóceles')
    elif(reta1==reta2 and reta2==reta3):
        print('O triangulo formado sera um triangulo equilátero')
    else:
        print('O triangulo formado sera um triangulo escaleno')
else:
    print('Com essas três retas não é possível formar um triângulo.')


## Desafio 08: calcular o imc de alguem e mostrar o status da pessoa

altura = float(input('Digite sua altura em metros: '))
peso = float(input('digite seu peso em Kg: '))
imc = peso / (altura*altura)

if(imc<18.5):
    print('Você esta abaixo do peso seu imc é de {:.2f}'.format(imc))
elif(imc<=25):
    print('Você esta no peso ideal, seu imc é de {:.2f}'.format(imc))
elif(imc<=30):
    print('Você está sobrepeso, seu imc é de {}'.format(imc))
elif(imc<=40):
    print('Você está obeso, seu imc é de {}'.format(imc))
else:
    print('Você está com obesidade mórbida, seu imc é de {}'.format(imc))

    ## Desafio 10: calcule o valor a ser pago por um produto considerando seu preco normal e condicao de pagamento
    ## dinheiro a vista ou cheque 10% desconto
    ## a vista no cartao 5% de desconto
    ## em ate 2x no cartao preco normal
    ## 3x ou mais no cartao 20% de juros

print('{:=^40}'.format('Lojão do Tonhão'))
preco = float(input('Quanto você comprou?: '))
print('''Formas de pagamento:
[1] dinheiro à vista/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual sua opção?  '))
if(opcao == 1):
    total = preco - (preco*0.1)
elif(opcao == 2):
    total = preco - (preco*0.05)
elif(opcao == 3):
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif(opcao == 4):
    total = preco + (preco*0.2)
    totalparcelas = int(input('Quantas parcelas: '))
    parcela = total/totalparcelas
    print('Sua compra será parcelada em {:.2f}x de R${:.2f} com juros.'.format(totalparcelas,parcela))
else:
    total = 0
    print('\033[0;31mOpção de pagamento inválida!\033[m \033[0;33mtente novamente!\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco,total))


    ## desafio 11: fazer o computador jogar jokenpô com o usuario

from random import choice
jokenpo = [1,2,3]
escolha_pc = choice(jokenpo)
escolha_usuario = int(input("""Escolha o que irá jogar:
[1] Pedra
[2] Papel
[3] Tesoura\n"""))
if(escolha_pc == 1 and escolha_usuario == 3):
    print('O computador escolheu pedra, você perdeu.')
elif(escolha_pc == 2 and escolha_usuario == 1):
    print('O computador escolheu papel, você perdeu.')
elif(escolha_pc == 3 and escolha_usuario == 2):
    print('O computador escolheu Tesoura, você perdeu.')
elif(escolha_pc == 1 and escolha_usuario == 2):
    print('O computador escolheu pedra, você ganhou.')
elif(escolha_pc == 2 and escolha_usuario == 3):
    print('O computador escolheu papel, você ganhou.')
elif(escolha_pc == 3 and escolha_usuario == 1):
    print('O computador escolheu tesoura, você ganhou.')
else:
    print('O computador escolheu o mesmo que você, empatou.')