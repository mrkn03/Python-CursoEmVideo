"""Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade de digitação de um número
de tipo inválido. Aproveite e crie tambem uma função leiaFloat() com a mesma funcionalidade."""
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero inteiro valido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mEntrada de dados interrompida pelo usuário.\033[m ")
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero real valido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrompita pelo usuário.\033[m")
            return 0
        else:
            return n


num = leiaint("Digite um inteiro: ")
num2 = leiafloat("Digite um real: ")