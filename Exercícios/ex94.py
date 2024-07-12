"""Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média"""
pessoas = []
dados = {}
soma = media = 0

while True:
    dados.clear()
    dados["Nome"] = str(input("Digite o nome: "))
    
    #Sexo
    while True:
        dados["Sexo"] = str(input("Digite o sexo: (M/F) - ")).upper()[0]
        if dados["Sexo"] in "MF":
            break
        print("Operação inválida. Digite apenas M ou F")
    
    #Idade
    dados["Idade"] = int(input(f"Digite a idade de {dados['Nome']}: "))
    soma += dados["Idade"]
    pessoas.append(dados.copy())
    
    #Desja continuar acrescentando dados
    while True:
        opcao = str(input("Deseja continuar? (S/N) - ")).upper()[0]
        if opcao in "SN":
            break
        print("Operação inválida. Digite apenas S ou N")
    if opcao == "N":
        break

print("-"*30)
print(f"Ao todo temos {len(pessoas)} cadastradas")

media = soma / len(pessoas)
print(f"A média de idade é de {media:5.2f} anos.")

print(f"As mulheres cadastradas foram ", end="")
for dados in pessoas:
    if dados["Sexo"] in "Ff":
        print(f"{dados['Nome']} ", end="")

print()
print("Pessoas que estao acima da média: ",end="")
for dados in pessoas:
    if dados["Idade"] >= media:
        print("   ", end="")
        for k, v in dados.items():
            print(f"{k} = {v}; ", end="")
        print()
print("-"*30)