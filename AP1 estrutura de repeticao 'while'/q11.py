#Escreva um programa que deverá apresentar o menu de opções apresentado a seguir. Caso não seja digitado nenhuma das opções do menu, o programa deverá apresentar a mensagem “Opção inválida”. Após a realização de uma das opções escolhidas, o programa deverá sempre retornar para o menu.

# Menu de opções: 
# Intervalo de Valores
# Média de Números
# Tabuada da Multiplicação
# Sair

# Na opção 1, o usuário deverá informar dois valores X e Y, e o programa deverá imprimir todos os números de X até Y, incluindo-os. 

# Na opção 2, o usuário deverá informar o valor de N, em seguida o programa deverá realizar a leitura de N números reais em seguida apresentar a média aritmética desses números. 

# Na opção 3, o usuário deverá informar um número inteiro e o programa irá imprimir a tabuada da multiplicação de 1 até 10 daquele número. 

# Quando o usuário digitar a opção 4, o programa deverá imprimir uma mensagem de “Até logo” e encerrar o programa. 
 
opcao = 0 
while opcao != 4:
    opcao = int(input('Menu de opções: Intervalo de valores(1); Média de números(2); Tabuada de multiplicação(3); Sair(4): ')) 
    if opcao == 1:
        X = int(input('Valor de x: '))
        Y = int(input('Valor de Y: '))
        print('O intervalo dos valores é: ')
        for i in range(X, Y + 1):
            print(i)
    if opcao == 2:
        N = int(input('Valor de N: '))
        soma = 0
        for i in range(N):
            numero = int(input('Número: '))
            soma += numero
        print('A média artmética é: {}'.format(soma/N))
    if opcao == 3:
        numero_tab = int(input('Digite um número para saber sua tabuada: '))
        for i in range(1,11):
            print('{} x {} = {}'.format(i, numero_tab, i*numero_tab))
    if opcao == 4:
        print('Até logo')        