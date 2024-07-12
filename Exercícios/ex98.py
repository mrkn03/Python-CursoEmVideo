"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realiza a contagem. Seu programa tem que realizar três contagens atraves da função criada:

A) De 1 ate 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada"""
from time import sleep

def contador(inicio, fim, passo):
    print("-"*40)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    print("-"*40)
    sleep(1.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont} ", end = "", flush=True)
            sleep(0.5)
            cont += 1
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end = "", flush=True)
            sleep(0.5)
            cont -= passo
        print("FIM!")
        print("-"*40)

contador(int(input("Digite o inicio: ")), int(input("Digite o fim: ")), int(input("Digite o passo: ")))