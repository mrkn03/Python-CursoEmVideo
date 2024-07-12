#27. Faça um programa que leia uma frase pelo teclado e mostre:
    #a) quantas vezes aparece a letra 'A'.
frase = input('Digite uma frase: ').upper().strip()

print('A letra A aparece {} vezes'.format(frase.count('A')))

    #b) em que posição ela aparece a primeira vez.
frase = input('Digite uma frase: ').upper().strip()

print('Ela aparece pela primeira vez na posição: {}'.format(frase.find('A')+1))

    #c) em que posição ela aparece a ultima vez.
frase = input('Digite uma frase: ').lower().strip()
print('Ela aparece pela ultima vez na posição: {}'.format(frase.rfind('a')+1))