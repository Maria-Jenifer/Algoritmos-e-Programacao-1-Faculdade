# Ler 10 valores, um de cada vez, e contar quantos deles estão no intervalo de [10,50] e quantos estão fora do intervalo.

dentro_intervalo = 0
fora_intervalo = 0

for i in range(10):
    valor = int(input(f"Informe o valor {i+1}: "))
    
    if 10 <= valor <= 50:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

print(f"Valores dentro do intervalo [10, 50]: {dentro_intervalo}")
print(f"Valores fora do intervalo [10, 50]: {fora_intervalo}")