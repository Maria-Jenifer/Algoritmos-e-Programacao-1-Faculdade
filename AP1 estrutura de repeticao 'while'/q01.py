#  Escrever um programa em Python que leia 5 valores para a, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação.  

aux = 0 

for a in range (1,6):
    valor = int(input('Valor: '))
    if valor < 0:
        aux = aux + 1 
print('A quantidade de numeros negativos é: {}'.format(aux))