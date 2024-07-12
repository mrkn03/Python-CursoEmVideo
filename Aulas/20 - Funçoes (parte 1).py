def soma(a,b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"Soma = {s}")
    print("-"*30)


#Programa Principal
soma(b = 4, a = 5)
soma(8,9)
soma(2,1)


#Usando enpacotamento
def contador(* num):
    tam = len(num)
    print(f"Recebi os valores {num} e sao ao todos {tam} numeros")


contador(2,1,7)
contador(9, 0)
contador(4, 4, 7, 6, 2)


#Usando lista
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


#Usando enpacotamento
def soma(*valores):
    s = 0 
    for num in valores:
        s += num
    print(f"Somandos os valores {valores} temos {s}")


soma(5,2)
soma(2, 9, 4)