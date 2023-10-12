# Escreva um programa que imprime os N primeiros números da sequência de Fibonacci.

numero = int(input("Quantos números de Fibonacci você deseja imprimir? "))
a, b = 0, 1

for i in range(N):
    print(a, end=" ")  
    a, b = b, a + b  

print()