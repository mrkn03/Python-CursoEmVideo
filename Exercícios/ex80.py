"""Crie um programa onde o usuario possa digitar cinco valores numericos e cadastr-os em uma lista, já na posição correta de inserção(sem usar o sort()).
no final, mostre a lista ordenada na tela"""
lista = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º valor: "))
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(f"Os valores digiados em ordem foram {lista}")