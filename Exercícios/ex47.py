#47. Faça um programa que mostre na tela uma contagem regressiva para os estouros de fogos de artificio,
#indo de 10 até 0, com um intervalo de 1 segundo entre eles.
from time import sleep
import emoji
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Feliz ano novo!!!')
print(emoji.emojize('🎉🎉🎉🎉🎉🎉🎉'))