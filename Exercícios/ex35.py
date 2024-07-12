#35. Escreva um programa que leia o salario de um funcionario e calcule o valor do seu aumento.
    #Para salarios superiores a RS#1250, calcular um aumento de 10%
    #Para salarios inferiores a RS$1250, calcular um aumento de 15%
salario = float(input('Digite o salário do funcionário: RS$'))

if salario > 1250:
    print('Com 10% de aumento o seu novo salário é RS#{}'.format(salario + (salario * 10/100)))

else:
    print('Com 15% de aumento o seu novo salário é RS${}'.format(salario + (salario * (15/100))))