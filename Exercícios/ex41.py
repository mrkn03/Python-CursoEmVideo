#41. Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
#final, de acordo com a média atingida:
    # média abaixo de 5.0: REPROVADO
    # média entre 5.0 e 6.9: RECUPERAÇÃO
    # média 7.0 ou superior: APROVADO
nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite a sua segunda nota:'))

média = (nota1 + nota2) / 2

if média < 5.0:
    print('Você foi REPROVADO')
elif 5.0 <= média <= 6.9:
    print('Você esta de RECUPERAÇÂO')
elif média >= 7.0:
    print('Parabens você foi APROVADO')
