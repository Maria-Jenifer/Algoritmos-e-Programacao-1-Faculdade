# Calcular a média das idades informadas no programa anterior.


num_pessoas = int(input("Informe o número de pessoas: "))
soma_idades = 0

for i in range(num_pessoas):
    idade = int(input(f"Informe a idade da pessoa {i+1}: "))
    soma_idades += idade

media_idades = soma_idades / num_pessoas
print(f"A média das idades das {num_pessoas} pessoas é: {media_idades:.2f}")