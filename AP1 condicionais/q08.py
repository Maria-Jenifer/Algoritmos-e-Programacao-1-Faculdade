# 08) Escreva um programa que deverá realizar a leitura de um número inteiro da entrada padrão e deverá
# informar se o número é NEGATIVO, NULO ou POSITIVO.

num = int(input('Digite um numero inteiro: '))

if num < 0:
    print('O numero é negativo')
elif num == 0: 
    print('O numero é nulo')
else:
    print('O numero é positivo')