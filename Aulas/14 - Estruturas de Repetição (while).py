#Usando for
'''for c in range(1,10): 
    print(c)
print('Fim')'''

#Usando while
'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIm')'''

#Usando for
'''for c in range(1,5):
    n = int(input('Digite um valor: '))
print('Fim')'''

#Usando while
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:   
        if n % 2 == 0 :
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} numeros pares e {} numeros impares'.format(par, impar))