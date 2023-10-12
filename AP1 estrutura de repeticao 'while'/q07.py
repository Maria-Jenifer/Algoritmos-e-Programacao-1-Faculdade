# Faça um programa que calcula os 20 primeiros números primos, dados os três primeiros 1, 2 e 3.

qtd_primos = 1
n = 1
while qtd_primos <= 20:
    contador = 0
    for i in range (1, n+1):
        if n % i == 0:
            contador += 1 

    if contador == 2:
        print(n,' É primo')
        qtd_primos += 1  
    n += 1