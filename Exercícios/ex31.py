#31. Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.
numero = int(input('Digite um numero inteiro:'))

if numero % 2 == 0  :
    print('O número {} é par.'.format(numero))

else:
    print('O número {} é impar.'.format(numero))