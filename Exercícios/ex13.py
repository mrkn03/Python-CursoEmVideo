#13. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('digite o preço do produto. R$'))

d = p - (p*(5/100))

print('o valor do produto com o desconto é R${}'.format(d))