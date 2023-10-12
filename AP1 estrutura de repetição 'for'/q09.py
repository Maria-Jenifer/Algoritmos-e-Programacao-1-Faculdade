# Calcula a soma das idades de N pessoas informadas pelo usuário. O valor de N também é informado pelo usuário.

numero_pessoas = int(input("Informe o número de pessoas: "))
soma_idades = 0

for i in range(numero_pessoas):
    idade = int(input(f"Informe a idade da pessoa {i+1}: "))
    soma_idades += idade
print(f"A soma das idades das {numero_pessoas} pessoas é: {soma_idades}")