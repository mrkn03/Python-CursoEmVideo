"""Crie um programa que leia varios números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista"""
vet_a = []
cont = 0

for i in range(5):
    num = float(input(f"Digite o {i+1}º valor: "))
    vet_a.append(num)
    cont = cont + 1

print(f"Foram digitados {cont} números na lista")
print(f"Valores decrescente do vetor: {vet_a.sort(reverse = True)}")

if 5 in vet_a:
    print("O número 5 esta presente no vetor.")
else:
    print("O número 5 não está presente no vetor")