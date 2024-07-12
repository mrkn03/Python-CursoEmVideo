#55. Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda
#nao atingiram a maioridade e quantas ja sao maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))