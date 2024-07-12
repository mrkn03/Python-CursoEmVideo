#46. Crie um programa que faça o computador jogar jokenpo (PEDRA, PAPEL OU TESOURA) com voce.
import random
usuario = str(input('VAMOS JOGAR PEDRA, PAPEL OU TESOURA, ESCOLHA UM DELES:')).upper()
computador = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
if usuario == 'PEDRA' and computador == 'PAPEL':
    print('VOCÊ ESCOLHEU {} E EU ESCOLHI {}, VOCÊ PERDEU!'.format(usuario, computador))
elif usuario == 'PAPEL' and computador == 'TESOURA':
    print('VOCÊ ESCOLHEU {} E EU ESCOLHI {}, VOCÊ PERDEU!'.format(usuario, computador))
elif usuario == 'TESOURA' and computador == 'PEDRA':
    print('VOCÊ ESCOLHEU {} E EU ESCOLHI {}, VOCÊ PERDEU!'.format(usuario, computador))
elif usuario == 'PEDRA' and computador == 'TESOURA':
    print('VOCÊ ESCOLHEU {} E EU ESCOLHI {}, PARABÉNS VOCÊ ME VENCEU!'.format(usuario, computador))
elif usuario == 'PAPEL' and computador == 'PEDRA':
    print('VOCÊ ESCOLHEU {} E EU ESCOLHI {}, PARABÉNS VOCÊ ME VENCEU!'.format(usuario, computador))
elif usuario == 'TESOURA' and computador == 'PAPEL':
    print('VOCÊ ESCOLHEU {} E EU ESCOLHI {}, PARABÉNS VOCÊ ME VENCEU!'.format(usuario, computador))
elif usuario == computador:
    print('VOCÊ ESCOLHEU {} E EU ESCOLHI {}, NINGUÉM VENCEU'.format(usuario, computador))