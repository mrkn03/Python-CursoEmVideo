"""Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleiçoes."""
def voto(ano_nascimento):
    """Função verifica sua idade e sua situação eleitoral

    Args:
        ano_nascimento (int): Recebe ano de nascimento para verificar idade
    """
    from datetime import date

    atual = date.today().year
    idade = atual - ano_nascimento
    if idade < 16:
        return f"Você tem {idade} anos e NÃO PODE VOTAR"
    elif idade <=18 or idade >= 65:
        return f"Voê tem {idade} anos e o voto é OPCIONAL"
    else:
        return f"Você tem {idade} anos e o voto é OBRIGATÓRIO"
    

#programa principal
print(voto(int(input("Digite o ano em que nasceu: "))))