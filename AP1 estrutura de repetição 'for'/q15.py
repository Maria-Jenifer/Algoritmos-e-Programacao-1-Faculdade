# Escreva quais números entre 1000 e 1999 que divididos por 11 dão resto igual a 5.

for i in range(1000, 2000):
    if i % 11 == 5:
        print(i)