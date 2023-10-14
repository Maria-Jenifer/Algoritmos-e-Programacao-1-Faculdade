# Escreva uma função que deverá receber dois números inteiros X e Y. A função deverá retornar 0, caso os números sejam iguais; -1 caso o número X seja menor que o número Y; e +1 caso contrário

def num_inteiros(x, y):
    if x == y:
        return '0'
    elif x < y:
        return '-1'
    else:
        return '+1'

print(num_inteiros(5, 23))