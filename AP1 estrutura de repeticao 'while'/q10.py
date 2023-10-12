# Escreva um programa que deverá ler vários números da entrada padrão. Calcule e mostre: 
# a soma dos números digitados
# quantidade de números digitados
# a média dos números digitados;
# o maior número;
# o menor número;
# a média dos números pares; 
# o percentual de números ímpares dentre todos os números digitados. 

# Finalize a leitura dos números com um valor negativo. Este número não deverá ser considerado nos cálculos pedidos

menor_numero = 0
maior_numero = 0
numero = 0
contador = 0 
soma = 0
soma_pares = 0
contador_pares = 0
contador_impares = 0
contador_percentual = 0

while numero >= 0:
    num = float(input('Numero: '))
    numero = num

    if num >= 0: 
        contador += 1
        soma += num 
        if num > maior_numero:
            maior_numero = num
        if num < menor_numero:
            menor_numero = num
        if num % 2 == 0 and num != 0: #verifica se o número é par e diferente de 0
            soma_pares += num
            contador_pares += 1
        if num % 2 != 0:
            contador_impares += 1 
        
print('A soma de números digitados foi: {}'.format(soma))
print('A quantidade de números digitados foi: {}'.format(contador))
print('A média de números digitados foi: {}'.format(soma / contador))
print('O maior número informado foi: {}'.format(maior_numero))
print('O menor número informado foi: {}'.format(menor_numero))
print('A média de números pares é: {}'.format(soma_pares / contador_pares))
print('O percentual de números ímpares dentre todos os números digitados foi: {}%'.format(100 * contador_impares / contador))