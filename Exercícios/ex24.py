#24. Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados. 
    #ex: 1834
    #unidade:4, dezena:3, centena:8, milhar:1
numero = int(input('Escolha um numero entre 0 e 9999: '))

n0 = numero // 1 % 10
n1 = numero // 10 % 10
n2 = numero // 100 % 10
n3 = numero // 1000 % 10

print('Unidade:{}'.format(n0))
print('Dezena:{}'.format(n1))
print('Centena:{}'.format(n2))
print('Milhar:{}'.format(n3))