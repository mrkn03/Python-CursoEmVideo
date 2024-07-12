#17. Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: 6.127 - o numero 6.127 tem sua parte inteira 6
import math
n = float(input('Digite um numero qualquer: '))
real = math.trunc(n)

print('Aposiçao inteira do numero {} é {:.0f}'.format(n,real))