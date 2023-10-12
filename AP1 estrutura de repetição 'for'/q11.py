# Calcule a média aritmética da soma de todos os números pares compreendidos entre 50 e 82

soma_pares = 0
quantidade_pares = 0

for i in range(50, 83):
    if i % 2 == 0:
        soma_pares += i
        quantidade_pares += 1

if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print(f"A média aritmética dos números pares entre 50 e 82 é: {media_pares:.2f}")
else:
    print("Nenhum número par encontrado no intervalo.")