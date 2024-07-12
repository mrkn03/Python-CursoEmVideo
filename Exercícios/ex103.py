"""Faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou.

O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente"""
def ficha(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} fez {gols} gols no campeonato.")
    

n = str(input("Nome do jogador: "))
g = str(input("Gols realizado: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == "":
    ficha(gols = g)
else:
    ficha(n, g)
