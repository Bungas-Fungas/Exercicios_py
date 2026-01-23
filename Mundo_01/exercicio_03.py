##Aula 6 Curso em Vídeo

## aspas simples e duplas funcionam para strings, mas de preferencia usar as simples
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
soma = n1+n2
print('A soma vale',soma)
print('A soma vale {}'.format(soma))
##usar True e False com inicias capitalizadas
##type() mostra o tipo primitivo de uma variavel
print('A soma entre {0} e {1} vale {2}'.format(n1,n2,soma))
##isnumeric() mostra se é possivel converter o valor para numero
##isalpha() mostra se é letra
##isalphanum() mostra se é alfanumerico
##-------------------------------------------------------------------------
##Desafios da aula

##somar dois números
n1= int(input('Digite o primeiro numero:'))
n2= int(input('Digite o segundo numero:'))
soma = n1+n2
print('A soma de {} e {} é {}'.format(n1,n2,soma))

##-----------------------------------------------------------------
##mostrar o tipo e informações sobre a variavel
a= input('Digite algo:')
print('O tipo primitivo é:',type(a))
print('so tem espaços?',a.isspace())
print('é um número?',a.isnumeric())
print('é alfabetico?'), a.isalpha()
print('é alfanumerico?'), a.isalnum()
print('está em maiúsculas?'), a.isupper()
print('está em minusculas?'), a.islower()
print('está capitalizada?)',a.istitle())

