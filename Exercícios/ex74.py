"""Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o
maior valor que estao na tupla"""
from random import randint
numero = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f"Eu sorteei os valores {numero}")
print(f"O maior valor sorteado foi {max(numero)}")
print(f"O menor valor sorteado foi {min(numero)}")
