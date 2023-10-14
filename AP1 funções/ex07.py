# Escreva uma função que deverá receber dois números inteiros positivos X e Y como parâmetros. A função deverá imprimir todos os números pares entre X e Y, incluindo os dois valores

def num_positivos(x, y):
    for i in range(x, y + 1):
        if i % 2 == 0:
            print(i)

num_positivos(10, 22)