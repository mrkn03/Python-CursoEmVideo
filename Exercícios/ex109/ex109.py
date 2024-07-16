"""Modifique as funçoes que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o
valor retornado por elas vai ser ou nao formatado pela função moeda(), desenvolvida no desafio 108"""
import moedas

preco = float(input("Digite um valor:"))

print(f"A metade de {moedas.moeda(preco)} é {moedas.metade(preco)}")
print(f"O dobro de {moedas.moeda(preco, sit=True)} é {moedas.dobro(preco)}")
print(f"Aumentando 10%, temos {moedas.aumentar(preco, 10)}")