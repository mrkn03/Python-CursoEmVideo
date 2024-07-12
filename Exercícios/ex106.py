"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuario digitar a palavra "FIM", o programa 
se encerrará.
OBS: use as cores.
"""
def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg)
    print("~"*(tam+4))
    print(f"  {msg}")
    print("~"*(tam+4))


comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELP", )
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO!")