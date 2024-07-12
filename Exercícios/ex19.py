#19. Faça um programa que leia um angulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente.
import math
a = float(input('Digite um angulo qualquer: '))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))

print('O seno do angulo de {}° é igual a {:.2f}.'.format(a,sen))
print('O cosseno do angulo de {}° é igual a {:.2f}.'.format(a,cos))
print('A tangente do angulo de {}° é igual a {:.2f}.'.format(a,tg))