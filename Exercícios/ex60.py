'''60. Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''
[1]SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
          ''')
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma dos números {} e {} é igual a {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre os números {} e {} é igual a {}'.format(n1, n2, multiplicação))
    elif opção == 3:
        if n1 > n2:
            print('O primeiro termo {} é maior que o segundo termo {}'.format(n1, n2))
        if n2 > n1:
            print('O segundo termo {} é maior que o primeiro termo {}'.format(n2, n1))
    elif opção == 4:
        print('Informe os números novamente.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, digite novamente.')
    sleep(2)
print('Fim do programa! Volte sempre!')

