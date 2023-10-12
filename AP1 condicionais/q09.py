# 09) Escreva um programa que deverá ler da entrada padrão duas notas de um aluno: n1 e n2. Em seguida,
# o programa deverá apresentar se o aluno foi aprovado por média ou não. Sabe-se que para o aluno ser 
# aprovado por média, o valor da média ponderada de suas notas (peso 2 e 3, respectivamente) deverá ser 
# maior ou igual a 7,0 (sete).


n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (2 * n1 + 3 * n2) / 5 

if media >= 7:
    print('Você foi aprovado. PARABÉNS!!')
else:
    print('Você não foi aprovado.')