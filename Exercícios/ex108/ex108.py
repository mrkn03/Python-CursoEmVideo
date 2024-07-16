"""Adapte o codigo do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um
valor monetario formatado"""
import moedas
preco = float(input("Digite um preço:"))

print(f"A metade de {moedas.moeda(preco)} é {moedas.moeda(moedas.metade(preco))}")
print(f"O dobro de {moedas.moeda(preco)} é {moedas.moeda(moedas.dobro(preco))}")
print(f"Aumentando 10%, temos {moedas.moeda(moedas.aumentar(preco, 10))}")