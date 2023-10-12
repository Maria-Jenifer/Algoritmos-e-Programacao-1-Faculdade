# 10) Escreva um programa que deverá analisar se vai ser possível uma determinada pessoa realizar uma viagem 
# de carro ou não. O programa deverá receber da entrada padrão: o consumo do veículo (km/litro), o preço do 
# litro da gasolina (R$), a distância total da viagem (km) e o valor do orçamento da pessoa (R$). Caso o 
# valor a ser gasto com o combustível for maior do que o orçamento desta pessoa o programa deverá apresentar 
# a seguinte mensagem: “Não será possível realizar a viagem, pois o valor a ser gasto ultrapassará o 
# orçamento em X reais”, onde o valor de X é a diferença entre o orçamento e o valor a ser gasto com o 
# combustível. Caso contrário, deverá ser apresentada a seguinte mensagem: “Você poderá viajar com o seu 
# orçamento”.


consumoVeiculo = float(input("Digite o consumo do veículo (km/litro): "))
precoGasolina = float(input("Digite o preço do litro de gasolina (R$/litro): "))
distanciaViagem = float(input("Digite a distância total da viagem (km): "))
orcamento = float(input("Digite o valor do seu orçamento (R$): "))

gastoCombustivel = (distanciaViagem / consumoVeiculo) * precoGasolina

if gastoCombustivel > orcamento:
    diferenca = gastoCombustivel - orcamento
    print("Não será possível realizar a viagem, pois o valor a ser gasto ultrapassará o orçamento em {} reais.".format(diferenca))
else:
    print("Você poderá viajar com o seu orçamento.")
