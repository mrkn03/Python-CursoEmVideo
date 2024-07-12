"""Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia. No final, mostre uma listagem de preços, organizando
os dados em forma tabular"""
lista = ("Lápis", 1.75,
         "Borracha", 2,
         "Caderno", 15.9,
         "Estojo", 25,
         "Transferidos", 4.20,
         "Compasso", 9.99,
         "Mochila", 120.32,
         "Canetas", 22.30,
         "Livro", 34.90)
for i in range(len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<30}", end="")
    else:
        print(f"R${lista[i]:>7.2f}")