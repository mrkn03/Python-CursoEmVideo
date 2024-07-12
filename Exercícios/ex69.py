'''Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador
perder, mostrando o total de vitórias consecutivos que ele conquistou no final do jogo'''
from random import randint
v = 0
while True:
    jogador = int(input("Escolha um número: "))
    computador = randint(0,10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Impar? [P/I]")).strip().upper()
    print("Voce jogou",jogador, "e o computador jogou", computador, "Total de ",total)
    if tipo == "P":
        if total % 2 ==0:
            print("Voce VENCEU")
            v += 1
        else:
            print("Voce PERDEU")
            break
    if tipo =="I":
        if total % 2 == 1:
            print("Voce VENCEU")
            v += 1
        else:
            print("Voce PERDEU")
            break
    print("Vamos jogar novamente")
print("Voce venceu",v,"vezes")