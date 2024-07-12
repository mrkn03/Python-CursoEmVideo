'''61. Faça um programa que leia um número e mostre o seu fatorial.
ex: 5! = 5x4x3x2x1 = 120
'''
'''from math import factorial
n1 = int(input('Informe o número que deseja saber seu fatorial: '))
f = factorial(n1) 
print('O fatorial de {} é {}.'.format(n1, f))'''

n = int(input('Digite o número que deseja saber seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n), end = '')
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))
