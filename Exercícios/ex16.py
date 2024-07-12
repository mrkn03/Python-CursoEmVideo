#16. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
qd = int(input('Informe a quantidade de dias que o carro foi alugado: '))
km = float(input('Informe a quantidade de km percorrido: '))

qk = qd * 60
ck = km * 0.15

t = qk + ck
print('O preço total a ser pago é igual a R${:.2f}'.format(t))