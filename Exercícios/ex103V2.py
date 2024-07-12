"""Faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou.

O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente"""
def ficha(nome=0, gols=0):

    if nome == "":
        nome = "<desconhecido>"
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    return f"O jogador {nome} fez {gols} gols no total"


n = str(input("Nome do jogador: "))
g = str(input("Gols realizados: "))

print(ficha(n, g))