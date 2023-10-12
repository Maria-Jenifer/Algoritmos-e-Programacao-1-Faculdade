# 04) Faça um programa que realize 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
# responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

pergunta1 = str(input('Você telefonou para a vitima? (sim/nao) '))
pergunta2 =  str(input('Você esteve no local do crime? (sim/nao) '))
pergunta3 =  str(input('Você mora perto da vitima? (sim/nao) '))
pergunta4 =  str(input('Você devia para a vitima(sim/nao)? '))
pergunta5 =  str(input('Você ja trabalhou com a vitima? (sim/nao) '))

totalSim = 0

if pergunta1 == 'sim':
    totalSim = totalSim + 1
if pergunta2 == 'sim':
    totalSim = totalSim + 1 
if pergunta3 == 'sim':
    totalSim = totalSim + 1
if pergunta4 == 'sim':
    totalSim = totalSim + 1
if pergunta5 == 'sim':
    totalSim = totalSim + 1


if totalSim == 2:
    print('Você é suspeito! ')
elif totalSim >= 3 and totalSim <= 4:
    print('Você é cumplice! ')
elif totalSim == 5: 
    print('Você é assassino! ')
else:
    print('Você é inocente!')