#TUPLAS

lanche = ("hambuerguer", "suco", "pizza", "pudim", "Batata Frita")
#TUPLAS SAO IMUTAVEIS

print(lanche[1])    #MOSTRA O ELEMENTO 1
print(lanche[-2])   #MOSTRA O PENULTIMO ELEMENTO
print(lanche[1:3])  #MOSTRA DO ELEMENTO 1 ATÉ O ELEMENTO 3, EXCLUINDO O ELEMENTO 3
print(lanche[2:])   #MOSTRA DO ELEMENTO 2 ATÉ O FINAL
print(lanche[:2])   #MOSTRA DO INICIO ATÉ O ELEMENTO 2, EXCLUINDO O ELEMENTO 2
print(lanche[-2:])  #MOSTRA DO PENULTIMO ATÉ O FINAL
print(lanche[-3:])  #MOSTRA DO ANTIPENULTIMO ELEMENTO ATÉ O FINAL
print(lanche)       #MOSTRA A TUPLA INTEIRA

#UTILIZANDO FOR
for comida in lanche:
    print("Eu vou comer",comida)
print("Comi pra caramba!")

for cont in range(0, len(lanche)):
    print("Eu vou comer",lanche[cont], " na posição", cont)

for pos, comida in enumerate(lanche):
    print("Eu vou comer", comida, "na posicao", pos)

# MANIPULAR A TUPLA ORGANIZADA
print(sorted(lanche))   #TUPLA ORGANIZADA
print(lanche)           #TUPLA ORIGINAL

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b               #JUNTA AS TUPLAS (a, b)

print(len(c))           #MOSTRA A QUANTIDADE DE ELEMENTOS NA TUPLA
print(c.count(5))       #MOSTRA QUANTAS VEZES APARECE O NUMERO "5" NA TUPLA
print(c.index(8))       #MOSTRA EM QUE POSICAO ESTRA O NUMERO "8" NA TUPLA

pessoa = ("Gustavo", 39, "M", 99.88)
print(pessoa)           #TUPLAS PODEM TER MAIS DE UM TIPO DE DADO
del(pessoa)             #APAGA A TUPLA 