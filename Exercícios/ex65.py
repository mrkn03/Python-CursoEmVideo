'''65. Crie um programa que leia varios números inteiros pelo teclado. o programa só vai parar quando 
o usuario digitar o valor 999, que é a condição de parada. no final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsidere o flag)
'''
n = cont = soma = 0
n = int(input('Digite um número qualquer: [999 para parar] '))
while n != 999:
    soma += n
    cont = cont + 1
    n = int(input('Digite um número qualquer: [999 para parar] '))
print('Você digitou {} e a soma foi {}'.format(cont, soma))
