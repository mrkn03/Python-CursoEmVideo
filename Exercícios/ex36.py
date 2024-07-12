#36. Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.
a= float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Sim estes segmentos podem format um triangulo')

else:
    print('Os segmentos {}, {}, {} nao podem formar um triangulo'.format(a, b,))
