#05. Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela

n = input('Digite algo: ')

print('O tipo primitivo deste valor é: ', type(n))
print('Este valor é numerico? ',n.isnumeric())
print('Este valor é alfabetico? ',n.isalpha())
print('este valor tem espaços? ', n.isspace())
print('Este valor é alfanumerico? ', n.isalnum())
print('este valor esta em maiuscula? ', n.isupper())
print('Este valor esta em minuscula? ', n.islower())
print('Este valor esta capitalizado? ', n.istitle())