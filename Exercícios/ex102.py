"""Crie um programa que tenha uma função fatorial() que receba dois parametros: O primeiro que indique o número a calcular e o outro chamado show, que sera um valor lógico (opcional)
indicando se um sera mostrado ou não na tela o processo de calculo do fatorial."""
def fatorial(n, show=False):
    """Função para mostrar fatorial de um valor

    Args:
        n (int): Numero a ser calculado
        show (bool, optional): Mostrar ou não o calculo. Defaults to False.

    Returns:
        int: Retorna valor de fatorial de numero n
    """
    f = 1
    for i in range(n, 0 ,-1):
        if show:
            print(i, end=" ")
            if i > 1:
                print(f"x", end=" ")
            else:
                print(" = ", end= " ")
        f *= i
    return f

    


print(fatorial(5))