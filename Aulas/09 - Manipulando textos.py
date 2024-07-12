#Fatiamento
frase = 'curso em video Python'
frase[9]
frase[9:]
frase[9::3]
frase[:9]

#Analise
len(frase) #comprimento da frase
frase.count('o', 0, 13) #conta a letra + fatiamento da frase
frase.find('deo') #em que momento encontrou 'deo'
frase.find('Android') #se retornado o valor -1 significa que nao foi encontrado
'curso' in frase #mostrara se existe a palavra dentro da frase

#Transformação
frase.replace('Python', 'Android') #substituira pela palavra seguinte
frase.upper() #Transformar em maisculo
frase.lower() #Transformar em minusculo
frase.capitalize() #transforma em minusculo e transforma a primeira letra em maiusculo
frase.title() #analisa quantas palavras tem a string e transforma o inicio de cada palavra em maiusculo
frase.strip() #remove todos os espaços inuteis no inicio e no final da string 
frase.rstrip() #remove apenas os espaços da direita
frase.lstrip() #remove apenas os espaços da esquerda

#Divisão
frase.split() #divide a string em uma lista de acordo com seus espaços

#Junção
'-'.join(frase) # junta todos os elementos de (frase) e usa o separador '-'

#----------------- EXEMPLOS -------------------
#01. 
frase = 'Curso em Video Python'