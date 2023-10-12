# Escreva um programa que lê um valor n inteiro e positivo e que calcula a seguinte soma:  
# S := 1 + 1/2 + 1/3 + 1/4 + ... + 1/n


num = int(input('Número: '))
soma = 1
for n in range(2, num+1):
    soma += 1/n
print(soma)    