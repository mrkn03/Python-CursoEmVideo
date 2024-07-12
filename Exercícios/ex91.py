"""Crie um programa onde quatro jogadores joguem um dado e tenham um resultados aleatórios. Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem,
sabendo que o vencedor tirou o maior numero no dado"""
from random import randint
from operator import itemgetter

jogos = {}

for i in range(4):
    jogos[f"Jogador {i+1}"] = randint(0,10)

ranking = {}

print(" "*10,"Valores soretados")
for k, v in jogos.items():
    print(f"{k} tirou o número {v} no dado")
print()
print(" "*10, "Ranking dos jogadores")
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"    '{i+1}º lugar: {v[0]} com {v[1]} pontos")