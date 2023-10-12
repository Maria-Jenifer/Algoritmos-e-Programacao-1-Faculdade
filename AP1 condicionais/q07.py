# 07) Escreva um programa que deverá ler dois números inteiros X e Y e o programa deverá apresentar os números
# em ordem crescente. 

x = int(input('Escreva o valor de x: '))
y = int(input('Escreva o valor de y: '))

if x < y:
    print('Numeros em ordem crescente:', x, y)
else:
    print('Numeros em ordem crescente', y, x)