"""Crie um programa que vai ler varios números e colocar em uma lista. Depois disso, crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados,
respectivamente. Ao final, mostre o conteúdo das tres listas geradas."""
#Determinar vetores
lista = []
lista_par = []
lista_impar = []


cont = 0
while True:
    num = int(input(f"Digite o {cont+1}º valor: "))
    opcao = str(input("Deseja continuar? (S/N) ")).upper()
    cont += 1
    lista.append(num)
    if opcao == "N":
        print("Programa finalizado.")
        break

for numero in lista:
    if numero % 2 ==0:
        lista_par.append(numero)
    elif numero % 2 != 0:
        lista_impar.append(numero)
 
print(f"A lista completa é {lista}")
print(f"A lista de pares é {lista_par}")
print(f"A lista de ímpares é {lista_impar}")