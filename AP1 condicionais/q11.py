# 11) O IMC (índice de massa corpórea) é um critério da Organização Mundial da Saúde para classificar a condição
# de peso de um determinado adulto. A fórmula para o cálculo da mesma é IMC = peso / altura², onde o peso é 
# fornecido em kg e a altura em metros. Escreva um programa que deverá ler da entrada padrão esses dois 
# valores e apresentar a sua classificação com base na tabela a seguir: 


peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

classificacao = ''

if imc < 18.5:
    classificacao = "Baixo peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
elif 30 <= imc < 34.9:
    classificacao = "Obesidade grau 1"
elif 35 <= imc < 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3"

print("Seu IMC é:", imc)
print("Classificação:", classificacao)