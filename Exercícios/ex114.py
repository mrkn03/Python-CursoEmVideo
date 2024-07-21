"""Crie um codigo em Python que teste se o site Pudim esta acessivel pelo computador usado."""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen(('https://www.pudim.com.br/'))
except urllib.error.URLError:
    print("O site www.pudim.com.br esta indiponivel no momento.")
else:
    print("O site www.pudim.com.br esta disponivel.")