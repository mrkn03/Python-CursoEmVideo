"""Faça um programa que tenha uma função chamada area(), que receba as dimensoes de um terreno retangular (largura e comprimento) e mostre a area do terreno"""

def area_retangulo(b, h):
    area = b * h
    print("-"*30)
    print("          AREA DO TERRENO")
    print(f" -Base = {b}m \n -Altura = {h}m\n -Area = {area}m²")
    print("-"*30)


print("-"*30)
print("     CONTROLE DE TERRENO")
print("-"*30)
area_retangulo(float(input("Largura: ")), float(input("Comprimento: ")))