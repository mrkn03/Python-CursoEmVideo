#if carro.esquerda():

#elif carro.direita():

#elif carro.ré():

#else carro.siga():

#----------------- EXEMPLOS -------------------
#01.
nome = str(input('Digite seu nome:')).capitalize()

if nome == 'gustavo':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia {}'.format(nome))
