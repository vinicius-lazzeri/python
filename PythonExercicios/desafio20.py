import random
aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))
bingo = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(bingo)
print('Sorteio da ordem de apresentação: ')
print(bingo)

