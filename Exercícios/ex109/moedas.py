def aumentar(valor=0, taxa=0, sit=False):
    """Função para efetuar um aumento de determinado valor

        :param valor: Numero inicial
        :param taxa: Porcentagem que deseja aumentar
        :return: Retorna o resultado da equação
        """
    aumento = valor + (valor * taxa/100)
    if sit:
        return aumento
    else:
        return moeda(aumento)



def diminuir(valor=0, taxa=0, sit=False):
    """Função para retornar a diminuição de dois números

    :param x: Valor inicial a ser diminuido
    :param y: Valor a ser diminuido"""

    subtracao = valor - (valor * taxa/100)
    if sit:
        return subtracao
    else:
        return moeda(subtracao)



def dobro(valor=0, sit=False):
    """Função para dobrar o valor inicial

    :param valor: Valor a ser dobrado
    """

    dobro = valor * 2
    if sit:
      return dobro
    else:
        return moeda(dobro)



def metade(valor=0, sit=False):
    """Função para retornar a metade do valor inicial

    param valor: Valor a ser dividido por 2
    """

    metade = valor / 2
    if sit:
        return metade
    else:
        return moeda(metade)



def moeda(valor=0, moeda = "R$", sit=False):
    """Função para retornar um valor formatando o mesmo

        :param valor: Valor aa ser formatado
        :return: Retorna o valor já formatado"""
    if sit:
        return f"{moeda}{valor:.2f}".replace(".",",")
