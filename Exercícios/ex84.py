"""Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. 
No final, mostre:

A) quantas pessoas forasm cadastradas.
B) uma listagem com as pessoas mais pesadas.
C) uma listagem com as pessoas mais leves."""

temporario = []
principal = []
quantidade = 0
maior = menor = 0
while True:
    temporario.append(str(input("Nome: ")))
    temporario.append(float(input("Peso: ")))
    
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]

    principal.append(temporario[:])
    temporario.clear()

    opcao = str(input("Deseja continuar? (S/N)")).upper()
    quantidade += 1
    
    if opcao in "N":
        break

print(f"Foram cadastradas {quantidade} pessoas.")
print(f"O maior peso foi de {maior}kg. Peso de ", end = "")
for p in principal:
    if p[1] == maior:
        print(f"[{p[0]}]", end = "")
print()
print(f"O menor peso foi de {menor}kg. Peso de ", end = "")
for p in principal:
    if p[1] == menor:
        print(f"[{p[0]}]", end = "")