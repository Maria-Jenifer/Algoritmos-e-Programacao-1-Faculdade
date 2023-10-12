# 06) Escreva um programa que deverá fazer a leitura do ano atual e do ano de nascimento de uma pessoa e deve
#  informar ao usuário se esta pessoa está apta a tirar a carteira de motorista neste ano. Sabe-se que para
#  tirar a carteira de motorista é necessário a pessoa ter no mínimo 18 anos. 


anoatual = int(input('Qual o ano atual? '))
anonasc = int(input('Qual ano do seu nascimento? '))

total = anoatual - anonasc

if total >= 18:
    print('Você está apto a tirar sua carteira de habilitação')
else: 
    print('Você não pode tirar sua CNH agora.')