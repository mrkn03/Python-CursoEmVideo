"""Modifique as funçoes que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o
valor retornado por elas vai ser ou nao formatado pela função moeda(), desenvolvida no desafio 108"""
import moedas

preco = float(input("Digite um preço:"))

print(f"A metade de {moedas.moeda(preco)} é {moedas.moeda(moedas.metade(preco, True))}")
print(f"O dobro de {moedas.moeda(preco)} é {moedas.moeda(moedas.dobro(preco, True))}")
print(f"Aumentando 10%, temos {moedas.moeda(moedas.aumentar(preco, 10, True))}")
print(f"Reduzindo 13%, temos {moedas.moeda(moedas.diminuir(preco, True))}")