import random
from time import sleep
print('=' * 18, 'B I N G O', '=' * 18)
print('Será que você consegue adivinhar o nº sorteado?')
print('=' * 47)
n1 = int(input('Digite um número de 0 a 10: '))
n2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
bingo = random.choice(n2)
i = 1
while bingo != n1:
    if bingo != n1:
        print('Você errou, tente novamente!')
        i += 1
        n1 = int(input('Digite um número de 0 a 10: '))
    if bingo == n1:
        print('BINGO!')
        sleep(1.5)
        print('Processando a jogatina...')
        sleep(1.5)
        print(f'Parabéns! Você acertou na tentativa de nº{i}!')
        sleep(1)
print('[FIM] - Press [Shift + F10] to play again!')
