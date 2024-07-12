#34. Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
n3 = int(input('Digite um numero:'))
#Menor valor
if n1<n2 and n1<n3:
    print('O menor número é o {}'.format(n1))
if n2<n1 and n2<n3:
    print('O menor número é o {}'.format(n2))
if n3<n1 and n3<n2:
    print('O menor número é o {}'.format(n3))
#Maior valor
if n1>n2 and n1>n3:
    print('O maior valor é o {}'.format(n1))
if n2>n1 and n2>n3:
    print('O maior valor é o {}'.format(n2))
if n3>n1 and n3>n2:
    print('O maior valor é o {}'.format(n3))