#38. Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera
#a base de conversao. 
    # 1 para binario 
    # 2 para octal
    # 3 para hexadecimal
num = int(input('Digite um numero inteiro qualquer: '))
print("""escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal
""")
opçao = input('Sua opção:')
if opçao == '1':
    print('O numero {} convertido para binário é {}'.format(num, bin(num)))
elif opçao == '2':
    print('O numero {} convertido para octal é {}'.format(num, oct(num)))
elif opçao == '3':
    print('O numero {} convertido para hexadecimal é {}'.format(num, hex(num)))
else:
    print('Opçao invalida, tente novamente')