"""Faça um programa que tenha uma função chamada maior(), que receba varios parametros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles
é o maior."""
def maior(* numeros):
    cont = maior = 0
    print("-"*30)
    print("\nAnalisando os valores passados...")

    for valor in numeros:
        print(f"{valor}", end=" ")
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} valores.")
    print(f"O maior valor foi {maior}")

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()