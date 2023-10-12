# 03) Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro 
# número elevado ao segundo número. Ao final, informe se o resultado é maior ou igual a 50.

base = float(input('Digite sua base: '))
expoente = float(input('Digite seu expoente: '))
resultado = base ** expoente

if resultado > 50:
    print('O resultado da sua potência é maior que 50 ')
else:
    print('O resultado da sua potência é menor que 50. ')
