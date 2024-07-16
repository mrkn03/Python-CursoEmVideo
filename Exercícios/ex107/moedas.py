def aumentar(valor, taxa):
    """Função para efetuar um aumento de determinado valor

        :param valor: Numero inicial
        :param porcentagem: Porcentagem que deseja aumentar
        :return: Retorna o resultado da equação
        """
    return valor +(valor * taxa/100)

def diminuir(valor, taxa):
    """Função para retornar a diminuição de dois números

    :param x: Valor inicial a ser diminuido
    :param y: Valor a ser diminuido"""
    return valor - (valor * taxa/100)



def dobro(valor):
    """Função para dobrar o valor inicial

    :param valor: Valor a ser dobrado
    """

    return valor * 2


def metade(valor):
    """Função para retornar a metade do valor inicial

    param valor: Valor a ser dividido por 2
    """

    return valor / 2