"""Aprimore o desafio anterios, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0 , 0, 0]]
soma_par = maior = soma_coluna = 0

#Lendo matriz
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Elemento [{i}, {j}] "))

print()

print(" "*1,"MATRIZ 3X3 GERADA")
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end = "")
        if matriz [i][j] % 2 == 0:
            soma_par += matriz[i][j]
    print()

#Soma da terceira coluna
for l in range(3):
    soma_coluna += matriz[l][2]

#Maio valor da segunda linha
for c in range(3):
    maior = matriz[1][c]

print()
print(f"A soma dos valores pares é {soma_par}")
print(f"A soma da terceira coluna é {soma_coluna}")
print(f"O maior valor da segunda linha é {maior}")