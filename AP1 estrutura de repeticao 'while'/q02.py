#  A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:  
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$100,00.

# O final da leitura de dados se dará com a entrada de um salário negativo.

maior_sal = 0
total_filhos = 0 
salario = 0
contador = 0 
soma_salarios = 0
contador_percentual = 0

while salario >= 0:
    sal = float(input('Salário: '))
    salario = sal

    if sal > 0: 
        qtd_filhos = int(input('Quantos filhos?: ')) 
        contador += 1
        soma_salarios += sal
        total_filhos += qtd_filhos
        if sal > maior_sal:
            maior_sal = sal
        if sal <= 100:
            contador_percentual += 1

print('O maior salário informado foi: {}'.format(maior_sal))
print('A média de salário informado foi: {}'.format(soma_salarios / contador))
print('A média de filhos é de: {}'.format(total_filhos / contador))
print('O percentual de pessoas com salário de até R$100, é: {}%'.format(contador_percentual * 100 / contador))