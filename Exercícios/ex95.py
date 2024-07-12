"""Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização detalhada do aproveitamento de cada jogador"""
time = []
relatorio = {}
partidas = []

while True:
    relatorio.clear()
    relatorio["Nome"] = str(input("Digite o nome do jogador: ")).capitalize()
    cont = int(input(f"Digite quantas partidas o jogador {relatorio['Nome']} jogou: "))
    partidas.clear()

    for i in range(0,cont):
        partidas.append(int(input(f"Quantos gols {relatorio['Nome']} na {i+1}ª partida? - ")))

    relatorio["Gols"] = partidas[:]
    relatorio["Total"] = sum(partidas)
    time.append(relatorio.copy())

    while True:
        opcao = str(input("Deseja continuar? (S/N) - ")).upper()[0]
        if opcao in "SN":
            break
        print("Opção inválida. Informe apenas S ou N")
    if opcao == "N":
        break

print("-"*40)
print(" Cod  ", end= "")
for i in relatorio.keys():
    print(f"{i:<15}", end = "")
print()
print("-"*40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end= "")
    for d in v.values():
        print(f"{str(d):<15}", end= "")
    print()
        
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) - "))
    if busca == 999:
        break
    if busca >= len(time):
        print("Jogador inexistente. Informe outro jogador ")
    else:
        print(f"Relatório do jogador {time[busca]["Nome"]}: ")
        for i, g in enumerate(time[busca]["Gols"]):
            print(f"    No jogo {i+1} fez {g} gols.")
    print("-"*40)