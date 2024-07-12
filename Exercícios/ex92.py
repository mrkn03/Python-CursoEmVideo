"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionario recebera
tambem o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar"""
from datetime import date
dados = {}
atual = date.today().year

dados["Nome"] = str(input("Digie seu nome: "))
dados["Ano de nascimento"] = int(input("Digite seu ano de nascimento: "))
dados["CTPS"] = int(input("Digite o nº da carteira de trabalho: (0 caso não tenha) "))
dados["Idade"] = atual - dados["Ano de nascimento"]

if dados["CTPS"] != 0:
    dados["Ano de contratação"] = int(input("Digite o ano em que foi contratado: "))
    dados["Salário"] = float(input("Digite seu salário: R$"))
    dados["Idade da aposentadoria"] = dados["Idade"] + (dados["Ano de contratação"] + 35 - atual) 

print("-"*50)

print(" "*5,"Dados cadastrados")
print(" -",f"Nome informado: {dados['Nome']}")
print(" -",f"Ano de nascimento: {dados['Ano de nascimento']}")
print(" -",f"{dados['Nome']} tem {dados['Idade']} anos")

if dados["CTPS"] == 0:
    print(" -",f"{dados['Nome']} não possuí carteira de trabalho.")
else:
    print(" -",f"Nº da carteira de trabalho: {dados['CTPS']}")
    print(" -",f"Ano de contratação: {dados['Ano de contratação']}")
    print(" -",f"Salário: R${dados['Salário']}")
    print(" -",f"{dados['Nome']} tem {dados['Idade']} anos e irá se apostar com {dados['Idade da aposentadoria']} anos. ")

print("_"*50)
