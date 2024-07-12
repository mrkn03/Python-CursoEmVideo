"""Faça um programa que leia nome e média de um aluno, guardando tambem a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""
aluno = {}

aluno["Nome"] = str(input("Digite o nome do aluno: ")).capitalize()
aluno["Média"] = float(input(f"Digite a média do {aluno['Nome']}: "))

if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
elif 5 <= aluno["Média"] <7:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"

print(" "*10,"Relatório Semestral")
for k, v in aluno.items():
    print(f"{k} é igual a {v}")