#52. Desenvolva um programa que leia o primeiro termo e a razao de uma PA. no final, mostre os 10 primeiros 
#termos dessa progressão.
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
d = p + (10-1) * r
for c in range(p, d + r, r):
    print('{}'.format(c), end=', ')
print('ACABOU!')
