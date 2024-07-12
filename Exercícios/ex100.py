"""Faça um programa que tenha uma lista chamada numeros e duas funçoes chamadas sorteia() e somaPar(). A primeira função vai sortear 5 numeros e vai coloca-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARESsorteados pela função anterior"""
from random import randint
from time import sleep

numeros = []

def sorteia():
    print("-"*40)
    for i in range(5):
        numeros.append(randint(0,10))
    print(f"Números sorteados: {numeros}")


def soma_par():
    soma = 0
    for n in range(5):
        if numeros[n] % 2 == 0:
            soma += numeros[n]
    print(f"Soma dos números pares: {soma}")
    print("-"*40)


sorteia()
soma_par()