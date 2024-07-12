#12. Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²
l = float(input('digite a largura de sua parede em metros: '))
a = float(input('digite a altura de sua parede em metros: '))

ar = l * a
t = ar / 2

print('a area de sua parede é {} e sera necessario {} litros de tinta'.format(ar,t))