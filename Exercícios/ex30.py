#30. Escreva um programa que leia a velocidade de um carro.
    #se ele ultrapassar 80km/, mostre uma mensagem dizendo que ele foi multado.
    #a multa vai custar RS$7.00 por cada Km acima do limite.
km = int(input('Informe a velocidade do seu carro: '))

if km > 80:
    m = 7 * (km - 80)
    print('Você foi multado em RS${}, por estar acima da velocidade permitida na via'.format(m))

else:
    print('Você esta na velocidade correta da via')
