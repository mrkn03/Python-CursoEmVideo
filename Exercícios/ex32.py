#32. Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem,
#cobrando RS$0.50 por Km para viagens de até 200Km e RS$0.45 para viagens mais longas.
distancia = float(input('Digite a distancia da viagem em Km: '))

if distancia <= 200:
    print('O valor da passagem é RS${}'.format(distancia * 0.50))

else:
    print('O valor da passagem é RS${}'.format(distancia * 0.45))