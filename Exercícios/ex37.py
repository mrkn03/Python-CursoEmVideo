#37. Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. o programa vai
#perguntar o valor da casa, o salario do comprador e em quantos anos ela vai pagar.
    #calcule o valor da prestação mensal, sabendo que ela nao pode execer 30% do salario ou entao o
    #emprestimo sera negado
casa = float(input('Qual é o valor da casa que deseja comprar: RS$'))
salario = float(input('Qual o seu salario: RS$'))
tempo = int(input('Em quantos anos o(a) senhor(a) quer pagar o financiamento? '))

prestação = casa / (tempo * 12)
if prestação < salario - (salario * (30/100)):
    print('O senhor pagará RS${:.2f} por mês durante {} meses.'.format(prestação, (tempo * 12)))
elif prestação > salario - (salario * (30/100)):
    print('O senhor não poderá financiar essa casa, pois a prestação exede 30% do seu salario, dando um valor de RS${}'.format(prestação))
