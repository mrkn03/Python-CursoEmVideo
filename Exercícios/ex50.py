#50. Refaça o exercicio 09, mostrando a tabuada de um número que o usuário escolher, só que agora usando 
#um laço for.

for c in range(0, 2):
    n1 = int(input('Digite o primeiro valor inteiro a ser multiplicado: '))
    n2 = int(input('Digite o segundo valor inteiro a ser multiplicado: '))
    m = n1 * n2
    print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, m))

#Outra alternativa para o exercicio
n = int(input('Informe o numero que você queira saber a tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))