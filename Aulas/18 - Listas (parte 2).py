teste = []
teste.append("Gustavo")
teste.append(40)
galera = []
galera.append(teste[:]) #Cria uma cópia da lista
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:]) #Cria uma cópia da lista
print(galera)


galera2 = [["Joao", 19], ["Ana", 33], ["Joaquim", 13] , ["Maria", 45]]
print(galera2)
#print(galera2[0][0]) #"Escolhe" qual elemento vai mostrar
for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idadea")

galera3 = []
dado = []
total_maior = 0
total_menor = 0
for c in range(0,5):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera3.append(dado[:])
    dado.clear()

for p in galera3:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        total_maior += 1
    else:
        print(f"{p[1]} é menor de idade")
        total_menor += 1
print(f"Temos {total_maior} maiores e {total_menor} menores de idade")