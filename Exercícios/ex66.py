'''66. Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se 
ele quer ou não continuar a digitar valores.'''
n = cont = soma = 0

parar = 0
while parar != 'N':
    soma += n
    cont = cont + 1
    média = soma / cont
    n = int(input('Digite um número qualquer: '))
    parar = str(input('Deseja Continuar? [S/N]')).upper()
print('Você digitou {} números média foi {}'.format(cont, média))
