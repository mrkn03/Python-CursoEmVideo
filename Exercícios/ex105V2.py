"""Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação(opicional)
Adicionar tambem as docstrings da função."""
def notas(*n, sit=False):
    """Função para gerar relatorio de notas de alunos 

        :param n: uma ou mais notas dos alunos (aceita varias)
        :param sit: valor bool opcional, indicando se deve ou nao adicionar a situação
        :return: dicionario com informaçoes da turma
    """
    r = {}
    r["Total"] = len(n)
    r["Maior"] = max(n)
    r["Menor"] = min(n)
    r["Media"] = sum(n) / len(n)

    if sit:
        if r["Media"] >= 7:
            r["Situação"] = "BOA"
        elif r["Media"] >= 5:
            r["Situação"] = "RAZOAVEL"
        else:
            r["Situação"] = "RUIM"
    return r


res = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(res)