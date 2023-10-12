#  Calcule e imprima os números divisíveis por 5, menores ou iguais a 125.

for i in range(1, 126):
    if i % 5 == 0:
        print(i)