# Escreva uma função que deverá verificar e retornar em qual categoria de desconto um determinado produto de uma loja se enquadra, considere a tabela apresentada a seguir e a respectiva categoria. A função deverá receber o valor do produto como parâmetro. 

def categoria_desconto(valor_produto):
    if valor_produto >= 100 and valor_produto <= 1000:
        print('ESPECIAL')
    elif valor_produto >= 1001 and valor_produto <= 5000:
        print('VIP')
    elif valor_produto > 5000:
        print('GOLD')      

categoria_desconto(10000)        