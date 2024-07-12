#44. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, Calcule seu IMC e mostre seu status,
#de acordo com a tabela abaixo
    # Abaixo de 18.5: ABAIXO DO PESO
    # Entre 18.5 e 25: PESO IDEAL 
    # Entre 25 e 30: SOBREPESO
    # Entre 30 e 40: OBESIDADE
    # Acima de 40: OBESIDADE MÓRBIDA
peso = float(input('Digite o seu peso em Kg:'))
altura = float(input('Digite sua altura:'))

IMC = peso / (altura ** 2)
if IMC < 18.5:
    print('O seu IMC foi de {:.1f} e você esta abaixo do peso ideal'.format(IMC))
elif 18.5 <= IMC < 25:
    print('O seu IMC foi de {:.1f} e você esta no peso ideal.'.format(IMC))
elif 25 <= IMC < 30:
    print('O seu IMC foi de {:.1f} e você esta no sobrepeso.'.format(IMC))
elif 30 <= IMC <= 40:
    print('O seu IMC foi de {:.1f} e você esta na obesidade.'.format(IMC))
elif IMC > 40:
    print('O seu IMC foi de {:.1f} e você esta na obesidade morbida.'.format(IMC))