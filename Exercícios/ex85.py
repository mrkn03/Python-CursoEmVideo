"""Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista única que mantenha separados os valores pares e impares.
No final, mostre os valores pares e ímpares em ordem crescente."""
num = [[], []]
valores = 0

for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else: 
        num[1].append(valor)
        
#Organizando valores em ordem crescente
num[0].sort()
num[1].sort()
print(f"Os valores ímpares são {num[1]}")
print(f"Os valores pares são {num[0]}")