# Escreva um programa que calcule a média dos números pares digitados pelo usuário. Termine a leitura se o usuário digitar zero (0).

contador = 0 
soma_pares = 0

num = 1
while num != 0:
    num = int(input('Numero: '))
    if num % 2 == 0 and num != 0:
        soma_pares += num
        contador += 1

print('A média de números pares é: {}'.format(soma_pares /  contador))