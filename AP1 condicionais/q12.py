# 12) Escreva um programa que receba duas notas, calcule e mostre a média aritmética e a mensagem de acordo com a tabela abaixo: 

# Média Aritmética
# Mensagem
# Maior ou igual a 0,00 e Menor do que 3,00
# Reprovado
# Maior ou igual a 3,00 e Menor que 7,00
# Exame Final
# Maior ou igual a 7,0 e menor ou igual a 10,00
# Aprovado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

mensagem = ''
if media >= 0.0 and media < 3.0:
    mensagem = "Reprovado"
elif media >= 3.0 and media < 7.0:
    mensagem = "Exame Final"
elif media >= 7.0 and media <= 10.0:
    mensagem = "Aprovado"
else:
    mensagem = "Média inválida"

print("Média Aritmética: {}".format(media))
print("Mensagem: {}".format(mensagem))


