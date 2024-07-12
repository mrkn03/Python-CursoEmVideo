def area(largura, comprimento):
    area = largura * comprimento
    print("     AREA DO TERRENO")
    print("-"*30)
    print(f" -LARGURA: {largura}m\n -COMPRIMENTO: {comprimento}m\n -AREA: {area}m²")
    print("-"*30)


print("-"*30)
print("     CONTROLE DE TERRENO")
print("-"*30)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
print("-"*30)
area(l, c)