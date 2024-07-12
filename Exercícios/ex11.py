#11. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. considere USD$1,00=3,27
c = float(input('digite quantos reais possui em sua carteira: '))

d = c / 3.27

print('voce pode comprar {:.3f} dolares'.format(d))