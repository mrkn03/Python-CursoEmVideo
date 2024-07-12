#40. Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    # se ele ainda vai se alistar ao serviço militar 
    # se é a hora de se alistar
    # se ja passou do tempo de se alistar
# seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
alistamento = str(input('Voce ja se alistou à forças armadas?'))

if alistamento == 'sim':
    print('Parabens, voce esta com suas obrigações em dia')

elif alistamento == 'nao':
    ano = int(input('Em que ano você nasceu? '))
    idade = atual - ano
    saldo = 18 - idade
    if 2024 - ano < 18:
        print('Ainda faltam {} anos para você se alistar à forças armadas'.format(saldo))
    if 2024 - ano > 18:
        print('Você esta em atraso com suas obrigaçoes, aliste-se o mais rapido posivel')
    if 2024 - ano == 18:
        print('Você esta no ano exato para poder se alistar')