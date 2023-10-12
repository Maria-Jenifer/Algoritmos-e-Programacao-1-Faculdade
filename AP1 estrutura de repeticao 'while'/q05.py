# Escreva um programa que gere os números de 1000 a 1999 e escreva aqueles que dividido por 11 dão resto igual a 5.

for i in range(1000, 2000):
    if i % 11 == 5:
        print(i)
        