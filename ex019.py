from random import choice
a1 = input('Digite o nome do primeiro aluno:   ')
a2 = input('Digite o nome do segundo aluno:   ')
a3 = input('Digite o nome do terceiro aluno:   ')
a4 = input('Digite o nome do quarto aluno:   ')
alunos = [a1, a2, a3, a4]
print('O aluno sorteado foi {}.' .format(str(choice(alunos))))
