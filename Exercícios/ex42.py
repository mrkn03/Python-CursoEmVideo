#42. A confederaçao de nataçao precisa de um programa que leia o ano de nascimento de um atleta e mostre
#sua categoria, de acordo com sua idade:
    # até 9 anos: MIRIM
    # até 14 anos: INFANTIL
    # até 19 anos: JUNIOR
    # até 20 anos: SENIOR
    # acima: MASTER
idade = int(input('Digite a sua idade:'))

if idade <= 9:
    print('Você esta na equipe MIRIM')
elif idade <= 14:
    print('Você esta na equipe INFANTIL')
elif idade <= 19:
    print('Você esta na equipe JUNIOR')
elif idade <= 20:
    print('Você esta na equipe SENIOR')
elif idade > 20:
    print('Você esta na equipe MASTER')