#58. Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. caso esteja errado
#peça a digitação novamente até ter um valor correto.
'''Primeira forma'''
c = 'S'
while c == 'S':
    sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
    if sexo == 'F':
        print('O sexo informado foi FEMININO')
    elif sexo == 'M':
        print('O sexo informado foi MASCULINO')
    c = str(input('Quer continuar? [S/N]')).upper()

'''Segunda forma'''
sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format())