#51. Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor impar, desconsidere-o.
s = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {} valor inteiro: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você informou {} numeros pares e o resultado foi {}'.format(cont, s))