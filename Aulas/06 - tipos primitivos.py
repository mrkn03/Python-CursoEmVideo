int #para numeros inteiros
exemplo = 1, 2, 3, 4, -1234

float #para numeros reais
exemplo = 2.5, 5.04, 0.134512, -15.1234123

bool  #valores lógicos ou booleanos
exemplo = True, False

str  #valores caracteres ou strings
exemplo = 'ola', 'bom', 'hoje'

n = input('Digite algo: ')

print('O tipo primitivo deste valor é: ', type(n))
print('Este valor é numerico? ',n.isnumeric())
print('Este valor é alfabetico? ',n.isalpha())
print('este valor tem espaços? ', n.isspace())
print('Este valor é alfanumerico? ', n.isalnum())
print('este valor esta em maiuscula? ', n.isupper())
print('Este valor esta em minuscula? ', n.islower())
print('Este valor esta capitalizado? ', n.istitle())