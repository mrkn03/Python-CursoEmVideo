#39. Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
    # o primeiro valor é maior
    # o segundo valor é maior
    # nao existe valor maior, os dois sao iguais
n1 = float(input('Digite um valor qualquer:'))
n2 = float(input('Digite um valor qualquer'))

if n1 == n2:
    print('Não existe valor maior, os dois sao iguais')

elif n1 > n2:
    print('O primeiro valor é maior')

elif n2 > n1:
    print('O segundo valor é maior')