#04. Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int (input('digite um numero:'))
n2 = int (input('digite um numero:'))

x = n1 + n2

#print('a soma vale', x)

print('A soma entre {} e {} é igual a{}'.format(n1, n2, x))