"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. """
from random import randint

lista = []
jogos = []

print()
print("        JOGA NA MEGA SENA            ")
print()

quant = int(input("Quantos jogos deseja ser sorteados? "))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear
    tot += 1

for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")