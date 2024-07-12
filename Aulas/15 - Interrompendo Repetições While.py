bloco = 0
bloco_vazio = 0
moeda = 0
trofeu = 0
while True: #Looping infinito
    if bloco:
        print('Passo')
    if bloco_vazio:
        print('Pula')
    if moeda:
        print('Pega')
    if trofeu:
        print('Pula')
        break #Jogar 'para fora' da estrutura de repetição
print('Pega')

'''Exemplos:'''
'''cont = 1
while cont <= 10:
    print(cont, '->', end='')
    cont += 1
print('Acabou')'''

s = n = 0
n = int(input('Digite um número: '))
while True:
    if n == 999:
        break
    s += n
#print('A soma é igual a {}'.format(s))
print(f'A soma é igual a {s}')