# Escreva uma função que deverá receber um número inteiro positivo N como parâmetro. A função deverá retornar o valor do fatorial de N. Obs: não pode utilizar a biblioteca math

def num(n):
    total = 1
    while(n >= 1):
        total = total * n
        n = n - 1
    print(total)

num(5)