#28. Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o ultimo nome separadamente.
nome = input('Digite seu nome completo:').lower().split()

n0 = nome[0]
nl = nome[-1]
print('O seu primeiro nome é {}'.format(n0))
print('O seu ultimo nome é {}'.format(nl))
print('O seu primeiro e ultimo nome é {} {}.'.format(n0,nl))