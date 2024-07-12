"""Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação(opicional)
Adicionar tambem as docstrings da função."""
def notas(cont, sit=False):
    relatorio = {}

    for i in range(cont):
        relatorio["Nome:"] = str(input(f"Nome do {i+1}º aluno: "))
        relatorio["Nota:"] = float(input(f"Nota do {i+1}º aluno: "))

    relatorio["Maior:"] = 0
    relatorio["Menor:"] = 999
    relatorio["Media:"] = 0

    for i in range(cont):
        relatorio["Media:"] += relatorio["Nota:"] / cont

    for i in range(cont):
        if relatorio["Nota:"] > relatorio["Maior:"]:
            relatorio["Maior:"] = relatorio["Nota:"]
    
    for i in range(cont):
        if relatorio["Nota:"] < relatorio["Menor:"]:
            relatorio["Menor:"] = relatorio["Nota:"]

    for k, v in relatorio.items():
        print(f"{k} : {v}")
    
    if sit:
        if relatorio["Media:"] < 6:
            print("Situação: RUIM")
        elif 6 == relatorio["Media:"] <=7:
            print("Situação: BOM")
        else:
            print("Situação: EXCELENTE")



cont = int(input("Você vai digitar as notas de quantos alunos? "))
situacao = bool(input("Deseja ver a situação (True/False)? "))
notas(cont, situacao)