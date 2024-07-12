"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanha adaptavel.
Ex:
escreva("Olá, Mundo!")

Saída:
---------------
  Olá, Mundo!
---------------"""
def escreva(txt):
    print("-"*(len(txt)+4))
    print(f"  {txt}")
    print("-"*(len(txt)+4))

escreva(str(input("Digite uma mensagem: ")))