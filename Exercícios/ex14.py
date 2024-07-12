#14. Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
sa = float(input('informe o seu salario atua. R$'))
ns = sa + (sa*(15/100))

print('o seu novo salario com aumento é R${}'.format(ns))