pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}

print(pessoas["nome"])  #Imprimir apenas nome

print(pessoas["idade"]) #Imprimir apenas idade

print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")   #Imprimir valores

print(pessoas.keys())   #Ira mostrar apenas as keys

print(pessoas.values()) #Ira mostrar apenas os valores

print(pessoas.items())  #Ira mostrar os items

#Mostrar as keys
for k in pessoas.keys():
    print(k)

#Mostrar os valores
for v in pessoas.values():
    print(v)

#Mostrar os itens
for i in pessoas.items():
    print(i)

#Mostrar duas coisas
pessoas["Nome"] = "Leandro"
pessoas["peso"] = 98.5
for k, v in pessoas.items(): #No dicionário é usado o items
    print(f"{k} = {v}")


#Criar dicionário dentro de uma lista
brasil = []
estado1 = {"UF": "Rio de Janeiro", "Sigla": "RJ"}
estado2 = {"UF": "São Paulo", "Sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]["UF"])
print(brasil[1]["Sigla"])

#Lendo listas
estado = {}
brasil = []

for i in range(3):
    estado["UF"] = str(input("Unidade Federativa: ")).capitalize()
    estado["Sigla"] = str(input("Sigla do estado: ")).upper()
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for v in e.values():
        print(v, end = " ")
    print()