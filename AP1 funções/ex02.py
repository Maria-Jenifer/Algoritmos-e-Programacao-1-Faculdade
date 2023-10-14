# Escreva uma função que recebe um número inteiro como parâmetro e deverá retornar um valor lógico para verificar se aquele número é impar ou não

def e_impar(num):
    if num % 2 != 0: 
        return True
    else:
        return False

print(e_impar(23))
print(e_impar(25))
print(e_impar(20))