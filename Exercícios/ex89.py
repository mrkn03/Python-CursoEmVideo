"""Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente."""
ficha = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [ nota1, nota2], media])
    
    opcao = str(input("Deseja continuar? (S/N) ")).upper()
    if opcao == "N":
        break

print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f"{i+1:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    opcao = int(input("Deseja mostrar notas de qual aluno? (999 para parar"))
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')