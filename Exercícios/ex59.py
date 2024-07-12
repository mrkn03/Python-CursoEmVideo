#59. Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. só que agora
#o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''import random
c = 'S'
t = 0
n = random.randint(0,10)
while c == 'S':
    numero = int(input('Escolha um número de 0 a 10:'))
    t = t + 1
    if numero == n:
        print('Parabéns você conseguiu acertar o número que eu estava pensando em {} tentativas'.format(t))
        c = str(input('Deseja continuar? [S/N] ')).upper()
    else:
        print('Você escolheu o número {}, não é nesse número que eu estou pensando'.format(numero))
    '''

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma ves.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acabou com {} tentativas. Parabéns'.format(palpites))
