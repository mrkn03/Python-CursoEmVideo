"""Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os ultimso 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética
D) em que posicao na tabela esta o time da chapecoense"""

brasileirao = ("Flamengo","Bahia","Botafogo","São Paulo","Atlético Paranaense",
               "RB Bragantino","Palmeiras","Internacional","Cruzeiro","Atlético-MG",
               "Fortaleza EC","Juventude","Gremio","Vasco da Gama","Fluminense","Criciuma",
               "Corinthians","Atletico Goianiense","Vitoria","Cuiaba")

print("CLASSIFICAÇÃO DO BRASILEIRÃO:")
for i in range(0,20):
    print(f"O {i+1}º é o time do(a) {brasileirao[i]}")
print()
print("OS 5 PRIMEIROS COLOCADOS:")
for i in range(0,5):
    print(f"O {i+1}º colocado é o {brasileirao[i]}")
print()
print("OS ULTIMOS 4 COLOCADOS")
for i in range(16,20):
    print(f"O {i+1} colocado é o {brasileirao[i]}")
print()
print("OS TIMES EM ORDEM ALFABÉTICA")
print(sorted(brasileirao))
print()
if "Chapecoense" in brasileirao:
    print(f"O Chapecoense esta na {brasileirao.index("Chapecoense")+1} posição")
else:
    print("O time da Chapecoense não esta na tabela da serie A")