import moedas

preco = float(input("Digite o preço: R$"))

print(f"A metade de R${preco} é R${moedas.metade(preco)}")
print(f"O dobro de R${preco} é R${moedas.dobro(preco)}")
print(f"Aumentando 10% temos {moedas.aumentar(preco, 10)}")