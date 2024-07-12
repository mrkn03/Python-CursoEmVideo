"""Crie um programa onde o usuario digite uma expressao qualquer que use parenteses. Seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos e fechados
na ordem correta"""
expressao = str(input("Digite a expressão: "))
pilha = []

for simbolo in expressao:
    if simbolo =="(":
        pilha.append("(")
    elif simbolo == ")":
        if len (pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão está válida.")
else:
    print("Sua expressão está inválida.")