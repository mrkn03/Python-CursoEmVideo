#15. Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
tc = float(input('escreva a temperatura em °C: '))

f = (tc * 1.8) + 32

print('{}°C equivale a {:.2f}°F'.format(tc,f))