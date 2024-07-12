#Interective Help
help(print)
print(input.__doc__)


#Docstrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
        -parametro i: início da contagem
        -parametro f: fim da contagem
        -parametro p: passo da contagem
        -return: sem retorno
        """
    c= i
    while c <= f:
        print(f"{c}", end=" ")
        c += p 
    print("FIM!")

help(contador)


#Parametros opcionais
def somar(a=0, b=0, c=0): #Parametros limitados
    """
    -> Faz a soma de três valoes e mostra o resultado na tela.
        -parametro a: o primeiro valor
        -parametro b: o segundo valor
        -parametro c: o terceiro valor
    """
    s = a +b + c
    print(f"A soma vele {s}")


somar(3, 2, 5)
somar(8, 4)
somar(3)


#Escopo de variáveis
def funcao():
    n1 = 4  #Variavel local
    print(f"N1 dentro vale {n1}")


n1 = 2  #Variavel gloval
funcao()
print(f"N1 fora vale {n1}")


#Retorno de valores
def somar(a=0, b=0, c=0): #Parametros limitados
    """
    -> Faz a soma de três valoes e mostra o resultado na tela.
        -parametro a: o primeiro valor
        -parametro b: o segundo valor
        -parametro c: o terceiro valor
    """
    s = a +b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f"Os resultados foram {r1}, {r2} e {r3}")