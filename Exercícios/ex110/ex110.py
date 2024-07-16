"""Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
informações geradas pelas funções que já temos no módulo criado até aqui."""
import moedas
preco = float(input("Digite um preço:"))

print(f"A metade de {moedas.moeda(preco)} é {moedas.moeda(moedas.metade(preco))}")
print(f"O dobro de {moedas.moeda(preco)} é {moedas.moeda(moedas.dobro(preco))}")
print(f"Aumentando 10%, temos {moedas.moeda(moedas.aumentar(preco, 10))}")