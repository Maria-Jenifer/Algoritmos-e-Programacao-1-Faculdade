# 05) Escreva um programa que deverá ler da entrada três números inteiros A, B e C e deverá informar se 
# A+B é maior ou igual ao valor de C.

a = int(input('Número a: '))
b = int(input('Número b: '))
c = int(input('Número c: '))

if a + b >= c:
    print('a+b é maior ou igual a c')
else:
    print('a+b é menor que c')