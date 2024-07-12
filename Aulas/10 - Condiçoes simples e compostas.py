#Condicionais

if carro.esquerda():
    bloco True

else:
    bloco False

#------------------ EXEMPLO -------------------
#01. Condicional Composta
tempo = int(input('Quantos anos tem o seu carro? .'))
if tempo <= 3:
    print('Carro novo')

else:
    print('Carro velho')

print('--FIM--')

#02. Condicional Simplificada
tempo = int(input('Quantos anos tem o seu carro? .'))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('--FIM--')

#03. Condicional Simples
nome = str(input('Digite seu nome: ')).capitalize()
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print('Bom dia, {}!.'.format(nome))

#04. Condição Composta
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2) / 2

print('A sua média foi {:.1f}'.format(m))
if m >=6: 
    print('Sua média foi boa, parabens!')

else:
    print('Sua média foi ruim, estude mais!')
