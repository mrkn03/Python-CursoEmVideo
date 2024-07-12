'''Crie um programa que leia a idade e o sexo de varias pessoas. a cada pessoa cadastrada, o programa 
devera perguntar se o usuario quer ou nao continuar. no final mostre:
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos'''
homem = 0
mulher_menor18 = 0
maior_18 = 0
while True:
    idade = int(input("Informe a idade: "))
    sexo = str(input("Informe o sexo [M/F]: ")).upper()
    if (idade > 18):
        maior_18 += 1
    elif (sexo == "M"):
        homem += 1
    elif (sexo == "F" and idade < 20):
        mulher_menor18 += 1
    continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    if continuar == "N":
        break