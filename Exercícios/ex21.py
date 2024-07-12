#21. O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 = input('Digite o nome do 1° aluno :')
a2 = input('Digite o nome do 2° aluno :')
a3 = input('Digite o nome do 3° aluno :')
a4 = input('Digite o nome do 4° aluno :')

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print('A ordem de apresentação dos trabalhos sera a seguinte: {}'.format(lista))