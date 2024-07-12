"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso"""
numero = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
extenso = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove",
           "dez","onze","douze","treze","quatroze","quinze","dezeseis","dezesete",
           "dezoito","dezenove","vinte")


while True:
    escolha = int(input("Escolha um número entre 0 e 20: "))
    if escolha < 0 and escolha > 20:
        escolha = int(input("Número escolhido incorreto. Digite novamente! "))
    else:
        print(f"Você digitou o número {extenso[escolha]}")