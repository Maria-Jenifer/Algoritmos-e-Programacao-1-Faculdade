pesoantigo = float(input('Quanto você pesava a 3 meses? '))
pesoatual = float(input('Quanto você pesa atualmente? '))

taxa = (pesoatual * 100) / pesoantigo - 100

print('A taxa de aumento / diminuição do se peso é: {} %'.format(taxa))