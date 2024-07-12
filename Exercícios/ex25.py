#25. Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'SANTO'.
cidade = input('Digite o nome da sua cidade: ').lower()
cidade = cidade.strip()
print('santo' in cidade)
