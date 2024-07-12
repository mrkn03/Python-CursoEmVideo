"""Crie um rograma onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. Caso o número já exista la dentro, ele não sera adicionado.
No final, serao exibidos todos os valores unicos digitados, em ordem crescente"""""
#DETERMINAR VETOR
vet_a = []

while True:
    num = int(input("Digite um valor: "))
    if num not in números:
        vet_a.append(num)
    else:
        print("Valor duplicado. Tente outro. ")
    escolha = str(input("Quer continuar? (S/N) "))
    if escolha in "Nn":
        break