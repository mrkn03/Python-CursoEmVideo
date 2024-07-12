#54. Crie um programa que leia uma frase qualquer e diga se ela pe um palindromo, desconsiderando os espaços.
    #Ex: APOS A SOPA
    #A SACADA DA CASA
    #O LOBO AMA O BOLO 
    #A TORRE DA DERROTA
    #ANOTARAM A DATA DA MARATONA
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')