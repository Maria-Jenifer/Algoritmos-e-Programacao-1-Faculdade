# Escreva uma função que deverá receber dois números inteiros A e B como parâmetros. A função deverá imprimir todos os números de A até B (inclusive). 

def num_intervalos(a, b):
    for num in range(a,b + 1):
        print(num)

print(num_intervalos(12,23))