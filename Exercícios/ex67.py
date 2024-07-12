'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuario
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsidere o flag)'''
soma = 0
cont = 0
while True:
    numero = int(input("Digite um número inteiro qualquer [999 para para]: "))
    soma += numero
    cont += 1
    if numero == 999:
        break
print("A soma de todos os números digitados é igual a ", soma)
print("Quantidade de números digitados",cont)