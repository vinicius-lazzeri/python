import random
aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))
bingo = (aluno1, aluno2, aluno3, aluno4)
escolhido = random.choice(bingo)
print(f'Aluno 1: {aluno1}| Aluno 2: {aluno2}| Aluno 3:{aluno3}| Aluno 4: {aluno4}| Escolhido: {escolhido}')


