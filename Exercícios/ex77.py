"""Crie um programa que tenha uma tupla com varias palavras (não usar acentos). Depos disso, voce deve mostrar, para cada palavra, quais sao as suas vogais"""

palavras = ("pizza","jujuba","lapis","caneta","bolo","planta")

for i in palavras:
    print(f"\nNa palavra {i.upper()} temos as vogais:", end=" ")
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra, end=" ")