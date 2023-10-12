# Escrever um programa que leia 20 valores para uma variável n e, para cada um deles, calcule a tabuada de 1 até n. Mostre a tabuada na forma:
# 1 x n = n
# 2 x n = 2n
# 3 x n = 3n
# .......
# n x n = n2

cont_vezes = 0 

while cont_vezes < 20:
    num = int(input('digite um número para ver sua taboada: '))
    for a in range (1, num+1):
        print('{} X {} = {}'.format(a, num, a*num))
    cont_vezes += 1     