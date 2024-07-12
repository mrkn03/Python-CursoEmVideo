"""Faça um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçoes"""
#DETERMINAR VETORES
vet_a = []

#INSERIR VALORES NO VETOR
for i in range(5):
    num = float(input(f"Digite o {i+1}º valor: "))
    vet_a.append(num)

#IMPRIMIR O MAIOR E MENOR VALOR
print(f"MAIOR VALOR = {max(vet_a)}")

print(f"MENOR VALOR = {min(vet_a)}")

#IMPRIMIR AS POSIÇOES DO MAIOR E MENOR VALOR
print(f"O MAIOR VALOR ESTA NA POSIÇÃO {vet_a.index(max(vet_a))}")

print(f"O MENOR VALOR ESTA NA POSIÇÃO {vet_a.index(min(vet_a))} ")