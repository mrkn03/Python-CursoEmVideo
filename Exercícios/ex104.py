"""Crie um programa que tenha uma função leiaint(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numerico.
Ex: n = leiaint("Digite um n")
"""
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO. Digite um numero inteiro\033[m")
        if ok:
            break
    return valor


n = leiaint("Digite um numero: ")
print(f"Voce digitou o numero {n}")