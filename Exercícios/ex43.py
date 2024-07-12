#43. Refaça o exercicio 36 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera
#formado:
    # Equilatero: todos os lados iguais
    # Isoceles: dois lados iguais
    # Escaleno: todos os lados diferentes
a = float(input('Digite o primeiro segmento:'))
b = float(input('Digite o segundo segmento:'))
c = float(input('Digite o terceiro segmento:'))

if a < b + c and b < a + c and c < a + b:
    print('Esses segmentos podem formar um triangulo')
    if a == b == c:
        print('Esse triangulo é Equilatero')
    if a == b != c or a == c != b or b == c != a:
        print('Esse triangulo é Isoceles')
    if a != b != c != a:
        print('Esse triangulo é Escaleno')
else:
    print('Esses segmentos nao podem formar um triangulo')

