"""Crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamado moeda e dado. Transfira todas as funçoes
utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando"""
import moedas

preco = float(input("Digite um preço:"))

print(f"A metade de {moedas.moeda(preco)} é {moedas.moeda(moedas.metade(preco))}")
print(f"O dobro de {moedas.moeda(preco)} é {moedas.moeda(moedas.dobro(preco))}")
print(f"Aumentando 10%, temos {moedas.moeda(moedas.aumentar(preco, 10))}")