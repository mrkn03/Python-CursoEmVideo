"""Crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamado moeda e dado. Transfira todas as funçoes
utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando"""
from Exercícios.ex111.UtilidadesCeV import moeda, dado

preco = float(input("Digite um preço:"))

moeda.resumo(preco, 35, 22)