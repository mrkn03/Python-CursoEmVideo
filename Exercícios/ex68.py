'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo'''
while True:
    numero = int(input("DIGITE UM NUMERO INTEIRO QUALUQER: "))
    if numero < 0:
        break
    else:
        for i in range(1,11):
            print(numero,"X",i,"=",numero*i)