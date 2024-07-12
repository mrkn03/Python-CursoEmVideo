#33. Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0:
    print('O ano de {} é bissexto.'.format(ano))

else:
    print('O ano de {} não é bissexto.'.format(ano))