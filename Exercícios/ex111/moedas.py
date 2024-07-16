def aumentar(valor=0, taxa=0, sit=False):
    """Função para efetuar um aumento de determinado valor

        :param valor: Numero inicial
        :param taxa: Porcentagem que deseja aumentar
        :return: Retorna o resultado da equação
        """
    res = valor + (valor * taxa/100)
    if sit:
        return res
    else:
        return moeda(res)


def diminuir(valor=0, taxa=0, sit=False):
    """Função para retornar a diminuição de dois números

    :param x: Valor inicial a ser diminuido
    :param y: Valor a ser diminuido"""

    res = valor - (valor * taxa/100)
    if sit:
        return res
    else:
        return moeda(res)



def dobro(valor=0, sit=False):
    """Função para dobrar o valor inicial

    :param valor: Valor a ser dobrado
    """

    res = valor * 2
    if sit:
        return res
    else:
        return moeda(res)


def metade(valor=0, sit=False):
    """Função para retornar a metade do valor inicial

    param valor: Valor a ser dividido por 2
    """

    res = valor / 2
    if sit:
        return res
    else:
        return moeda(res)


def moeda(valor=0, moeda = "R$"):
    """Função para retornar um valor formatando o mesmo

        :param valor: Valor aa ser formatado
        :return: Retorna o valor já formatado"""
    return f"{moeda}{valor:.2f}".replace(".",",")


def resumo(função):
    return help(função)
