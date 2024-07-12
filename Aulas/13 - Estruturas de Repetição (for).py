#Laços de Repetição
for c in range (1,10):   #laço C no intervalo(1,10):
    print('passos')
print('pega')

for c in range(0,3):
    print('passo')
    print('pula')
print('passo')
print('pega')

#------------ EXEMPLOS ------------
#01.
for c in range(1,6):
    print('Oi')
print('FIM')

#02. 
for c in range(6, 0, -1):
    print(c)
print('FIM')

#03. 
for c in range(0, 7, 2):
    print (c)
print('FIM')

#04. 
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

#05.
i = input('INICIO: ')
f = input('FIM: ')
p = input('PASSO: ')
for c in range(i, f+1, p):
    print(c)
print('FIM')

#06.
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

#07.
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s =  s + n
print('O somatorio de todos os valores foi {}'.format(s))