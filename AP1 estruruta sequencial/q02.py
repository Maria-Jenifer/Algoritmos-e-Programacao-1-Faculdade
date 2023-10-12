salario = int(input('Qual é o deu salario atual?: '))
vendas = int(input('Quantas vendas você fez esse mês?: '))

salariofinal = salario + (vendas + vendas * 5/100)

print('Você receberá ao final do mês R$', salariofinal,)