## Aula 09 do curso em video mundo 1

## Manipulando texto ou strings

## strings ocupam um espaco e dentro deste espaço cada caracter ocupa um micro espaço indo de 0 ate a quantidade de caracteres presentes

## fatiando strings

## frase inteira
frase = 'Curso em Vídeo Python' ## esse exemplo vai de 0 a 20 caracteres
print(frase)

## frase fatiada
print(frase[9])
print(frase[9:13])## vai do 9 ao 13 porem exclui o 13
## o primeiro sempre conta e o ultimo é excluido
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2]) ## esse 2 no final faz pular de 2 em 2
print(frase[:5])## quando omite o inicio ele vai do inicio ate o final dado
print(frase[15:])## quando omite o final ele vai do inicio dado ate o final
print(frase[9::3])## comeca no 9 e vai ate o final pulando de 3 em 3

## analise de strings

print(len(frase))## mostra o comprimento da frase
print(frase.count('o'))## conta quantas vezes aparece algo, nesse caso o 'o' minusculo
print(frase.count('o',0,13))## mostra a quantidade de 'o' dentro de um certo espaço, analise com fatiamento
print(frase.find('deo'))## mostra onde começa a parte da string escolhida 
print(frase.find('Android'))## quando a parte nao existe na string ele retorna -1
print('Curso' in frase)## ao inves de retornar a posicao na frase como o find o in retorna True ou False

## Trasnformação de strings

print(frase.replace('Python','Android'))## troca uma parte da string por outra
print(frase.upper())## deixa a frase em maiusculo
print(frase.lower())## deixa a frase em minusculo
print(frase.capitalize())## deixa so o primeiro caracter em maiusculo e o resto fica em minusculo
print(frase.title())## analisa quantas palavras tem a string e cada palavra comecara com maiusculo e o resto fica em minusculo
print(frase.strip())## remove todos os espaços inuteis no inicio e no final da string
print(frase.rstrip())## remove os espaços inuteis a direita
print(frase.lstrip())## remove os espacos inuteis a esquerda

## Divisão de strings

print(frase.split())## gera uma lista com as palavras de uma cadeia de caracteres 
print('-'.join(frase))## junta palavras separadas em listas e usa '-' como separador ex: Olá-Mundo!
##----------------------

print("""ichard McClintock, um professor de latim do Hampden-Sydney College na Virginia, pesquisou uma das mais obscuras palavras em latim, consectetur, oriunda de uma passagem de Lorem Ipsum, e, procurando por entre citações da palavra na literatura clássica, descobriu a sua indubitável origem. Lorem Ipsum vem das seções 1.10.32 e 1.10.33 do "de Finibus Bonorum et Malorum" (Os Extremos do Bem e do Mal), de Cícero, escrito em 45 AC. Este livro é um tratado de teoria da ética muito popular na época da Renascença. A prime""")## o uso de tres aspas duplas pode ser usada para imprimir textos grandes


## strings sao imutaveis a nao ser que se utilize uma funcao de transformacao junto a uma atribuicao
frase = frase.replace('Python','Android')
print(frase)

