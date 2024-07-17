"""Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um modulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar que
sejam monetarios"""
from Exercícios.ex112.UtilidadesCeV import moeda
from Exercícios.ex112.UtilidadesCeV import dado

preco = dado.LeiaDinheiro('Digite o preço: R$')

moeda.resumo(preco, 35, 22)