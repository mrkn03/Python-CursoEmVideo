#18. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

h = math.hypot(co, ca)

print('A hipotenusa entre os valores {} e {} é igual a {}'.format(co, ca, h))