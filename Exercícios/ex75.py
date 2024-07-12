"""Desenvolva um programa que leia quatros valores pelo teclado e guarde-os em uma tupla. No final, mostre
A) Quantas vezes apareceu o valor 9
B) Em que posicao foi digitado o primeiro valor 3
C) Quais foram os numeros pares"""

num = (int(input("Digite um numero: ")), int(input("Digite um numero: ")), int(input("Digite um numero: ")), int(input("Digite um numero: ")))
print()
#VALORES DIGITADOS NA TUPLA
print(f"Os valores digitados foram {num}")
print()
#QUANTAS VEZES APARECE O NÚMERO 9
if 9 in num:
    print(f"O número nove apareceu {num.count(9)} vezes")
else:
    print(f"O número 9 não foi digitado nenhuma vez")
print()
#EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3
if 3 in num:
    print(f"O número 3 foi digitado na posição {num.index(3)+1}")
else:
    print("O número 3 não foi digitado nenhuma vez")
print()
#QUAIS FORAM OS NÚMEROS PARES
for i in num:
    if i % 2 ==0:
        print(f"Os valores pares são {i}") 
    else:
        print("Não foram digitados nenhum valor par")