#09. Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
n1 = float(input('digite o tamanho de sua parede em metros: '))

km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000

print('o tamanho da sua parede em km é {} em hm é {} em dam {} em dm é {} em cm é {} e em mm é {}'. format(km,hm,dam,dm,cm,mm))