#23. Crie um programa que leia o nome completo de uma pessoa e mostre:
#a) o nome com todas as letras maiusculas.
#b) o nome com todas as letras minusculas.
#c) quantas letras ao todo (sem considerar espaço).
#d) quantas letras tem o primeiro nome.
nome = str(input('Digite o seu nome completo: '))
nome1 = nome.split()

print('Seu nome em maiusculo é:{}'.format(nome.upper()))
print('Seu nome em minusculo é:{}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(len(nome1[0])))