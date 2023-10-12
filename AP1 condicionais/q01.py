# 01) Escreva um programa que pergunte o preço de dois produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Qual o preço do seu primeiro produto? '))
produto2 = float(input('Qual o preço do seu primeiro produto? '))

if produto1 < produto2 :
    print('Você deve comprar o primeiro produto')
elif produto2 < produto1 :
    print('Você deve comprar o segundo produto')
else: 
    print('Os produtos tem o mesmo preço. Pode escolher qual comprar!')