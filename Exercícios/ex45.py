#45. Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL
# e CONDIÇÂO DE PAGAMENTO:
    # A vista dinheiro/cheque: 10% de desconto
    # A vista no cartao: 5% de desconto
    # Em até 2x no cartao: preço normal
    # 3x ou mais: 20% de juros
print('-' * 40)
preço = float(input('Informe o preço do produto: RS$'))
pagamento = str(input("""Selecione a forma de pagamento:
[1] A VISTA DINHEIRO/CHEQUE COM DESCONTO DE 10%
[2] A VISTA NO CARTÃO COM DESCONTO DE 5%
[3] ATÉ 2X NO CARTÃO SEM JUROS
[4] 3X OU MAIS NO CARTÃO COM JUROS DE 20%
QUAL SUA OPÇÃO?  """))
if pagamento == '1':
    print('O valor do produto de {} irá para {} com 10% de desconto'.format(preço, preço - (preço *(10/100))))
elif pagamento == '2':
    print('O valor do produto de {} irá para {} com 5% de desconto'.format(preço,preço - (preço * (5/100))))
elif pagamento == '3':
    parcelas = int(input('Em quantas parcelas? '))
    if parcelas > 3:
        print('Opção errada, tente novamente')
    print('O valor do produto de {} irá para {:.2f} em até 2x no cartao sem juros'.format(preço, preço / parcelas))
elif pagamento == '4':
    parcelas = int(input('Em quantas parcelas? '))
    if parcelas < 4:
        print('Opção errada, tente novamente')
    print('O valor do produto de {} irá para {} acima de 3x no cartao com 20% de juros'.format(preço, (preço + (preço * 20/100)) ))
print('-' * 40)