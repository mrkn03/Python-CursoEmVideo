"""Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os ultimso 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética
D) em que posicao na tabela esta o time da chapecoense"""

brasileirao = ("Flamengo","Bahia","Botafogo","São Paulo","Atlético Paranaense",
               "RB Bragantino","Palmeiras","Internacional","Cruzeiro","Atlético-MG",
               "Fortaleza EC","Juventude","Gremio","Vasco da Gama","Fluminense","Criciuma",
               "Corinthians","Atletico Goianiense","Vitoria","Cuiaba")

print(f"Lista de times do Brasileirão: {brasileirao}")
print()
print(f"Os 5 primeiros colocados: {brasileirao[0:5]}")
print()
print(f"Os ultimos 4 colocados: {brasileirao[-4:]}")
print()
print(f"Lista com os times em ordem alfabéfica: {sorted(brasileirao)}")
print()
if "Chapecoense" in brasileirao:
    print(f"O Chapecoense esta na {brasileirao.index("Chapecoense")+1} posição")
else:
    print("O time Chapecoense não esta na serie A do Brasileirão")
