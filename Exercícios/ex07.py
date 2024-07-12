#07. Crie um algoritimo  que leia um numero e mostre o seu dobro, seu triplo e sua raiz quadrada.
n1 = int(input('digite um numero: '))

d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)

print('o dobro deste numero é {} o seu triplo é {} e a sua raiz quadrada é{}'.format(d,t,r))