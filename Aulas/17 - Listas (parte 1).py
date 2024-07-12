num = [2, 5, 9, 1] #Lista original
num[2] = 3 #Alterar o valor ta lusta
num.append(7) #Adicionar um elemento
num.sort() #Colocar a lista em ordem crescente
num.sort(reverse=True) #Colocar a lista em ordem decrescente
num.insert(2, 0) #Adiciona o 0 na posição 2
num.pop() #elimina por padrao o elemento 1
num.remove() #Remove o valor que esta dentro da lista
print(f"Essa lista tem {len(num)} elementos.") #Mostrar quantos elementos tem a lista


valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f" Na posição {c} encontrei o valor {v}...", end="")
print()

lista = []

for i in range(0,5):
    lista.append(int(input("Digite um valor: ")))
print("Cheguei ao final da lista.")

a = [2,3,4,6]
b = a #Cria uma ligação entre as duas listas
b = a[:] #Lista B recebe uma cópia da lista A
b[2] = 8 #Lista A e lista B vai receber o valor 8 na posição 2

print(f"Lista A: {a}")
print(f"Lista B: {b}")