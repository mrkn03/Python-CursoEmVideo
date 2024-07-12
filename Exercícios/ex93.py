"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato"""
relatorio = {}
partidas = []

relatorio["Nome"] = str(input("Digite o nome do jogador: "))
cont = int(input(f"Digite quantas partidas o jogador {relatorio['Nome']} jogou: "))

for i in range(0,cont):
    partidas.append(int(input(f"Quantos gols {relatorio['Nome']} na {i+1}ª partida? - ")))

relatorio["Gols"] = partidas[:]
relatorio["Total"] = sum(partidas)

print("-"*40)
print(relatorio)

print("-"*40)
for k, v in relatorio.items():
    print(f"{k}: {v}")

print("-"*40)
print(f"    O jogador {relatorio['Nome']} jogou {len(relatorio['Gols'])} partidas.")
for  i, v in enumerate(relatorio["Gols"]):
    print(f"    Na partida {i+1} fez {v} gols")
print(f"    Total de gols: {relatorio['Total']}")
print("-"*40)