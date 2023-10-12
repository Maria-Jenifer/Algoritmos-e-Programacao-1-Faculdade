#  Escreva um programa que o usuário informa (através da entrada padrão) uma faixa de valores a ser impressa.

inicio = int(input("Informe o valor inicial: "))
fim = int(input("Informe o valor final: "))

for i in range(inicio, fim + 1):
    print(i)